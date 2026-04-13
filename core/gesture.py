class GestureDetector:
    def __init__(self):
        # Finger tip IDs
        self.tipIds = [4, 8, 12, 16, 20]

    def get_fingers(self, lmList):
        fingers = []

        # Thumb
        if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        for id in range(1, 5):
            if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers