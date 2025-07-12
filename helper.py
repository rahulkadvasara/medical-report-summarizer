from PIL import Image
import pytesseract
from groq import Groq
import os
from dotenv import load_dotenv
import re

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama3-70b-8192"

client = Groq(api_key=GROQ_API_KEY)

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    print("OCR TEXT:", text)
    return text

def generate_prompt(text):
    return f"""
You are a medical assistant AI. A user uploaded an image of a medical report.
Your job is to:
1. Summarize the content in simple, understandable language.
2. Detect the health status (normal, minor issue, or critical).
3. Provide recommendations if needed.

Medical Report:
{text}

Output format:
Summary: ...
Health Status: ...
Recommendations: ...
"""

def emphasize_headings(text):
    # Remove unwanted line
    if text.startswith("Here is the output:"):
        text = text.replace("Here is the output:", "").strip()

    # Normalize & style heading labels using span
    text = re.sub(r"\*\*?(Summary):\*\*?", r"<span class='heading'>📝 \1:</span>", text)
    text = re.sub(r"\*\*?(Health Status):\*\*?", r"<span class='heading'>❤️ \1:</span>", text)
    text = re.sub(r"\*\*?(Recommendations):\*\*?", r"<span class='heading'>📌 \1:</span>", text)

    # Replace newlines with <br> for HTML rendering
    return text.replace("\n", "<br>")

def summarize_text(text):
    prompt = generate_prompt(text)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    output = response.choices[0].message.content.strip()
    return emphasize_headings(output)
