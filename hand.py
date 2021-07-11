import cv2 as cv
import mediapipe as mp
import numpy as np


class HandDetection:

    def __init__(self, capture, min_confidence=0.5, max_hands=1, mode=False):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=mode, max_num_hands=max_hands, min_detection_confidence=min_confidence)
        self.capture = capture
        self.coords = None
        self.frame = None
        self.diference = None
        # reference vars
        self.finger_names = ["THUMB_TIP", "INDEX_FINGER_TIP",
                             "MIDDLE_FINGER_TIP", "RING_FINGER_TIP", "PINKY_TIP"]
        self.finger_numbers = [4, 8, 12, 16, 20]
        self.index = [8, 11]

    def Run(self):
        ret, frame = self.capture.read()
        if ret == False:
            print("No video input sources found!")
        heigth, width, _ = frame.shape
        frame = cv.flip(frame, 1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                for (i, poins) in enumerate(hand_landmarks.landmark):
                    if i == self.index[0]:
                        coor_x = int(poins.x * width)
                        coor_y = int(poins.y * heigth)
                    if i == self.index[1]:
                        x = int(poins.x * width)
                        y = int(poins.y * heigth)
                self.coords = {"x": coor_x, "y": coor_y}
                self.diference = self.distance(coor_x, coor_y, x, y)
        else:
            self.coords = None
            self.diference = None

    def distance(self, x1, y1, x2, y2):
        return np.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))