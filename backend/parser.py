# backend/parser.py
import tempfile, os
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def extract_text_from_bytes(b: bytes, filename: str = "uploaded"):
    ext = filename.lower().split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp:
        tmp.write(b)
        tmp.flush()
        tmp_path = tmp.name
    try:
        if ext == "pdf":
            txt = extract_pdf_text(tmp_path)
        elif ext in ("docx", "doc"):
            doc = Document(tmp_path)
            txt = "\n".join([p.text for p in doc.paragraphs])
        else:
            with open(tmp_path, "r", encoding="utf-8", errors="ignore") as f:
                txt = f.read()
    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass
    return txt
