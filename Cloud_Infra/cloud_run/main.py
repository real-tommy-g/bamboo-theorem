from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel
import PyPDF2

app = Flask(__name__)

# Inicializácia Vertex AI
vertexai.init(project="bamboo-theorem-2000", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")

# Načítanie PDF
def load_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Načítanie pri štarte
pdf_text = load_pdf("AI_Prompt_Engineer_Role.pdf")
print(f"PDF načítaný: {len(pdf_text)} znakov")

# CORS hlavičky
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/', methods=['POST', 'OPTIONS'])
def rag_api():
    if request.method == 'OPTIONS':
        return '', 204

    data = request.get_json() or {}
    question = data.get("question", "What does a Prompt Engineer do?")
    prompt = f"Document: {pdf_text}\nQuestion: {question}\nAnswer (short):"
    response = model.generate_content(prompt)

    result = {"answer": response.text}
    return add_cors_headers(jsonify(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)