import cv2

class Drawer:
    def __init__(self, brush_thickness=8, eraser_thickness=40):
        self.brush_thickness = brush_thickness
        self.eraser_thickness = eraser_thickness
        self.prev_x, self.prev_y = 0, 0

    def draw(self, canvas, lmList, fingers):
        # Index finger tip
        x1, y1 = lmList[8][1], lmList[8][2]

        # If only index finger is up → DRAW
        if fingers[1] == 1 and fingers[2] == 0:
            if self.prev_x == 0 and self.prev_y == 0:
                self.prev_x, self.prev_y = x1, y1

            cv2.line(canvas, (self.prev_x, self.prev_y),
                     (x1, y1), (255, 0, 255), self.brush_thickness)

            self.prev_x, self.prev_y = x1, y1

        # If index + middle finger → ERASE
        elif fingers[1] == 1 and fingers[2] == 1:
            cv2.circle(canvas, (x1, y1),
                       self.eraser_thickness, (0, 0, 0), -1)
            self.prev_x, self.prev_y = 0, 0

        else:
            self.prev_x, self.prev_y = 0, 0

        return canvas