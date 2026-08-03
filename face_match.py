
from PIL import Image
import io
import os
import cv2
import sys
import numpy as np
import requests
import cloudinary
import cloudinary.api
import cloudinary_config
print(cloudinary.config().cloud_name)

from insightface.app import FaceAnalysis
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=-1)

files = os.listdir("selfies")

if len(files) == 0:
    print("No selfie found")
    exit()

selfie_path = os.path.join("selfies", files[0])
selfie = cv2.imread(selfie_path)

if selfie is None:
    print("Cannot load selfie")
    exit()
selfie_faces = app.get(selfie)

if len(selfie_faces) == 0:
    print("No face detected")
    exit()

selfie_embedding = selfie_faces[0].embedding
event_name = sys.argv[1]
resources = cloudinary.api.resources(
    type="upload",
    prefix=event_name,
    max_results=100
)

photos = resources["resources"]

print("Total Photos Found:", len(photos))

matched_photos = []   

for photo in photos:
    image_url = photo["secure_url"]

    response = requests.get(image_url)

    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)

    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if img is None:
        continue

    faces = app.get(img)

    print("Faces detected:", len(faces), image_url)

    if len(faces) == 0:
        continue

    for face in faces:

        similarity = np.dot(
            selfie_embedding,
            face.embedding
        ) / (
            np.linalg.norm(selfie_embedding)
            * np.linalg.norm(face.embedding)
        )

        print(image_url, "Similarity:", round(similarity, 2))

        # if similarity >= 0.50:
        if similarity >= 0.50:
            matched_photos.append(image_url)
            print("✅ MATCH FOUND:", image_url)
            break

print("\nMatched Photos:", len(matched_photos))

with open("matched.txt", "w") as f:
    for photo in matched_photos:
        f.write(photo + "\n")

print("Program Finished")
