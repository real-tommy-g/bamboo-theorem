# main.py – 100% FUNGUJÚCI NA CLOUD RUN (2025)

from flask import Flask, request, jsonify, make_response
import vertexai
from vertexai.generative_models import GenerativeModel
import PyPDF2

app = Flask(__name__)

# Inicializácia
vertexai.init(project="bamboo-theorem-2000", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")

# Načítanie PDF
def load_pdf():
    try:
        with open("AI_Prompt_Engineer_Role.pdf", "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        print(f"[DEBUG] PDF načítaný: {len(text)} znakov")
        return text
    except Exception as e:
        print(f"[ERROR] PDF chyba: {e}")
        return "Error: PDF not found"

pdf_text = load_pdf()

@app.route("/", methods=["GET", "POST", "OPTIONS"])
def rag_api():
    # CORS preflight
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # GET test
    if request.method == "GET":
        return jsonify({"status": "API is alive", "pdf_length": len(pdf_text)})

    # POST otázka
    data = request.get_json() or {}
    question = data.get("question", "What does a Prompt Engineer do?")
    print(f"[DEBUG] Otázka: {question}")

    prompt = f"Document: {pdf_text}\nQuestion: {question}\nAnswer in 3 bullet points:"
    response = model.generate_content(prompt)

    result = {"answer": response.text}
    resp = make_response(jsonify(result))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)