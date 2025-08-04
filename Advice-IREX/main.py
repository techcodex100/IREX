from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from models import RemittanceAdvice
from parse_pdf import extract_data_from_pdf
import pdfplumber
import io
import csv

app = FastAPI(
    title="Remittance Extractor API",
    description="Upload remittance PDF and get structured CSV response.",
    version="1.0.0"
)


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Open PDF file using pdfplumber
    with pdfplumber.open(file.file) as pdf:
        parsed_data = extract_data_from_pdf(pdf)

    # Validate and parse data with Pydantic model
    data = RemittanceAdvice(**parsed_data)

    # Create in-memory CSV
    csv_stream = io.StringIO()
    writer = csv.writer(csv_stream)

    def write_section(section_title, section_data):
        writer.writerow([section_title])  # Write section header
        for key, value in section_data.items():
            clean_key = key.replace("_", " ").title()
            clean_value = f"{value:,.2f}" if isinstance(value, (int, float)) else value
            writer.writerow(["", clean_key, clean_value])
        writer.writerow([])  # Add empty row for spacing

    # Write all structured sections
    write_section("🔷 Remittance Info", data.remittance.model_dump())
    write_section("🔷 Currency Conversion", data.conversion.model_dump())
    write_section("🔷 Charge 1: COMM ON FGN TT", data.charge1.model_dump())
    write_section("🔷 Charge 2: GST on Forex Conversion", data.charge2.model_dump())
    write_section("🔷 Debit Transaction", data.debit.model_dump())
    write_section("🔷 Credit Transaction", data.credit.model_dump())
    write_section("🔷 GST Details", data.gst.model_dump())

    # Move cursor to beginning
    csv_stream.seek(0)

    return StreamingResponse(
        csv_stream,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=remittance_report.csv"}
    )
