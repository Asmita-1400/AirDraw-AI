import cv2
from core.hand_tracker import HandTracker
from core.gesture import GestureDetector
from core.drawer import Drawer
from ui.canvas import create_canvas
from config.settings import *

# ✅ Try multiple camera indices (0,1,2)
def initialize_camera():
    for i in range(3):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            print(f"✅ Camera opened with index {i}")
            return cap
    return None

cap = initialize_camera()

if cap is None:
    print("❌ Failed to access camera")
    exit()

cap.set(3, WIDTH)
cap.set(4, HEIGHT)

# Initialize modules
tracker = HandTracker(
    detection_confidence=DETECTION_CONFIDENCE,
    tracking_confidence=TRACKING_CONFIDENCE
)

gesture = GestureDetector()

drawer = Drawer(
    brush_thickness=BRUSH_THICKNESS,
    eraser_thickness=ERASER_THICKNESS
)

# Create canvas
canvas = create_canvas(WIDTH, HEIGHT)

while True:
    success, frame = cap.read()

    if not success:
        print("❌ Camera read failed")
        break

    frame = cv2.flip(frame, 1)

    # Detect hands
    frame = tracker.find_hands(frame)
    lmList = tracker.get_position(frame)

    if lmList:
        fingers = gesture.get_fingers(lmList)
        canvas = drawer.draw(canvas, lmList, fingers)

    # Merge canvas
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    # UI Text
    cv2.putText(frame, "Press Q to Exit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("AirDraw", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()