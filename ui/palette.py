import cv2

def select_color(x, y):
    if y < 100:
        if 0 < x < 200:
            return (255, 0, 255)
        elif 200 < x < 400:
            return (255, 0, 0)
        elif 400 < x < 600:
            return (0, 255, 0)
    return None