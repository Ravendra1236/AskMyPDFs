FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create directories for data persistence
RUN mkdir -p /app/data/chroma_db

# Set environment variables
ENV PYTHONPATH=/app
ENV GOOGLE_API_KEY=""
ENV DB_PATH="/app/data/rag_app.db"
ENV CHROMA_PATH="/app/data/chroma_db"

# Create volume mount points
VOLUME ["/app/data"]

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]