from fastapi import FastAPI, HTTPException
import os

from utils import read_json, DATASET_PATH

app = FastAPI(
    title="Mock Account Aggregator Service"
)


@app.get("/")
def health():

    return {
        "service": "Mock Account Aggregator",
        "status": "running"
    }


# =====================================================
# GENERIC JSON RETRIEVER
# =====================================================

def fetch_json(customer, folder, filename):

    path = os.path.join(
        DATASET_PATH,
        customer,
        folder,
        filename
    )

    if not os.path.exists(path):

        raise HTTPException(
            status_code=404,
            detail=f"{filename} not found"
        )

    return read_json(path)


# =====================================================
# BANK STATEMENT
# =====================================================

@app.get("/bank-statement/{customer}")
def bank_statement(customer: str):

    return {
        "document_type": "bank_statement",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "bank_statement.json"
        )
    }


# =====================================================
# CIBIL
# =====================================================

@app.get("/cibil/{customer}")
def cibil(customer: str):

    return {
        "document_type": "cibil",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "cibil.json"
        )
    }


# =====================================================
# EPFO
# =====================================================

@app.get("/epfo/{customer}")
def epfo(customer: str):

    return {
        "document_type": "epfo",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "epfo.json"
        )
    }


# =====================================================
# INSURANCE
# =====================================================

@app.get("/insurance/{customer}")
def insurance(customer: str):

    return {
        "document_type": "insurance",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "insurance.json"
        )
    }


# =====================================================
# MUTUAL FUNDS
# =====================================================

@app.get("/mutual-funds/{customer}")
def mutual_funds(customer: str):

    return {
        "document_type": "mutual_funds",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "mutual_funds.json"
        )
    }


# =====================================================
# SALARY SLIPS
# =====================================================

@app.get("/salary-slips/{customer}")
def salary_slips(customer: str):

    return {
        "document_type": "salary_slips",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "salary_slips.json"
        )
    }


# =====================================================
# WEALTH
# =====================================================

@app.get("/wealth/{customer}")
def wealth(customer: str):

    return {
        "document_type": "wealth",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "wealth.json"
        )
    }


# =====================================================
# LAND RECORDS
# =====================================================

@app.get("/land-records/{customer}")
def land_records(customer: str):

    return {
        "document_type": "land_records",
        "customer": customer,
        "data": fetch_json(
            customer,
            "financial_json",
            "land_records.json"
        )
    }


# =====================================================
# ITR
# =====================================================

@app.get("/itr/{customer}")
def itr(customer: str):

    return {
        "document_type": "itr",
        "customer": customer,
        "data": fetch_json(
            customer,
            "tax_json",
            "itr.json"
        )
    }


# =====================================================
# FORM16
# =====================================================

@app.get("/form16/{customer}")
def form16(customer: str):

    return {
        "document_type": "form16",
        "customer": customer,
        "data": fetch_json(
            customer,
            "tax_json",
            "form16.json"
        )
    }


# =====================================================
# FORM26AS
# =====================================================

@app.get("/form26as/{customer}")
def form26as(customer: str):

    return {
        "document_type": "form26as",
        "customer": customer,
        "data": fetch_json(
            customer,
            "tax_json",
            "form26as.json"
        )
    }


# =====================================================
# ELECTRICITY BILL
# =====================================================

@app.get("/electricity-bill/{customer}")
def electricity_bill(customer: str):

    return {
        "document_type": "electricity_bill",
        "customer": customer,
        "data": fetch_json(
            customer,
            "utility_json",
            "electricity_bill.json"
        )
    }