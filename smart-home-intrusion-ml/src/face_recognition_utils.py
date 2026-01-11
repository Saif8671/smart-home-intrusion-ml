import face_recognition
import os

# Load owner images and encode them
owner_images = [f"owners/{f}" for f in os.listdir("owners")]
owner_encodings = []

for img_path in owner_images:
    img = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(img)
    if encodings:
        owner_encodings.append(encodings[0])

def is_owner(frame):
    rgb_frame = frame[:, :, ::-1]  # BGR to RGB
    faces = face_recognition.face_encodings(rgb_frame)
    for face in faces:
        matches = face_recognition.compare_faces(owner_encodings, face, tolerance=0.5)
        if True in matches:
            return True
    return False
