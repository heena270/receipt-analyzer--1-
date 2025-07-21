from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pytesseract
from PIL import Image
import io
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_receipt(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        text = pytesseract.image_to_string(image)

        lines = text.splitlines()
        result = {}

        for line in lines:
            match = re.match(r"(.+?)\s+(\d+(\.\d{1,2})?)$", line.strip())
            if match:
                item = match.group(1).strip()
                price = match.group(2).strip()
                result[item] = price

        return result
    except Exception as e:
        return {"detail": str(e)}
