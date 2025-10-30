# Day 1: Project Setup & GitHub

## Goal
Initialize repository and folder structure.

## Tasks
- Created `bamboo-theorem` repo on GitHub
- Set up local folder: `~/Desktop/bamboo-theorem`
- Added `.gitignore`
- First commit: `day1: Project initialized`

# Day 2: Python + PDF Parsing

## Goal
Read and extract text from PDF using Python.

## Code
```python
!pip install PyPDF2
import PyPDF2

def read_pdf(path):
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

```

# Day 3: Prompt Engineering

## Goal
Craft effective prompts for LLMs.

## Best Practices
- Be specific
- Use examples
- Chain reasoning
- Role-play: "You are a senior AI engineer..."

## Example Prompt
```text
You are an AI Prompt Engineer. Given this job description, answer in 3 bullet points:
"{pdf_text}"
Answer: {answer}

```
# Day 4: Gemini API Test

## Goal
Call Gemini model via API.

## Code (Colab)
```python
!pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Explain RAG in 1 sentence.")
print(response.text)

```
# Day 5: Vertex AI + Gemini 2.0 Flash

## Goal
Use **Gemini 2.0 Flash** on **Vertex AI** with service account.

## Setup
- Enabled Vertex AI API
- Created service account → `gemini-key.json`
- Tested in Colab

## Test Code
```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="bamboo-theorem-2000", location="us-central1")
model = GenerativeModel("gemini-2.0-flash")
response = model.generate_content("What is a Prompt Engineer?")
print(response.text)

```
# Day 6: RAG API on Cloud Run Functions

**Live URL:** https://rag-api-116522765677-us-central1.run.app

## What It Does
- Loads `AI_Prompt_Engineer_Role.pdf`
- Answers questions using **RAG + Gemini 2.0 Flash**
- Deployed on **Google Cloud Run**

## Test API
```bash
curl -X POST https://rag-api-116522765677-us-central1.run.app \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the main tasks of an AI Prompt Engineer?"}'