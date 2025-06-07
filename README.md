# AskMyPDFs - RAG-based Document QA System

A backend REST API service that allows users to upload documents (PDF, DOCX, HTML) and ask questions about their content using RAG (Retrieval Augmented Generation) with Google's Gemini Pro model.

## 🚀 Features

- Document Management:
  - Upload PDF, DOCX, and HTML files
  - List uploaded documents
  - Delete documents
- Question Answering:
  - RAG-based answers using document context
  - Chat history support
  - Session management
- Vector Storage:
  - Chroma DB for document embeddings
  - Google's Embedding model for vectorization
- Database:
  - SQLite for document and chat history storage
  - Persistent vector storage

## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Language Models**: 
  - Google Gemini Pro (Chat)
  - Google Embedding Model (Document Vectorization)
- **Vector Database**: ChromaDB
- **Document Processing**:
  - langchain-community (Document Loaders)
  - RecursiveCharacterTextSplitter
- **Database**: SQLite
- **API Documentation**: FastAPI Swagger/OpenAPI

## 📋 Requirements

```txt
# Core Dependencies
fastapi
uvicorn
python-multipart
pydantic

# LangChain Stack
langchain
langchain-core
langchain-community
langchain-google-genai

# Document Processing
docx2txt
pypdf
unstructured

# Vector Store
langchain_chroma
chromadb

# Environment Management
python-dotenv
```

## 🔧 Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AskMyPDFs
```

2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```plaintext
GOOGLE_API_KEY=your-google-api-key-here
```

5. Initialize the database:
```bash
python -m api.db_utils
```

## 🚀 Running the Application

Start the FastAPI server:
```bash
cd api
uvicorn main:app --reload
```

The API will be available at: http://localhost:8000

## 📚 API Endpoints

- `POST /chat`: Ask questions about uploaded documents
- `POST /upload-doc`: Upload a new document
- `GET /list-docs`: List all uploaded documents
- `POST /delete-doc`: Delete a document

## 🗄️ Project Structure

```
api/
├── main.py              # FastAPI application
├── db_utils.py          # Database utilities
├── chroma_utils.py      # Vector store utilities
├── langchain_utils.py   # LangChain RAG implementation
├── pydantic_models.py   # Data models
└── requirements.txt     # Project dependencies
```

## 🔄 RAG Implementation

The system uses a Retrieval Augmented Generation (RAG) approach:
1. Documents are split into chunks
2. Chunks are embedded using Google's embedding model
3. Embeddings are stored in ChromaDB
4. User questions trigger relevant document retrieval
5. Retrieved context is used by Gemini Pro to generate answers

## 🔒 Environment Variables

Required environment variables:
- `GOOGLE_API_KEY`: API key for Google Gemini Pro

