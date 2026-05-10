from fastapi import FastAPI, HTTPException
import base64
import json
import mimetypes
import os


app = FastAPI()


DATASET_PATH = r"D:\Projects\TCS\datasets"


# =====================================================
# ROOT
# =====================================================

@app.get("/")
def health():

    return {
        "service": "customer_profile_service",
        "status": "running"
    }


# =====================================================
# PROFILE RETRIEVAL
# =====================================================

def _find_image_file(folder_path: str):
    supported_ext = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
    for entry in os.listdir(folder_path):
        _, ext = os.path.splitext(entry)
        if ext.lower() in supported_ext:
            return os.path.join(folder_path, entry)
    return None


@app.get("/profile/{customer_name}")
def get_profile(customer_name: str):

    customer_folder = os.path.join(
        DATASET_PATH,
        customer_name
    )

    profile_path = os.path.join(
        customer_folder,
        "profile.json"
    )

    if not os.path.exists(profile_path):

        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    with open(profile_path, "r", encoding="utf-8") as f:

        profile = json.load(f)

    image_path = _find_image_file(customer_folder)
    image_data = None
    if image_path:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
        mime_type, _ = mimetypes.guess_type(image_path)
        image_data = {
            "filename": os.path.basename(image_path),
            "mime_type": mime_type or "application/octet-stream",
            "data_base64": encoded
        }

    response = {
        "document_type": "profile",
        "customer": customer_name,
        "data": profile
    }

    if image_data:
        response["image"] = image_data

    return response
