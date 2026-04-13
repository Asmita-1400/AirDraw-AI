import numpy as np

def create_canvas(width, height):
    return np.zeros((height, width, 3), dtype=np.uint8)