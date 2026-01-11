import cv2
import numpy as np
import time
from datetime import datetime

class FeatureExtractor:
    def __init__(self):
        self.prev_frame = None
        self.movement_counter = 0
        self.last_reset = time.time()

    def motion_level(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return 0

        delta = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        motion = np.sum(thresh) / 255

        if motion > 5000:
            self.movement_counter += 1

        self.prev_frame = gray
        return motion

    def movement_frequency(self):
        if time.time() - self.last_reset >= 10:
            count = self.movement_counter
            self.movement_counter = 0
            self.last_reset = time.time()
            return count
        return self.movement_counter

def extract_features(frame, extractor):
    motion = extractor.motion_level(frame)
    movement = extractor.movement_frequency()
    hour = datetime.now().hour
    sound = min(motion / 1000, 10)

    door_open = 1 if hour >= 22 and motion > 6000 else 0
    window_open = 1 if hour <= 5 and motion > 6000 else 0

    return [motion, sound, movement, hour, door_open, window_open]
