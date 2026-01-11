import cv2
import os
from datetime import datetime

def trigger_alert(frame, confidence):
    os.makedirs("intrusions", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"intrusions/intrusion_{timestamp}_conf_{round(confidence,2)}.jpg"
    cv2.imwrite(filename, frame)
    print("ALERT! Intrusion detected.")
    print("Image captured:", filename)
