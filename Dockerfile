FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for PDF generation and networking
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port Streamlit runs on (Hugging Face uses 7860)
EXPOSE 7860

# Command to run the app
CMD ["streamlit", "run", "src/app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]
