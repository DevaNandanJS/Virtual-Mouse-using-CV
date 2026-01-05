import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hand_detector = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y=0


cam= cv2.VideoCapture(0)

while True:
    _ , frame= cam.read()
    frame= cv2.flip(frame,1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output= hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    

    if hands:
        for hand in hands:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            landmarks= hand.landmark
            for id, landmark in enumerate(landmarks):
                x= int(landmark.x * frame_width)
                y= int(landmark.y * frame_height)
                print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x= screen_width/frame_width*x
                    index_y= screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x= screen_width/frame_width*x
                    thumb_y= screen_height/frame_height*y
                    print("outside", abs(index_y - thumb_y))

                    if abs(index_y - thumb_y) < 80:
                        pyautogui.click()
                        pyautogui.sleep(1)
                

    cv2.imshow("mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cam.release()
cv2.destroyAllWindows() 