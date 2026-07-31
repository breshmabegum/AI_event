# # import cv2
# # import insightface

# # app = insightface.app.FaceAnalysis()
# # app.prepare(ctx_id=0)

# # image = cv2.imread("DSC_2876.JPG")

# # faces = app.get(image)

# # print("Faces Found:", len(faces))


# # import os
# # import cv2
# # import numpy as np
# # import insightface

# # # AI Model
# # app = insightface.app.FaceAnalysis(name="buffalo_l")
# # app.prepare(ctx_id=-1)   # CPU mode

# # # Selfie
# # selfie = cv2.imread("selfies/selfie.jpg")
# # faces = app.get(selfie)

# # if len(faces) == 0:
# #     print("No face found in selfie")
# #     exit()

# # selfie_embedding = faces[0].embedding

# # matched = []

# # for file in os.listdir("uploads"):

# #     if file.lower().endswith((".jpg", ".jpeg", ".png")):

# #         img = cv2.imread(os.path.join("uploads", file))

# #         img_faces = app.get(img)

# #         if len(img_faces) == 0:
# #             continue

# #         for face in img_faces:

# #             similarity = np.dot(
# #                 selfie_embedding,
# #                 face.embedding
# #             ) / (
# #                 np.linalg.norm(selfie_embedding)
# #                 * np.linalg.norm(face.embedding)
# #             )

# #             if similarity > 0.55:
# #                 matched.append(file)
# #                 break

# # print("Matched Photos:")
# # print(matched)
# # selfie = cv2.imread("selfies/selfie.jpg")

# # print(selfie)
# # import cv2
# # import insightface

# # # AI model
# # app = insightface.app.FaceAnalysis()
# # app.prepare(ctx_id=-1)

# # # Load selfie
# # img = cv2.imread("C:\Users\Reshma\OneDrive\Desktop\AI_event\uploads\selfies\selfies\selfie.jpg")

# # if img is None:
# #     print("❌ Selfie image not found.")
# #     exit()

# # faces = app.get(img)

# # print("Faces detected:", len(faces))

# # if len(faces) > 0:
# #     print("✅ Face detected successfully!")
# # else:
# #     print("❌ No face detected in selfie.")
# # import cv2
# # import insightface

# # app = insightface.app.FaceAnalysis()
# # app.prepare(ctx_id=-1)

# # img = cv2.imread("selfies/selfie.jpg")

# # if img is None:
# #     print("Selfie image not found.")
# #     exit()

# # faces = app.get(img)

# # print("Faces detected:", len(faces))

# # if len(faces) > 0:
# #     print("Face detected successfully!")
# # else:
# #     print("No face detected in selfie.")
# #     import os

# # print("Current Folder:", os.getcwd())
# # print("Files in selfies folder:")

# # if os.path.exists("selfies"):
# #     print(os.listdir("selfies"))
# # else:
# #     print("selfies folder not found")

# # import os

# # print(os.getcwd())
# # print(os.path.exists("pro.jpg"))
# # import os

# # print(os.listdir("."))
# # print(os.listdir("selfies"))

# # import cv2
# # import insightface

# # app = insightface.app.FaceAnalysis(name="buffalo_l")
# # app.prepare(ctx_id=-1)

# # img = cv2.imread("pro.JPG")

# # faces = app.get(img)

# # print("Faces detected:", len(faces))


# # import cv2
# # import os
# # import insightface

# # image_path = "rr.jpeg"

# # print("File exists:", os.path.exists(image_path))

# # img = cv2.imread(image_path)

# # print("Image:", img)

# # if img is None:
# #     print("Image could not be loaded")
# #     exit()

# # app = insightface.app.FaceAnalysis(name="buffalo_l")
# # app.prepare(ctx_id=-1)

# # faces = app.get(img)

# # print("Faces detected:", len(faces))

# # import os

# # print(os.getcwd())
# # print(os.listdir("selfies"))
# import cv2

# # img = cv2.imread("rr.jpeg")   # మీ file పేరు ఏదైతే os.listdir లో కనిపించిందో అదే పెట్టండి
# # print(img is None)

# # import os
# # print(os.listdir("selfies"))
# # import os

# # files = os.listdir("selfies")
# # print(files)

# # import cv2

# # img = cv2.imread(os.path.join("selfies", files[0]))

# # if img is None:
# #     print("Cannot load:", files[0])
# # else:
# #     print("Loaded:", files[0])
# # import os
# # import cv2
# # import numpy as np
# # from insightface.app import FaceAnalysis

# # app = FaceAnalysis(name="buffalo_l")
# # app.prepare(ctx_id=-1)

# # # Load selfie
# # selfie = cv2.imread("selfies","rr.jpeg")
# # selfie_faces = app.get(selfie)

# # if len(selfie_faces) == 0:
# #     print("No face found in selfie")
# #     exit()

# # selfie_embedding = selfie_faces[0].embedding

# # print("Checking uploaded photos...\n")

# # for file in os.listdir("uploads"):
# #     if file.lower().endswith((".jpg", ".jpeg", ".png")):

# #         img = cv2.imread(os.path.join("uploads", file))
# #         faces = app.get(img)

# #         if len(faces) == 0:
# #             continue

# #         for face in faces:
# #             similarity = np.dot(selfie_embedding, face.embedding) / (
# #                 np.linalg.norm(selfie_embedding) * np.linalg.norm(face.embedding)
# #             )

# #             if similarity > 0.55:
# #                 print("MATCH FOUND:", file)
# #                 break
# import os
# import cv2

# files = os.listdir("selfies")
# print("Files:", files)

# image_path = os.path.join("selfies", files[0])
# print("Loading:", image_path)

# img = cv2.imread(image_path)

# if img is None:
#     print("Failed to load image")
# else:
#     print("Image loaded successfully")
#     print(img.shape)
# image_path = os.path.join("selfies", "rr.jpeg")

# selfie = cv2.imread(image_path)

# from insightface.app import FaceAnalysis
# image_path = os.path.join("selfies", "rr.jpeg")

# selfie = cv2.imread(image_path)

# print(type(selfie))
# print(selfie.shape)

# app = FaceAnalysis(name="buffalo_l")
# app.prepare(ctx_id=-1)

# selfie_faces = app.get(selfie)
# print("Faces detected:", len(selfie_faces))

# if len(selfie_faces) == 0:
#     print("No face found")
#     exit()

# print("Face detected successfully!")

# selfie_embedding = selfie_faces[0].embedding

# import numpy as np
# import os

# print("\nChecking uploaded photos...")

# for file in os.listdir("uploads"):
#     if file.lower().endswith((".jpg", ".jpeg", ".png")):

#         img = cv2.imread(os.path.join("uploads", file))

#         if img is None:
#             continue

#         faces = app.get(img)

#         if len(faces) == 0:
#             continue

#         for face in faces:
#             similarity = np.dot(selfie_embedding, face.embedding) / (
#                 np.linalg.norm(selfie_embedding) * np.linalg.norm(face.embedding)
#             )

#             print(file, "Similarity:", round(similarity, 2))

#             if similarity > 0.50:
#                 print("✅ MATCH FOUND:", file)
#                 break

import os
import cv2
import numpy as np
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

matched_photos = []
print("Checking uploaded photos...\n")

for file in os.listdir("uploads"):

    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join("uploads", file)
    img = cv2.imread(img_path)

    if img is None:
        continue

    faces = app.get(img)

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

        print(file, "Similarity:", round(similarity, 2))

        if similarity >= 0.50:
            matched_photos.append(file)
            print("MATCH FOUND:", file)
            break

print("\nMatched Photos:")

if len(matched_photos) == 0:
    print("No matching photos found.")
else:
    for photo in matched_photos:
        print(photo)
with open("matched.txt", "w") as f:
    for photo in matched_photos:
        f.write(photo + "\n")