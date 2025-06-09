# AskMyPDFs - RAG-based Document QA System

A backend REST API service that allows users to upload documents (PDF, DOCX, HTML) and ask questions about their content using RAG (Retrieval Augmented Generation) with Google's Gemini Pro model.

## 🚀 Features

### Backend (FastAPI)
- Document Management (Upload, List, Delete)
- RAG-based Question Answering
- Session Management
- Vector Storage with ChromaDB
- SQLite Database for Persistence

### Frontend (Streamlit)
- Interactive Chat Interface
- Document Upload and Management
- Real-time Response Generation
- Session History
- Model Selection
- Document List View

## 🛠️ Technology Stack

### Backend
- FastAPI
- LangChain
- Google Gemini Pro
- ChromaDB
- SQLite
- Python 3.10+

### Frontend
- Streamlit
- Python Requests
- Markdown Support
- Session State Management

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
GOOGLE_API_KEY=""
OPENAI_API_KEY=""
ANTHROPIC_API_KEY=""
GOOGLE_API_KEY=""
HUGGINGFACEHUB_API_TOKEN=""
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=""
LANGSMITH_API_KEY=""
LANGSMITH_PROJECT=""
PORT=8000

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

The API will be available at: http://localhost:8000 or https://askmypdfs.onrender.com/

## 📚 API Endpoints

- `POST /chat`: Ask questions about uploaded documents
- `POST /upload-doc`: Upload a new document
- `GET /list-docs`: List all uploaded documents
- `POST /delete-doc`: Delete a document

# AskMyPDFs - RAG-based Document QA System

A full-stack application that enables users to chat with their documents using RAG (Retrieval Augmented Generation) and Google's Gemini Pro model.

## 🏗️ Project Structure

```
AskMyPDFs/
├── api/                    # Backend FastAPI Application
│   ├── main.py            # FastAPI application entry
│   ├── db_utils.py        # Database utilities
│   ├── chroma_utils.py    # Vector store utilities
│   ├── langchain_utils.py # LangChain RAG implementation
│   ├── pydantic_models.py # Data models
│   └── requirements.txt   # Backend dependencies
│
├── app/                    # Frontend Streamlit Application
│   ├── streamlit_app.py   # Main Streamlit application
│   ├── api_utils.py       # API connection utilities
│   ├── chat_interface.py  # Chat UI implementation
│   ├── sidebar.py         # Sidebar UI implementation
│   └── requirements.txt   # Frontend dependencies
│
└── README.md              # Project documentation
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

