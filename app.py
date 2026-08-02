

from PIL import Image
import io
import subprocess
import streamlit as st
import os
import qrcode
import requests
import subprocess
import cloudinary
import cloudinary.uploader
import cloudinary.api
import cloudinary_config

cloudinary.config(
    cloud_name="dr9a7in2",
    api_key="248759673993831",
    api_secret="JoxkdcbtmUUkXeUsmasR7yKXwNI"
)

st.set_page_config(page_title="AI Event Photo Finder", page_icon="📸")

st.title("📸 AI Event Photo Finder")
event = st.query_params.get("event", "")

# Event Name
if event == "":
    event_name = st.text_input("Enter Event Name")

# Upload Event Photos
if event=="":
    uploaded_files = st.file_uploader(
    "Upload Event Photos",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# Upload Button
if event=="":
    if st.button("Upload"):
        st.write("Uploaded button clicked")
        if event_name == "":
            st.error("Please enter event name")
        elif not uploaded_files:
            st.error("Please upload photos")
        else:
            uploaded_urls = []
            for file in uploaded_files:
                image = Image.open(file)
                buffer = io.BytesIO()
                image.save(
                    buffer,
                    format="JPEG",
                    quality=75,
                    optimize=True
                    )

            buffer.seek(0)
  
            result = cloudinary.uploader.upload(
                buffer,
                folder=event_name
            )
           
                

            uploaded_urls.append(result["secure_url"])

        st.session_state["uploaded_urls"] = uploaded_urls

        st.success("Photos Uploaded Successfully to Cloudinary!")
# QR Code
if event == "":
    if st.button("Generate QR Code"):
        os.makedirs("qrcodes", exist_ok=True)

        url = f"https://aievent-h73cwd74dkwumvhmlemrhu.streamlit.app/?event={event_name}"

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
    # st.image(selfie)
    
# Find My Photos
if st.button("Find My Photos"):

    result = subprocess.run(
        ["python", "face_match.py",event_name],
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
                st.image(photo, caption="Matched Photo", width=300)
                st.download_button(
                    label="Download Photo",
                    data=requests.get(photo).content,
                    file_name="matched_photo.jpg",
                    mime="image/jpeg"
                    )

        else:
            st.warning("No matching photos found.")
if "uploaded_urls" in st.session_state:

    st.subheader("Uploaded Photos")

    for url in st.session_state["uploaded_urls"]:
        st.image(url, width=250)