from fastapi import FastAPI, HTTPException
import os

from utils import read_xml, read_json, DATASET_PATH

app = FastAPI(
    title="Mock DigiLocker Service"
)


# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/")
def health():

    return {
        "service": "Mock DigiLocker",
        "status": "running"
    }


# =====================================================
# AADHAAR
# =====================================================

@app.get("/aadhaar/{customer}")
def get_aadhaar(customer: str):

    path = os.path.join(
        DATASET_PATH,
        customer,
        "identity_xml",
        "aadhaar.xml"
    )

    if not os.path.exists(path):

        raise HTTPException(
            status_code=404,
            detail="Aadhaar not found"
        )

    return {
        "document_type": "aadhaar",
        "customer": customer,
        "data": read_xml(path)
    }


# =====================================================
# PAN
# =====================================================

@app.get("/pan/{customer}")
def get_pan(customer: str):

    path = os.path.join(
        DATASET_PATH,
        customer,
        "identity_xml",
        "pan.xml"
    )

    if not os.path.exists(path):

        raise HTTPException(
            status_code=404,
            detail="PAN not found"
        )

    return {
        "document_type": "pan",
        "customer": customer,
        "data": read_xml(path)
    }


# =====================================================
# DRIVING LICENSE
# =====================================================

@app.get("/driving-license/{customer}")
def get_dl(customer: str):

    path = os.path.join(
        DATASET_PATH,
        customer,
        "identity_xml",
        "driving_license.xml"
    )

    if not os.path.exists(path):

        raise HTTPException(
            status_code=404,
            detail="Driving License not found"
        )

    return {
        "document_type": "driving_license",
        "customer": customer,
        "data": read_xml(path)
    }


# =====================================================
# PASSPORT
# =====================================================

@app.get("/passport/{customer}")
def get_passport(customer: str):

    path = os.path.join(
        DATASET_PATH,
        customer,
        "identity_json",
        "passport.json"
    )

    if not os.path.exists(path):

        return {
            "document_type": "passport",
            "customer": customer,
            "available": False,
            "message": "Passport not available"
        }

    return {
        "document_type": "passport",
        "customer": customer,
        "available": True,
        "data": read_json(path)
    }