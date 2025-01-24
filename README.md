# AskMyPDFs : Chat with Multiple PDFs 📝💬

AskMyPDFs is an AI-powered platform that allows users to upload multiple PDF files 📂 and ask questions based on their content. The system leverages Google's Gemini API for embeddings and chat-based interactions to provide accurate and context-aware responses.

## Features ✨
- 💽 Upload and process multiple PDF files.
- 🔍 Extract text from PDFs and split it into chunks for better retrieval.
- 💾 Store text embeddings locally using FAISS for efficient similarity searches.
- 🤖 Interact with uploaded documents using conversational AI.

## Technologies Used 🛠️
- **Streamlit** for the web interface.
- **PyPDF2** for extracting text from PDFs.
- **LangChain** for text processing and conversational AI.
- **Google Gemini API** for embedding and chat capabilities.
- **FAISS** for vector storage and similarity searches.
- **Python dotenv** for environment variable management.

## Installation and Setup 🏷️

Follow these steps to run the project locally on your PC:

### Prerequisites ✅
Ensure you have the following installed:
-  Python (>= 3.8)
-  pip (Python package manager)

### Steps 🚀

```bash
# Clone the repository
git clone https://github.com/your-repo/AskMyPDFs.git
cd AskMyPDFs

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up the API key by creating a .env file in the project root directory
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env

# Run the application
streamlit run app.py
```

### Access the application 🌐
Open your browser and go to `http://localhost:8501` to start using AskMyPDFs.

## How to Use 📝

1. **Upload PDF Files:**
   - 📂 Use the sidebar to upload one or multiple PDF files.
   - ▶️ Click the "Submit & Process" button to extract and index the text.

2. **Ask Questions:**
   - ❓ Enter your query in the text input field.
   - 💡 Receive accurate responses based on the content of uploaded PDFs.

3. **Processing Status:**
   - ⏳ The app provides real-time feedback during the processing phase.

## Project Structure 💁
```
AskMyPDFs/
│-- app.py
│-- requirements.txt
│-- .env (to be created manually)
│-- faiss_index/ (vector storage)
```

## Environment Variables 🔑

The project requires a Google API key to function. The key should be stored in a `.env` file with the following format:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Contributing 🤝
If you'd like to contribute to AskMyPDFs, feel free to fork the repository and submit a pull request with your improvements.

## License 🐜
This project is licensed under the MIT License.

---

Happy chatting with your PDFs! 😊📝
