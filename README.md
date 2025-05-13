# NoKeyBoardGaming

# 🧠 Face and Hand Controlled Keyboard Input System

This Python project enables gesture-based control using your webcam. It detects specific face and hand gestures and maps them to keyboard inputs (W, A, S, D), allowing you to interact with applications hands-free or in an assistive tech context.

---

## 📦 Features

* 👃 Head movement (nose position) → triggers A (left) or D (right)
* 👄 Mouth opening → triggers S (down)
* ✌️ Two fingers up (index + middle) → triggers W (up)
* Real-time video feed from webcam
* Lightweight and easy to modify

---

## 🚀 Technologies Used

* OpenCV for real-time video capture and processing
* cvzone for high-level hand and face mesh detection
* pynput for keyboard event simulation

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/face-hand-control.git
cd face-hand-control
```

2. Install dependencies:

```bash
pip install opencv-python cvzone pynput
```

> Ensure your camera works and Python 3.7+ is installed.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Controls:

* Move your nose left or right → simulates A or D
* Move nose upward → simulates W (via two fingers)
* Open mouth → simulates S
* Raise index + middle fingers → simulates W

Press Q to quit the app.

---

## 🧠 How It Works

| Gesture                | Keyboard |
| ---------------------- | -------- |
| Move nose left/right   | A / D    |
| Raise two fingers (🖖) | W        |
| Open mouth             | S        |

The script uses cvzone’s FaceMeshModule to detect facial landmarks and HandTrackingModule to detect finger positions. Movement beyond thresholds is interpreted as directional input.

---

## 📸 Screenshots

<p float="left">
  <img src="screenshot.png" width="400" />
</p>

---

## 💡 Use Cases

* Accessibility tools for motor-impaired users
* Gesture-controlled games or presentations
* Hands-free control systems

---

## 🛠️ Customize

* Tune thresholds (e.g., mouth\_open\_threshold, nose movement threshold) as per your camera’s distance and lighting.
* Add more gestures using additional facial landmarks or finger combinations.

---

## 🧑‍💻 Author

Soham Dey — [LinkedIn](https://www.linkedin.com/in/soham-dey-891332256) | [GitHub](https://github.com/7sohamd)

---

Let me know if you'd like a badge-style README or want to deploy it as a demo app (e.g., with Streamlit or a GUI).
