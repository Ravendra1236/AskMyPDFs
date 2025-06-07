from fastapi import FastAPI , UploadFile , HTTPException
from pydantic_models import QueryInput , QueryResponse , DocumentInfo , DeleteFileRequest
from langchain_utils import get_rag_chain
from db_utils import insert_application_logs , get_chat_history , get_all_documents,
insert_document_record , delete_document_record 
from chroma_utils import index_document_to_chroma , delete_doc_from_chroma
import os 
import uuid 
import logging 
logging.basicConfig(filename='app.log' level=logging.INFO)
app = FastAPI()

@app.post("/chat" , response_model=QueryResponse)
def chat(query_input: QueryInput):
    session_id = query_input.session_id
    logging.info(f"Session ID: {session_id} , User Query: {query_input.question} , Model: {query_input.model.value}")
    if not session_id:
        session_id = str(uuid.uuid4())
        

        