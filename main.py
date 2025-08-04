import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Advice-IREX'))

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from models import RemittanceAdvice
from parse_pdf import extract_data_from_pdf
import pdfplumber
import io
import csv
import json

app = FastAPI(
    title="Remittance Extractor API",
    description="Upload remittance PDF and get structured JSON response.",
    version="1.0.0"
)


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Open PDF file using pdfplumber
    with pdfplumber.open(file.file) as pdf:
        parsed_data = extract_data_from_pdf(pdf)

    # Validate and parse data with Pydantic model
    data = RemittanceAdvice(**parsed_data)

    # Convert to JSON
    json_data = {
        "remittance_info": data.remittance.model_dump(),
        "currency_conversion": data.conversion.model_dump(),
        "charge1_comm_on_fgn_tt": data.charge1.model_dump(),
        "charge2_gst_on_forex": data.charge2.model_dump(),
        "debit_transaction": data.debit.model_dump(),
        "credit_transaction": data.credit.model_dump(),
        "gst_details": data.gst.model_dump()
    }

    # Create JSON string
    json_string = json.dumps(json_data, indent=2, ensure_ascii=False)
    
    # Create in-memory JSON file
    json_stream = io.StringIO(json_string)
    json_stream.seek(0)

    return StreamingResponse(
        json_stream,
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=remittance_data.json"}
    )


@app.post("/upload-pdf-json/")
async def upload_pdf_json(file: UploadFile = File(...)):
    # Open PDF file using pdfplumber
    with pdfplumber.open(file.file) as pdf:
        parsed_data = extract_data_from_pdf(pdf)

    # Validate and parse data with Pydantic model
    data = RemittanceAdvice(**parsed_data)

    # Convert to JSON
    json_data = {
        "remittance_info": data.remittance.model_dump(),
        "currency_conversion": data.conversion.model_dump(),
        "charge1_comm_on_fgn_tt": data.charge1.model_dump(),
        "charge2_gst_on_forex": data.charge2.model_dump(),
        "debit_transaction": data.debit.model_dump(),
        "credit_transaction": data.credit.model_dump(),
        "gst_details": data.gst.model_dump()
    }

    return JSONResponse(content=json_data)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 