# 🏠 Smart Home Intrusion Detection System (ML + Vision)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-orange.svg)
![Status](https://img.shields.io/badge/Status-Working-success.svg)

A **Machine Learning–based Smart Home Security System** that classifies activities as **Normal**, **Owner**, or **Intrusion** using **video analysis, motion features, and face recognition**.  
The system supports **Live Camera Mode** and **Recorded Video Mode**, captures evidence, and raises alerts for intrusions.

---

## 🚀 Features

- ✅ Dual Mode Operation  
  - **Live Camera Feed**
  - **Recorded `.mp4` Video**
- 🧠 ML-based Activity Classification  
  - Normal Activity  
  - Suspicious / Intrusion
- 👤 **Owner vs Intruder Identification**
- 📸 Automatic Image Capture on Intrusion
- 🔔 Alert Triggering for Suspicious Events
- ⚙️ Modular, Extendable Architecture

---

## 🧠 System Workflow

```
Video Input (Live / Recorded)
↓
Motion Detection + Feature Extraction
↓
ML Classifier (Normal / Suspicious)
↓
Face Recognition
┌───────────────┐
│ │
Owner Intruder
│ │
Ignore Alert + Capture Image

```
---

## 📁 Project Structure
```
smart-home-intrusion-ml/
│
├── src/
│ ├── predict_live.py # Live camera detection
│ ├── predict_recorded.py # Recorded video detection
│ ├── face_recognition_utils.py # Owner vs intruder logic
│
├── owners/ # Owner face images
│ ├── owner1.jpg
│ ├── owner2.jpg
│
├── alerts/ # Captured intrusion images
│
├── videos/
│ └── sample.mp4 # Test recorded video
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|------------|
| Language | Python |
| Vision | OpenCV |
| ML | Scikit-learn |
| Face Recognition | face_recognition (dlib) |
| Alerts | Image Capture + Logs |

---

## ⚙️ Installation

### 🔹 Step 1: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

🔹 Step 2: Install Dependencies

``` bash
pip install opencv-python numpy pandas scikit-learn
pip install face_recognition
```
⚠️ Important (Windows users)
If dlib fails to install:

Install Visual Studio C++ Build Tools
OR use conda:
```bash
conda install -c conda-forge dlib
```
## 🧑‍💼 Owner Setup (Required)

Create a folder:
owners/
Add 5–10 clear images of the owner
Different angles
Different lighting
JPG or PNG format

Example:
```
owners/
├── user1.jpg
├── user2.jpg
```
## ▶️ Running the System
🔴 Live Camera Mode:
```
python src/predict_live.py
```
Uses webcam
Detects motion
Identifies owner vs intruder
Saves alert images

### 🎥 Recorded Video Mode
Put any .mp4 file inside videos/
```
Run:
python src/predict_recorded.py
```
## 🚨 Alert Mechanism
Triggered when:
Activity classified as Suspicious
Face does not match owner

Automatically:
Captures frame
Saves image in alerts/
Prints intrusion warning

📸 Sample Alert Output
[ALERT] Intruder detected!
Image saved: alerts/intrusion_2026-01-13_10-45-32.jpg

## 🧩 Customization Ideas
Add SMS / Email alerts
Use deep CNN instead of classical ML
Multi-owner support
Cloud storage for alerts
Sound anomaly detection
Door/window IoT sensor integration

## 🎯 Use Cases
Home Security Systems
Hostel / PG Monitoring
Smart Office Surveillance

##👨‍💻 Author

Saif Ur Rahman
Cybersecurity | ML | AI
📧 saifurrahman887@gmail.com
🔗 LinkedIn: https://linkedin.com/in/saif-ur-rahman-0211002b9
