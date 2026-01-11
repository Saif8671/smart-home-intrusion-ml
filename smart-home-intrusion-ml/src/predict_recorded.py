import cv2
import joblib
import numpy as np
import time
from feature_extraction import FeatureExtractor, extract_features
from alert import trigger_alert
from face_recognition_utils import is_owner

model = joblib.load("model/intrusion_model.pkl")
extractor = FeatureExtractor()

VIDEO_PATH = "recorded_videos/sample.mp4"
cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)

frame_number = 0
last_alert_time = 0
ALERT_COOLDOWN = 5

print("Recorded video owner vs intruder analysis started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_number += 1
    timestamp_sec = frame_number / fps

    features = extract_features(frame, extractor)
    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]
    confidence = model.predict_proba(X)[0][1]

    label = "INTRUSION" if prediction == 1 else "NORMAL"
    color = (0, 0, 255) if prediction == 1 else (0, 255, 0)

    cv2.putText(frame, f"{label} ({round(confidence,2)})", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    current_time = time.time()
    if prediction == 1 and (current_time - last_alert_time) > ALERT_COOLDOWN:
        if not is_owner(frame):
            print(f"[!] Intruder detected at {round(timestamp_sec,2)} sec")
            trigger_alert(frame, confidence)
        else:
            print(f"[+] Owner detected at {round(timestamp_sec,2)} sec")
        last_alert_time = current_time

    cv2.imshow("Recorded Video Analysis", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Recorded video analysis completed.")
