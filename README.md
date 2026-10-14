# BookBuddy-RAG
BookBuddy AI is a RAG-based book assistant built with Python, LangChain, BeautifulSoup, Sentence Transformers, ChromaDB, and Groq. It scrapes book details, retrieves relevant information using vector search, and generates answers about book titles, prices, ratings, and availability.
# BookBuddy AI — RAG-Based Book Assistant

## Overview
BookBuddy AI is a Retrieval-Augmented Generation (RAG) project that answers questions using book information scraped from Books to Scrape.

## Features
- Scrapes book titles, prices, ratings, and availability.
- Converts book information into documents.
- Generates embeddings using Sentence Transformers.
- Stores and retrieves documents using ChromaDB.
- Uses a Groq-hosted language model to generate answers from retrieved context.

## Tech Stack
- Python
- BeautifulSoup
- LangChain
- Sentence Transformers
- ChromaDB
- Groq API
- Google Colab

## RAG Workflow
Website Scraping → Document Creation → Embeddings → ChromaDB → Retrieval → LLM Response

## How to Run
1. Open `BookBuddy_RAG.ipynb` in Google Colab.
2. Install the required dependencies.
3. Add your Groq API key to Colab Secrets using the name `groq`.
4. Run the notebook cells in order.
5. Ask questions about the retrieved book information.

## Data Source
[Books to Scrape](https://books.toscrape.com/)

## Security
Never commit API keys or other credentials to GitHub.

## Disclaimer
This is an educational project demonstrating a basic RAG workflow. Answers are limited by the scraped data and the documents retrieved.
