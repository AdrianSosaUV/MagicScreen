
from settings import *
from hand import *


class MagicScreen:

    def __init__(self):
        """
        Init function
        """
        self.capture = cv.VideoCapture(0, cv.CAP_DSHOW)
        self.hands = HandDetection(self.capture)
        self.Config()

    def Run(self):
        """
        Main function
        """
        while self.running:
            # Finger selection
            self.hands.IndexFinger()
            # Video imput
            ret, self.frame = self.capture.read()
            if ret is False:
                self.running == False
            # Flip video
            self.frame = cv.flip(self.frame, 1)
            # Shuffle color scale
            self.frameHSV = cv.cvtColor(self.frame, cv.COLOR_RGB2HSV)
            # Aux matrix
            if self.imAux is None:
                self.imAux = np.zeros(self.frame.shape, dtype=np.uint8)
            # Left panel / Color
            cv.rectangle(self.frame, (5, 5), (55, 55),
                         RECTANGLE_1_COLOR, self.RECTANGLE_1_WIDTH)
            cv.rectangle(self.frame, (60, 5), (110, 55),
                         RECTANGLE_2_COLOR, self.RECTANGLE_2_WIDTH)
            cv.rectangle(self.frame, (115, 5), (165, 55),
                         RECTANGLE_3_COLOR, self.RECTANGLE_3_WIDTH)
            cv.rectangle(self.frame, (170, 5), (220, 55),
                         RECTANGLE_4_COLOR, self.RECTANGLE_4_WIDTH)
            # Center panel / Erase
            cv.rectangle(self.frame, (230, 5), (430, 55), ORANGE, SMALL)
            cv.putText(self.frame, "Clear", (315, 25),
                       6, 0.6, ORANGE, 1, cv.LINE_AA)
            cv.putText(self.frame, "Screen", (310, 45),
                       6, 0.6, ORANGE, 1, cv.LINE_AA)
            # Right panel / Size
            cv.rectangle(self.frame, (440, 5), (480, 55),
                         BLACK, self.RECTANGLE_5_WIDTH)
            cv.circle(self.frame, (460, 30), SMALL, BLACK, -1)
            cv.rectangle(self.frame, (490, 5), (530, 55),
                         BLACK, self.RECTANGLE_6_WIDTH)
            cv.circle(self.frame, (510, 30), MEDIUM, BLACK, -1)
            cv.rectangle(self.frame, (540, 5), (580, 55),
                         BLACK, self.RECTANGLE_7_WIDTH)
            cv.circle(self.frame, (560, 30), LARGE, BLACK, -1)
            cv.rectangle(self.frame, (590, 5), (630, 55),
                         BLACK, self.RECTANGLE_8_WIDTH)
            cv.circle(self.frame, (610, 30), XLARGE, BLACK, -1)

            # Principal loop
            try:
                # Turn on the magic pen
                ## modify this condition for each finger of each person
                ## this is the distance between the TIP and MCP finger points
                ## for more info about finger points read the docs from docs.opencv.org
                if self.hands.diference > 85:
                    # Finger's coordinates
                    self.x2 = self.hands.coords["x"]
                    self.y2 = self.hands.coords["y"]
                    # Button's selection
                    if self.x1 is not None:
                        # Config for buttons
                        if 5 < self.x2 < 55 and 5 < self.y2 < 55:
                            self.COLOR = RECTANGLE_1_COLOR
                            self.RECTANGLE_1_WIDTH = LARGE
                            self.RECTANGLE_2_WIDTH = SMALL
                            self.RECTANGLE_3_WIDTH = SMALL
                            self.RECTANGLE_4_WIDTH = SMALL
                        if 60 < self.x2 < 110 and 5 < self.y2 < 55:
                            self.COLOR = RECTANGLE_2_COLOR
                            self.RECTANGLE_1_WIDTH = SMALL
                            self.RECTANGLE_2_WIDTH = LARGE
                            self.RECTANGLE_3_WIDTH = SMALL
                            self.RECTANGLE_4_WIDTH = SMALL
                        if 115 < self.x2 < 165 and 5 < self.y2 < 55:
                            self.COLOR = RECTANGLE_3_COLOR
                            self.RECTANGLE_1_WIDTH = SMALL
                            self.RECTANGLE_2_WIDTH = SMALL
                            self.RECTANGLE_3_WIDTH = LARGE
                            self.RECTANGLE_4_WIDTH = SMALL
                        if 170 < self.x2 < 220 and 5 < self.y2 < 55:
                            self.COLOR = RECTANGLE_4_COLOR
                            self.RECTANGLE_1_WIDTH = SMALL
                            self.RECTANGLE_2_WIDTH = SMALL
                            self.RECTANGLE_3_WIDTH = SMALL
                            self.RECTANGLE_4_WIDTH = LARGE
                        if 440 < self.x2 < 480 and 5 < self. y2 < 55:
                            self.SIZE = SMALL
                            self.RECTANGLE_5_WIDTH = LARGE
                            self.RECTANGLE_6_WIDTH = SMALL
                            self.RECTANGLE_7_WIDTH = SMALL
                            self.RECTANGLE_8_WIDTH = SMALL
                        if 490 < self.x2 < 530 and 5 < self.y2 < 55:
                            self.SIZE = MEDIUM
                            self.RECTANGLE_5_WIDTH = SMALL
                            self.RECTANGLE_6_WIDTH = LARGE
                            self.RECTANGLE_7_WIDTH = SMALL
                            self.RECTANGLE_8_WIDTH = SMALL
                        if 540 < self.x2 < 580 and 5 < self.y2 < 55:
                            self.SIZE = LARGE
                            self.RECTANGLE_5_WIDTH = SMALL
                            self.RECTANGLE_6_WIDTH = SMALL
                            self.RECTANGLE_7_WIDTH = LARGE
                            self.RECTANGLE_8_WIDTH = SMALL
                        if 590 < self.x2 < 630 and 5 < self.y2 < 55:
                            self.SIZE = XLARGE
                            self.RECTANGLE_5_WIDTH = SMALL
                            self.RECTANGLE_6_WIDTH = SMALL
                            self.RECTANGLE_7_WIDTH = SMALL
                            self.RECTANGLE_8_WIDTH = LARGE
                        if 230 < self.x2 < 430 and 5 < self.y2 < 55:
                            cv.rectangle(self.frame, (230, 5),
                                         (430, 55), ORANGE, LARGE)
                            # Erase Screen draft
                            self.imAux = np.zeros(
                                self.frame.shape, dtype=np.uint8)
                        if 0 < self.y2 < 60 or 0 < self.y1 < 60:
                            # Not drawing on buttons section
                            self.imAux = self.imAux
                        else:
                            # Draw the stroke
                            self.imAux = cv.line(
                                self.imAux, (self.x1, self.y1), (self.x2, self.y2), self.COLOR, self.SIZE)
                        # Draw a circle on fingertip as a pointer
                        cv.circle(self.frame, (self.x2, self.y2),
                                  SMALL, self.COLOR, self.SIZE)
                    self.x1, self.y1 = self.x2, self.y2
                else:
                    self.x1, self.y1 = None, None
            except:
                pass
            # Aux img to Gray scale
            self.imAuxGray = cv.cvtColor(self.imAux, cv.COLOR_RGB2GRAY)
            # Threshold
            _, th = cv.threshold(self.imAuxGray, 10, 255, cv.THRESH_BINARY)
            # Threshold inverse B&W to W&B
            thInv = cv.bitwise_not(th)
            # Overlays the W&B aux and frame
            self.frame = cv.bitwise_and(self.frame, self.frame, mask=thInv)
            # Add aux img to frame
            self.frame = cv.add(self.frame, self.imAux)

            cv.imshow('MagicScreen', self.frame)

            if cv.waitKey(1) & 0xFF == 27:
                self.Close()

    def Close(self):
        """
        Function for Close the App
        """
        self.running = False
        self.capture.release()
        cv.destroyAllWindows()
        sys.exit()

    def Config(self):
        """
        Auxiliary function
        """
        self.RECTANGLE_1_WIDTH = SMALL
        self.RECTANGLE_2_WIDTH = SMALL
        self.RECTANGLE_3_WIDTH = SMALL
        self.RECTANGLE_4_WIDTH = SMALL
        self.RECTANGLE_5_WIDTH = SMALL
        self.RECTANGLE_6_WIDTH = SMALL
        self.RECTANGLE_7_WIDTH = SMALL
        self.RECTANGLE_8_WIDTH = SMALL
        self.running = True
        self.imAux = None
        self.x1 = None
        self.y1 = None
        self.COLOR = GREEN
        self.SIZE = SMALL