#Step1: Open Webcamera
#Step2: Detect the Hand
#Step3: Separate index finger from the rest ["REMEMBER: Counting starts from center of the wrist and then the thumb then index finger and goes on"] {Trying for thumb as well}
#Step4: Move the Mouse pointer using finger
#Step5: Click

import cv2 #computer vision2 for python
import mediapipe as mp #detection er jonno
import pyautogui #mouse move korar jonno
cap = cv2.VideoCapture(0) #capture webcam
hand_detector = mp.solutions.hands.Hands() #hand detector ache ete
drawing_utils = mp.solutions.drawing_utils #initialization of drawing tools-
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:# run forever
    _ , frame = cap.read() #_ mane i dont need it ; frame mane video r frame; cap.read mane jeta webcam e dekhacche
    frame = cv2.flip(frame , 1) #jehetu ulto asche tai reverse korchi
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #rgb colour convert korche from black green red to red green black. frame theke convert korche
    output = hand_detector.process(rgb_frame) #jeta input amra dicchi seta process kore output dicche eta
    hands = output.multi_hand_landmarks #landmarks ,mane points on my hand
    # print(hands) #amar output ke print korchi
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame , hand) #amar haath er opore drawing korbe each and every point of my hand
            landmarks = hand.landmark #recognizing the index finger
            for id, landmark in enumerate(landmarks): #knowing the index number
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255), thickness= 2) # image holo frame mane index finger, center x y mane point , radius mane to kotota boro, color code ota yellow 
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255), thickness= 2) 
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    # print("outside",abs(index_y - thumb_y)) #checking the position of the fingers
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    
    cv2.imshow('VirtualMouse', frame) #imshow mane image show.
    if cv2.waitKey(1) == ord('q'): #waitkey(1) mane 1second wait kore tar por break kore debe..
        break
