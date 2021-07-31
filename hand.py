from settings import *


class HandDetection:

    def __init__(self, capture, min_confidence=0.5, max_hands=1, mode=False):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=mode, max_num_hands=max_hands, min_detection_confidence=min_confidence)
        self.capture = capture
        self.coords = None
        self.height = None
        self.width = None
        self.diference = None

    def Landmarks(self):
        ret, frame = self.capture.read()
        if ret == False:
            print("No video input sources found!")
        self.height, self.width, _ = frame.shape
        frame = cv.flip(frame, 1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks is not None:
            return results.multi_hand_landmarks
        else:
            return None

    def ThumbFinger(self):
        landmarks = self.Landmarks()
        if landmarks is not None:
            for hand_LM in landmarks:
                x = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * self.width)
                y = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * self.height)
                x1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.THUMB_MCP].x * self.width)
                y1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.THUMB_MCP].y * self.height)
            self.coords = {"x": x, "y": y}
            self.diference = self.distance(x, y, x1, y1)
        else:
            self.coords = None
            self.diference = None

    def IndexFinger(self):
        landmarks = self.Landmarks()
        if landmarks is not None:
            for hand_LM in landmarks:
                x = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * self.width)
                y = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * self.height)
                x1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].x * self.width)
                y1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP].y * self.height)
            self.coords = {"x": x, "y": y}
            self.diference = self.distance(x, y, x1, y1)
        else:
            self.coords = None
            self.diference = None

    def MiddleFinger(self):
        landmarks = self.Landmarks()
        if landmarks is not None:
            for hand_LM in landmarks:
                x = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * self.width)
                y = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * self.height)
                x1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x * self.width)
                y1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * self.height)
            self.coords = {"x": x, "y": y}
            self.diference = self.distance(x, y, x1, y1)
        else:
            self.coords = None
            self.diference = None

    def RingFinger(self):
        landmarks = self.Landmarks()
        if landmarks is not None:
            for hand_LM in landmarks:
                x = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * self.width)
                y = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * self.height)
                x1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].x * self.width)
                y1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.RING_FINGER_MCP].y * self.height)
            self.coords = {"x": x, "y": y}
            self.diference = self.distance(x, y, x1, y1)
        else:
            self.coords = None
            self.diference = None

    def PinkyFinger(self):
        landmarks = self.Landmarks()
        if landmarks is not None:
            for hand_LM in landmarks:
                x = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * self.width)
                y = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * self.height)
                x1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.PINKY_MCP].x * self.width)
                y1 = int(
                    hand_LM.landmark[self.mp_hands.HandLandmark.PINKY_MCP].y * self.height)
            self.coords = {"x": x, "y": y}
            self.diference = self.distance(x, y, x1, y1)
        else:
            self.coords = None
            self.diference = None

    def distance(self, x1, y1, x2, y2):
        return np.sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))
