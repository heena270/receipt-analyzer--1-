import pytesseract
from PIL import Image
import re

def process_receipt(file_path: str):
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    
    vendor = re.search(r"(?i)vendor[:\s]+(\w+)", text)
    amount = re.search(r"(?i)(total|amount)[:\s]+(\d+[.,]?\d*)", text)
    date = re.search(r"(\d{2}[/-]\d{2}[/-]\d{4})", text)

    return {
        "vendor": vendor.group(1) if vendor else "Unknown",
        "amount": float(amount.group(2)) if amount else 0.0,
        "date": date.group(1) if date else "Unknown",
    }
