import streamlit as st
import requests

st.set_page_config(page_title="Receipt Analyzer", layout="centered")

st.title("🧾 Receipt Analyzer")
st.write("Upload a receipt image to extract item names and prices using OCR.")

uploaded_file = st.file_uploader("Upload Receipt Image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    with st.spinner("Uploading and analyzing..."):
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with open("temp.jpg", "rb") as f:
            res = requests.post("http://127.0.0.1:8000/upload", files={"file": f})
        
        if res.status_code == 200:
            data = res.json()
            st.success("✅ Extracted Items and Prices:")

            if isinstance(data, dict):
                for item, amount in data.items():
                    st.write(f"🔹 {item}: ₹{amount}")
            elif isinstance(data, list):
                for item in data:
                    st.write(f"🔹 {item[0]}: ₹{item[1]}")
            else:
                st.warning("Unexpected response format.")
        else:
            st.error(f"❌ Failed to process receipt.\n\nError: {res.json().get('detail', 'Unknown error')}")
