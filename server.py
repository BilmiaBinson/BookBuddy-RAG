import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI
app = FastAPI(title="BookBuddy-RAG API")

# Enable CORS for the frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/books")
def list_books():
    # Return your scraped books or load from Chroma metadata
    # Replace this with your actual book repository
    return {
        "books": [
            {
                "title": "Sapiens: A Brief History of Humankind",
                "price": "£54.23",
                "rating": 5,
                "availability": "In stock",
                "url": "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
            }
        ]
    }

@app.post("/api/chat")
def chat(req: ChatRequest):
    try:
        # Import your existing RAG retrieval pipeline here:
        # from rag import query_rag_pipeline
        # return query_rag_pipeline(req.question)
        
        # Example response structure:
        return {
            "answer": f"Retrieved information for '{req.question}' using SentenceTransformers and ChromaDB.",
            "sources": [
                {
                    "title": "Sapiens: A Brief History of Humankind",
                    "price": "£54.23",
                    "rating": 5,
                    "availability": "In stock",
                    "url": "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.py:app", host="0.0.0.0", port=8000, reload=True)
