import cv2
import joblib
import numpy as np
import time
from feature_extraction import FeatureExtractor, extract_features
from alert import trigger_alert
from face_recognition_utils import is_owner

model = joblib.load("model/intrusion_model.pkl")
extractor = FeatureExtractor()

cap = cv2.VideoCapture(0)
print("Live owner vs intruder detection started. Press Q to exit.")

last_alert_time = 0
ALERT_COOLDOWN = 5  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    features = extract_features(frame, extractor)
    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]
    confidence = model.predict_proba(X)[0][1]

    label = "INTRUSION" if prediction == 1 else "NORMAL"
    color = (0, 0, 255) if prediction == 1 else (0, 255, 0)

    cv2.putText(frame, f"{label} ({round(confidence,2)})", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Alert only for intruders
    current_time = time.time()
    if prediction == 1 and (current_time - last_alert_time) > ALERT_COOLDOWN:
        if not is_owner(frame):
            trigger_alert(frame, confidence)
        else:
            print("Owner detected. No alert.")
        last_alert_time = current_time

    cv2.imshow("Smart Home Security - Live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
