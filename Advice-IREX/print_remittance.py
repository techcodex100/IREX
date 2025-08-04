from tabulate import tabulate
from models import RemittanceAdvice, RemittanceInfo, CurrencyConversion, ChargeDetails, TransactionDetails, GSTDetails

# Same sample_data as before...
sample_data = RemittanceAdvice(
    remittance=RemittanceInfo(
        bill_no="0500IREX21119221 - CRE001",
        remitting_bank_ref_no="T47LCIC223767",
        remitter_bank="Chase Manhatan, Singapore",
        value_date="02/09/2021",
        amount_received=93960.00,
        remitter_name="ALLIANCE DIVINE IMPEX PTE LTD",
        purpose="Advance receipts against export contracts"
    ),
    conversion=CurrencyConversion(
        from_currency="SGD",
        from_amount=93960.00,
        rate=54.29,
        to_currency="INR",
        to_amount=5101088.00
    ),
    charge1=ChargeDetails(
        title="COMM ON FGN TT",
        currency="INR",
        amount=200.00,
        gst_amount=36.00
    ),
    charge2=ChargeDetails(
        title="GST on Forex Conversion",
        currency="INR",
        amount=1728.20,
        gst_amount=0.00
    ),
    debit=TransactionDetails(
        account_number="31740200000041",
        transaction_type="Dr",
        amount=1964.20,
        amount_in_words="One Thousand Nine Hundred and Sixty Four Indian Rupee and Twenty Paisa"
    ),
    credit=TransactionDetails(
        account_number="31740200000041",
        transaction_type="Cr",
        amount=5101088.00,
        amount_in_words="Five Million One Hundred and One Thousand and Eighty Eight Indian Rupee"
    ),
    gst=GSTDetails(
        bank_gstn="23AAACB1534F2ZD",
        customer_gstn="23AAWFS9154K1ZE"
    )
)

# Format each section as a table
from tabulate import tabulate

print("\n🔷 REMITTANCE INFO")
print(tabulate(sample_data.remittance.model_dump().items(), tablefmt="grid"))

print("\n🔷 CURRENCY CONVERSION")
print(tabulate(sample_data.conversion.model_dump().items(), tablefmt="grid"))

print("\n🔷 CHARGE 1")
print(tabulate(sample_data.charge1.model_dump().items(), tablefmt="grid"))

print("\n🔷 CHARGE 2")
print(tabulate(sample_data.charge2.model_dump().items(), tablefmt="grid"))

print("\n🔷 DEBIT TRANSACTION")
print(tabulate(sample_data.debit.model_dump().items(), tablefmt="grid"))

print("\n🔷 CREDIT TRANSACTION")
print(tabulate(sample_data.credit.model_dump().items(), tablefmt="grid"))

print("\n🔷 GST INFO")
print(tabulate(sample_data.gst.model_dump().items(), tablefmt="grid"))
