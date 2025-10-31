# main.py – RAG API with CORS
import vertexai
from vertexai.generative_models import GenerativeModel
import PyPDF2
import functions_framework
from flask import make_response

vertexai.init(project="bamboo-theorem-2000", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")

def load_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

pdf_text = load_pdf("AI_Prompt_Engineer_Role.pdf")

@functions_framework.http
def rag_api(request):
    data = request.get_json(silent=True) or {}
    question = data.get("question", "What does a Prompt Engineer do?")
    prompt = f"Document: {pdf_text}\nQuestion: {question}\nAnswer (short):"
    response = model.generate_content(prompt)
    
    # CORS headers
    result = {"answer": response.text}
    resp = make_response(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    return resp