import streamlit as st
import os
import subprocess
import requests
st.set_page_config(page_title="AI Event Photo Finder", page_icon="📸")

st.title("📸 AI Event Photo Finder")
event_name = st.query_params.get("event", "")

if event_name == "":
    st.error("Event not found")
    st.stop()

st.write("Event:", event_name)
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
