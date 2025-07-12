from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from helper import extract_text_from_image, summarize_text
import os

app = FastAPI()

# Mount static and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-report/")
async def upload_report(request: Request, file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    try:
        text = extract_text_from_image(temp_path)
        if not text.strip():
            result = "OCR failed. Please upload a clearer image."
        else:
            result = summarize_text(text)

    except Exception as e:
        result = f"Error: {str(e)}"

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })
