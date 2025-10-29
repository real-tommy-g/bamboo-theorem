# RAG API on Cloud Run (Gemini 2.0 Flash)

**Live URL:** https://rag-api-116522765677-us-central1.run.app

## Test API
```bash
curl -X POST https://rag-api-116522765677-us-central1.run.app \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the main tasks of an AI Prompt Engineer?"}'