# Advice-IREX

A FastAPI application for extracting remittance advice data from PDF files.

## Features

- Upload PDF remittance files
- Extract structured data using PDF parsing
- Return CSV format response
- RESTful API interface

## Deployment on Render

### Method 1: Using render.yaml (Recommended)

1. Connect your GitHub repository to Render
2. Render will automatically detect the `render.yaml` file
3. The service will be deployed automatically

### Method 2: Manual Deployment

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## API Endpoints

- `POST /upload-pdf/` - Upload a PDF file and get structured CSV response
- `GET /docs` - Interactive API documentation (Swagger UI)

## Dependencies

All dependencies are frozen in `requirements.txt` including:
- FastAPI
- python-multipart (for file uploads)
- pdfplumber
- uvicorn

## Local Development

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` for the interactive API documentation. 