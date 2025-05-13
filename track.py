import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector
from pynput.keyboard import Controller

keyboard = Controller()
cap = cv2.VideoCapture(0)

# Init detectors
hand_detector = HandDetector(maxHands=1, detectionCon=0.7)
face_detector = FaceMeshDetector(maxFaces=1)

last_action = None
two_fingers_detected = False
mouth_open_detected = False

def detect_movement(nose_x, nose_y, frame_width, frame_height):
    global last_action
    center_x, center_y = frame_width // 2, frame_height // 2
    threshold_x, threshold_y = 50, 40

    action = None
    if nose_x < center_x - threshold_x:
        action = 'left'
    elif nose_x > center_x + threshold_x:
        action = 'right'
    elif nose_y < center_y - threshold_y:
        action = 'up'

    if action and action != last_action:
        if action == 'left':
            keyboard.press('a')
            keyboard.release('a')
        elif action == 'right':
            keyboard.press('d')
            keyboard.release('d')
        last_action = action
    elif action is None:
        last_action = None

def detect_mouth_open(top_lip_y, bottom_lip_y):
    global mouth_open_detected
    mouth_open_threshold = 10  # Adjust as needed
    if abs(top_lip_y - bottom_lip_y) > mouth_open_threshold:
        if not mouth_open_detected:
            keyboard.press('s')
            keyboard.release('s')
            mouth_open_detected = True
    else:
        mouth_open_detected = False

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Detect face
    frame, faces = face_detector.findFaceMesh(frame, draw=False)
    if faces:
        face = faces[0]
        nose = face[1]  # Nose tip
        top_lip = face[13]
        bottom_lip = face[14]
        detect_movement(nose[0], nose[1], frame_width, frame_height)
        detect_mouth_open(top_lip[1], bottom_lip[1])

    # Detect hand
    hands, frame = hand_detector.findHands(frame)
    if hands:
        hand = hands[0]
        fingers = hand_detector.fingersUp(hand)
        if fingers == [0, 1, 1, 0, 0]:  # Index and middle up
            if not two_fingers_detected:
                keyboard.press('w')
                keyboard.release('w')
                two_fingers_detected = True
        else:
            two_fingers_detected = False

    cv2.imshow("Control with Face & Hands", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
