def extract_data_from_pdf(pdf):
    # Combine all text from the PDF pages
    full_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    # You can print for debug
    # print(full_text)

    # Return dummy structured data (replace this with regex or fuzzy logic later)
    return {
        "remittance": {
            "bill_no": "0500IREX21119221 - CRE001",
            "remitting_bank_ref_no": "T47LCIC223767",
            "remitter_bank": "Chase Manhatan, Singapore",
            "value_date": "02/09/2021",
            "amount_received": 93960.00,
            "remitter_name": "ALLIANCE DIVINE IMPEX PTE LTD",
            "purpose": "Advance receipts against export contracts"
        },
        "conversion": {
            "from_currency": "SGD",
            "from_amount": 93960.00,
            "rate": 54.29,
            "to_currency": "INR",
            "to_amount": 5101088.00
        },
        "charge1": {
            "title": "COMM ON FGN TT",
            "currency": "INR",
            "amount": 200.00,
            "gst_amount": 36.00
        },
        "charge2": {
            "title": "GST on Forex Conversion",
            "currency": "INR",
            "amount": 1728.20,
            "gst_amount": 0.00
        },
        "debit": {
            "account_number": "31740200000041",
            "transaction_type": "Dr",
            "amount": 1964.20,
            "amount_in_words": "One Thousand Nine Hundred and Sixty Four Indian Rupee and Twenty Paisa"
        },
        "credit": {
            "account_number": "31740200000041",
            "transaction_type": "Cr",
            "amount": 5101088.00,
            "amount_in_words": "Five Million One Hundred and One Thousand and Eighty Eight Indian Rupee"
        },
        "gst": {
            "bank_gstn": "23AAACB1534F2ZD",
            "customer_gstn": "23AAWFS9154K1ZE"
        }
    }
