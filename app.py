import streamlit as st
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceMeshModule import FaceMeshDetector

st.set_page_config(page_title="Face & Hand Controller", layout="centered")
st.title("🧠 Face and Hand Controlled Keyboard System")
run = st.button("Start Detection")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

hand_detector = HandDetector(maxHands=1, detectionCon=0.7)
face_detector = FaceMeshDetector(maxFaces=1)

last_action = None
two_fingers_detected = False
mouth_open_detected = False

def simulate_key_press(key):
    print(f"Simulated key press: {key}")  # Replace with your logic

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
            simulate_key_press('a')
        elif action == 'right':
            simulate_key_press('d')
        last_action = action
    elif action is None:
        last_action = None

def detect_mouth_open(top_lip_y, bottom_lip_y):
    global mouth_open_detected
    if abs(top_lip_y - bottom_lip_y) > 10:
        if not mouth_open_detected:
            simulate_key_press('s')
            mouth_open_detected = True
    else:
        mouth_open_detected = False

if run:
    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape

        frame, faces = face_detector.findFaceMesh(frame, draw=False)
        if faces:
            face = faces[0]
            nose = face[1]
            top_lip = face[13]
            bottom_lip = face[14]
            detect_movement(nose[0], nose[1], frame_width, frame_height)
            detect_mouth_open(top_lip[1], bottom_lip[1])

        hands, frame = hand_detector.findHands(frame)
        if hands:
            hand = hands[0]
            fingers = hand_detector.fingersUp(hand)
            if fingers == [0, 1, 1, 0, 0]:  # Index and middle up
                if not two_fingers_detected:
                    simulate_key_press('w')
                    two_fingers_detected = True
            else:
                two_fingers_detected = False

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

