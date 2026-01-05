**AI Virtual Mouse**

A computer vision-based application that allows users to control their mouse cursor and perform clicks using hand gestures. This project leverages MediaPipe for robust hand tracking and geometric heuristics to interpret specific gestures as mouse actions.

📋 Features

Cursor Control: Move the mouse pointer by tracking the index finger tip.

Left Click: Triggered by curling the index finger while keeping the middle finger straight.

Right Click: Triggered by curling the middle finger while keeping the index finger straight.

Double Click: Triggered by curling both the index and middle fingers.

Screenshot: Triggered by curling both index and middle fingers while tucking the thumb in.

🛠️ Tech Stack & Dependencies

Python 3.x

OpenCV (cv2): For video capture and image processing.

MediaPipe (mediapipe): For real-time, on-device hand landmark detection.

PyAutoGUI (pyautogui): For programmatically controlling the mouse cursor and screen capture.

Pynput (pynput): Used for specific mouse button press events.

NumPy (numpy): For efficient geometric calculations (angles and distances).

🚀 Installation

Clone the repository (or download the source files):

virtual_mouse.py

util.py

Install the required dependencies:
Run the following command in your terminal:

pip install opencv-python mediapipe pyautogui pynput numpy



💻 Usage

Run the main script:

python virtual_mouse.py



Webcam Initialization: The application will open a window showing your webcam feed. Ensure your hand is visible and well-lit.

Gestures Reference:

| Action | Hand Gesture Logic |
| Move Cursor | Point with your Index Finger. The cursor maps to the tip position. |
| Left Click | Curl Index Finger (Angle < 50°) while holding Middle Finger straight. |
| Right Click | Curl Middle Finger (Angle < 50°) while holding Index Finger straight. |
| Double Click | Curl Both Index and Middle Fingers. (Thumb must be away from the palm). |
| Screenshot | Curl Both Index and Middle Fingers + Tuck Thumb in (Thumb tip close to Index base). |

Exit: Press q on your keyboard to close the application.

📂 Project Structure

virtual_mouse.py: The entry point. Handles the video loop, MediaPipe initialization, gesture detection logic, and execution of mouse commands.

util.py: Contains utility functions for geometry.

get_angle(a, b, c): Calculates the angle between three points (used to determine if a finger is curled or straight).

get_distance(landmark_list): Calculates the Euclidean distance between points (used to check thumb proximity).

⚙️ Architecture Note

The system uses a geometric approach rather than a trained classification model for gesture recognition. This ensures lower latency and high performance on standard CPUs.

Landmark Detection: MediaPipe extracts 21 3D hand landmarks.

Heuristic Analysis:

Angles are calculated at the finger joints (PIP-MCP-DIP) to determine state (Open/Closed).

Distances are normalized to adapt to hand depth relative to the camera.

⚠️ Troubleshooting

Cursor Jitter: Ensure your lighting is consistent. MediaPipe is robust, but extreme shadows can cause landmark instability.

Screen Size Mapping: The mouse movement is currently mapped to index_finger_tip.y / 2 to restrict the active area to the top half of the frame. You can adjust this factor in move_mouse inside virtual_mouse.py.
