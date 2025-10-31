import vertexai
from vertexai.generative_models import GenerativeModel
import PyPDF2
import functions_framework
from flask import make_response

# Initialize Vertex AI
vertexai.init(project="bamboo-theorem-2000", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")

# Load PDF
def load_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

pdf_text = load_pdf("AI_Prompt_Engineer_Role.pdf")

# RAG API with CORS
@functions_framework.http
def rag_api(request):
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Handle POST request
    data = request.get_json(silent=True) or {}
    question = data.get("question", "What does a Prompt Engineer do?")
    prompt = f"Document: {pdf_text}\nQuestion: {question}\nAnswer (short):"
    response = model.generate_content(prompt)

    # Return with CORS headers
    result = {"answer": response.text}
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return (result, 200, headers)