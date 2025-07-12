# 🩺 Medical Report Summarizer

This project is a FastAPI-based healthcare assistant that allows users to upload medical report **images** (JPG/PNG), performs **OCR** using Tesseract, and uses **Groq LLaMA 3** to generate:

- ✅ Layman-friendly medical summaries  
- ✅ Health status interpretation (Normal, Minor Issue, Critical)  
- ✅ Basic health recommendations  

---

## 📁 Project Structure

medical-report-summarizer/
├── main.py # FastAPI server
├── helper.py # OCR + AI summary logic
├── templates/
│ └── index.html # Upload form + output
├── static/
│ └── style.css # Frontend styling
├── .env # Groq API key
├── requirements.txt # Dependencies

---

## 🚀 Features

- 🖼️ Upload `.jpg` or `.png` medical reports
- 🧠 Automatic OCR using Tesseract
- 🤖 AI summarization with LLaMA 3 via [Groq API](https://console.groq.com)
- 💬 Easy-to-understand summaries for patients
- 🎨 Clean web interface with result highlighting

---

## ⚙️ Setup Instructions

1. Install Dependencies
pip install -r requirements.txt

2. Install Tesseract OCR
🔗 Tesseract Download
Install it to D:\Tesseract-OCR\ or update the path in helper.py
Add this path to your System Environment Variable > PATH
Verify:
tesseract --version

3. Create .env File
GROQ_API_KEY=your_groq_api_key_here
You can get your Groq API key from https://console.groq.com


---

🧪 Run the App
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/

---

🛠 Troubleshooting
1. ❌ Blank OCR output	Ensure Tesseract is correctly installed and image is readable
2. ❌ API error	Check your .env and verify Groq API key
3. ❌ HTML shows <b> tags	Use `{{ result
4. ❌ Tesseract not found	Update pytesseract.pytesseract_cmd or add to PATH

---

🧠 Tech Stack
1. FastAPI
2. Pytesseract
3. Groq LLaMA-3
4. Jinja2 Templates
5. HTML/CSS

---


![alt text](<Screenshot 2025-07-04 193852.png>)