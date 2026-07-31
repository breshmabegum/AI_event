import qrcode

if st.button("Generate QR Code"):
    os.makedirs("qrcodes", exist_ok=True)

    url = f"http://localhost:8501/?event={event_name}"

    img = qrcode.make(url)
    qr_path = f"qrcodes/{event_name}.png"

    img.save(qr_path)

    st.success("QR Code Generated Successfully!")

    st.image(qr_path, caption="Event QR Code")app.py