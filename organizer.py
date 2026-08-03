

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
if st.button("Generate QR Code"):
    os.makedirs("qrcodes", exist_ok=True)

    url = f"https://aievent-mskmt4gfzymwacaryet45u.streamlit.app/?event={event_name}"
    st.write(url)

    img = qrcode.make(url)

    qr_path = os.path.join("qrcodes", f"{event_name}.png")

    img.save(qr_path)

    st.success("QR Code Generated Successfully!")
    st.image(qr_path)

