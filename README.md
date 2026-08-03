# 📸 AI Event Photo Finder

An AI-powered web application that helps guests instantly find their event photos by uploading a selfie. The system uses face recognition to compare the uploaded selfie with event photos stored in the cloud and returns only the matching images.

## 🚀 Project Overview

AI Event Photo Finder is designed for photographers and event organizers to simplify photo sharing. Instead of manually searching through hundreds of event photos, guests can simply scan a QR code, upload a selfie, and instantly receive their matching photos.

---

## ✨ Features

- 📷 Upload multiple event photos
- ☁️ Store event photos securely using Cloudinary
- 🔍 AI-based face recognition using InsightFace
- 🤳 Guest selfie upload
- 📱 QR Code based event access
- 🎯 Automatic face matching
- 🖼️ Display matched photos
- ⬇️ Download matched photos
- 🌐 Streamlit Cloud deployment

---

## 🛠️ Tech Stack

- Python
- Streamlit
- InsightFace
- OpenCV
- NumPy
- Cloudinary
- Requests
- Pillow
- QRCode

---

## 📂 Project Structure

```
AI-Event-photo-Finder/
│
├── organizer.py
├── guest.py
├── face_match.py
├── cloudinary_config.py
├── requirements.txt
├── README.md
├── selfies/
├── qrcodes/
├── matched.txt
└── uploads/
```

---

## ⚙️ Project Workflow

1. Organizer creates an event.
2. Event photos are uploaded to Cloudinary.
3. QR Code is generated for the event.
4. Guest scans the QR Code.
5. Guest uploads a selfie.
6. InsightFace extracts facial embeddings.
7. Selfie is compared with all event photos.
8. Matching photos are displayed.
9. Guest downloads the matched photos.

---

## 🧠 Challenges Faced

During the development of this project, I solved several real-world technical challenges:

- Integrated Cloudinary cloud storage with Streamlit.
- Implemented AI face recognition using InsightFace.
- Solved image loading and URL handling issues.
- Fixed Streamlit deployment issues on Streamlit Community Cloud.
- Resolved OpenCV and Python dependency errors.
- Handled QR Code event routing and URL parameters.
- Fixed duplicate Streamlit widget key errors.
- Improved face matching by tuning similarity thresholds.
- Debugged cloud image retrieval and face detection.
- Implemented automatic photo download functionality.

These challenges helped improve my debugging, deployment, and problem-solving skills.

---

## 💡 Future Improvements

- Multiple face selection
- Higher face matching accuracy
- Event gallery
- Admin dashboard
- Email photo delivery
- Faster image search
- Mobile application

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/breshmabegum/AI-Event-photo-Finder.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Organizer

```bash
streamlit run organizer.py
```

Run Guest

```bash
streamlit run guest.py


---

## 🎯 Learning Outcomes

Through this project I gained hands-on experience in:

- Artificial Intelligence
- Face Recognition
- Streamlit Deployment
- Cloud Storage Integration
- Computer Vision
- REST API Integration
- Python Debugging
- Real-world Project Development

---

## 👩‍💻 Author

**Reshma Begum**

Aspiring Data Scientist | Python Developer | AI Enthusiast

GitHub: https://github.com/breshmabegum

LinkedIn: *(https://www.linkedin.com/in/reshma-begum-2057a7290?)*

---

⭐ If you like this project, consider giving it a Star!
