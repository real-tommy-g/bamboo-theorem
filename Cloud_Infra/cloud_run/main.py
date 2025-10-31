import vertexai
from vertexai.generative_models import GenerativeModel
import PyPDF2
import functions_framework
from flask import make_response, jsonify

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
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    data = request.get_json(silent=True) or {}
    question = data.get("question", "What does a Prompt Engineer do?")
    prompt = f"Document: {pdf_text}\nQuestion: {question}\nAnswer (short):"
    response = model.generate_content(prompt)

    result = {"answer": response.text}
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response