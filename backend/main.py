from fastapi import FastAPI
from fastapi import UploadFile, File
from parser import extract_text_from_bytes
from ai_engine import analyze_requirement_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local testing; later restrict to ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status":"ok"}


@app.post("/api/requirements/upload")
async def upload_requirement(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}")
    content = await file.read()
    text = extract_text_from_bytes(content, filename=file.filename)
    analysis = analyze_requirement_text(text)
    return {"filename": file.filename, "analysis": analysis}
    


