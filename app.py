# import streamlit as st
# import os
# import qrcode

# st.set_page_config(page_title="AI Event Photo Finder", page_icon="📸")

# st.title("📸 AI Event Photo Finder")

# event_name = st.text_input("Enter Event Name")

# uploaded_files = st.file_uploader(
#     "Upload Event Photos",
#     type=["jpg", "jpeg", "png"],
#     accept_multiple_files=True
# )

# if st.button("Upload"):
#     if event_name == "":
#         st.error("Please enter event name")
#     elif not uploaded_files:
#         st.error("Please upload photos")
#     else:
#         os.makedirs("uploads", exist_ok=True)

#         for file in uploaded_files:
#             with open(os.path.join("uploads", file.name), "wb") as f:
#                 f.write(file.getbuffer())

#         st.success("Photos Uploaded Successfully!")

# if st.button("Generate QR Code"):
#     os.makedirs("qrcodes", exist_ok=True)

#     url = f"http://localhost:8501/?event={event_name}"

#     img = qrcode.make(url)

#     qr_path = f"qrcodes/{event_name}.png"

#     img.save(qr_path)

#     st.success("QR Code Generated Successfully!")

#     st.image(qr_path, caption="Event QR Code")

# import streamlit as st
# import os
# import qrcode

# st.set_page_config(page_title="AI Event Photo Finder", page_icon="📸")

# st.title("📸 AI Event Photo Finder")

# event_name = st.text_input("Enter Event Name")

# uploaded_files = st.file_uploader(
#     "Upload Event Photos",
#     type=["jpg", "jpeg", "png"],
#     accept_multiple_files=True
# )

# if st.button("Upload"):
#     if event_name == "":
#         st.error("Please enter event name")
#     elif not uploaded_files:
#         st.error("Please upload photos")
#     else:
#         os.makedirs("uploads", exist_ok=True)

#         for file in uploaded_files:
#             with open(os.path.join("uploads", file.name), "wb") as f:
#                 f.write(file.getbuffer())

#         st.success("Photos Uploaded Successfully!")

# if st.button("Generate QR Code"):
#     os.makedirs("qrcodes", exist_ok=True)

#     url = f"http://localhost:8501/?event={event_name}"

#     img = qrcode.make(url)

#     qr_path = f"qrcodes/{event_name}.png"

#     img.save(qr_path)

#     st.success("QR Code Generated Successfully!")

#     st.image(qr_path, caption="Event QR Code")
#     # Guest Selfie Upload

# st.header("🤳 Guest Selfie Upload")

# selfie = st.file_uploader(
#     "Upload Your Selfie",
#     type=["jpg", "jpeg", "png"],
#     key="selfie"
# )

# if selfie is not None:
#     os.makedirs("selfies", exist_ok=True)

#     with open(os.path.join("selfies", selfie.name), "wb") as f:
#         f.write(selfie.getbuffer())

#     st.success("Selfie Uploaded Successfully!")
#     st.image(selfie, caption="Uploaded Selfie")
#     import subprocess

# if st.button("Find My Photos"):
#     result = subprocess.run(
#         ["python", "face_match.py"],
#         capture_output=True,
#         text=True
#     )

#     st.text(result.stdout)


import streamlit as st
import os
import qrcode
import subprocess

st.set_page_config(page_title="AI Event Photo Finder", page_icon="📸")

st.title("📸 AI Event Photo Finder")

# Event Name
event_name = st.text_input("Enter Event Name")

# Upload Event Photos
uploaded_files = st.file_uploader(
    "Upload Event Photos",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# Upload Button
if st.button("Upload"):
    if event_name == "":
        st.error("Please enter event name")
    elif not uploaded_files:
        st.error("Please upload photos")
    else:
        os.makedirs("uploads", exist_ok=True)

        for file in uploaded_files:
            with open(os.path.join("uploads", file.name), "wb") as f:
                f.write(file.getbuffer())

        st.success("Photos Uploaded Successfully!")

# QR Code
if st.button("Generate QR Code"):
    os.makedirs("qrcodes", exist_ok=True)

    url = f"http://localhost:8501/?event={event_name}"

    img = qrcode.make(url)

    qr_path = os.path.join("qrcodes", f"{event_name}.png")

    img.save(qr_path)

    st.success("QR Code Generated Successfully!")
    st.image(qr_path)

# Guest Selfie
st.header("🤳 Guest Selfie Upload")

selfie = st.file_uploader(
    "Upload Your Selfie",
    type=["jpg", "jpeg", "png"],
    key="selfie"
)

if selfie is not None:
    os.makedirs("selfies", exist_ok=True)

    selfie_path = os.path.join("selfies", selfie.name)

    with open(selfie_path, "wb") as f:
        f.write(selfie.getbuffer())

    st.success("Selfie Uploaded Successfully!")
    st.image(selfie)

# Find My Photos
# Find My Photos
if st.button("Find My Photos"):

    result = subprocess.run(
        ["python", "face_match.py"],
        capture_output=True,
        text=True
    )

    st.text(result.stdout)

    if os.path.exists("matched.txt"):

        with open("matched.txt", "r") as f:
            photos = f.read().splitlines()

        if len(photos) > 0:

            st.success("Matched Photos")

            for photo in photos:

                image_path = os.path.join("uploads", photo)

                if os.path.exists(image_path):

                    st.image(image_path, caption=photo)

                    with open(image_path, "rb") as img:

                        st.download_button(
                            label="Download " + photo,
                            data=img,
                            file_name=photo,
                            mime="image/jpeg"
                        )

        else:
            st.warning("No matching photos found.")