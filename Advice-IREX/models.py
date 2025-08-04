from pydantic import BaseModel

class RemittanceInfo(BaseModel):
    bill_no: str
    remitting_bank_ref_no: str
    remitter_bank: str
    value_date: str
    amount_received: float
    remitter_name: str
    purpose: str

class CurrencyConversion(BaseModel):
    from_currency: str
    from_amount: float
    rate: float
    to_currency: str
    to_amount: float

class ChargeDetails(BaseModel):
    title: str
    currency: str
    amount: float
    gst_amount: float

class TransactionDetails(BaseModel):
    account_number: str
    transaction_type: str  # "Dr" or "Cr"
    amount: float
    amount_in_words: str

class GSTDetails(BaseModel):
    bank_gstn: str
    customer_gstn: str

class RemittanceAdvice(BaseModel):
    remittance: RemittanceInfo
    conversion: CurrencyConversion
    charge1: ChargeDetails
    charge2: ChargeDetails
    debit: TransactionDetails
    credit: TransactionDetails
    gst: GSTDetails
