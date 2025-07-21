# 🧾 Receipt Analyzer

A full-stack mini-application to upload and analyze receipts using OCR (Tesseract). Built with FastAPI (backend) and Streamlit (frontend), it extracts item names, prices, totals, and supports corrections, exports, and multi-language/multi-currency processing.


## 🚀 Features

- 📤 Upload receipt/bill images (JPG, PNG, BMP)
- 🔍 Extract items and prices via OCR
- 🖊 Manually correct extracted text
- 💾 Export as `.csv` or `.json`
- 💱 Multi-currency support (₹, $, €, etc.)
- 🌐 Multi-language receipt handling (using Tesseract)


## 🛠 Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI
- **OCR Engine:** Tesseract
- **Languages:** Python


## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/receipt-analyzer.git
cd receipt-analyzer

2. Start Backend
bash
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
3. Start Frontend (Streamlit)
In a new terminal:

bash
Copy
Edit
cd frontend
pip install -r requirements.txt
streamlit run app.py
Make sure Tesseract is installed and added to your system PATH.

