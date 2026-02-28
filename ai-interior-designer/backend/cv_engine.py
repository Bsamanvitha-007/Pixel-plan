import cv2
import numpy as np

def analyze_room(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    room_type = "Living Room"
    if brightness < 80:
        room_type = "Low Light Room"

    return {
        "brightness": float(brightness),
        "room_type": room_type
    }