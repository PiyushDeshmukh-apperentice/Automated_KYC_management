from fastapi import FastAPI
from sqlalchemy.orm import Session
from db import SessionLocal
import models
import schemas
import uuid

app = FastAPI()

@app.post("/create-session")
def create_session(data: schemas.CreateSession):

    db: Session = SessionLocal()

    session = models.WorkflowSession(
        session_id=uuid.uuid4(),
        customer_id=data.customer_id,
        customer_name=data.customer_name,
        status="ACTIVE"
    )

    db.add(session)
    db.commit()

    return {
        "session_id": str(session.session_id),
        "status": "created"
    }


@app.post("/store-raw-data")
def store_raw_data(data: schemas.StoreRawData):

    db: Session = SessionLocal()

    raw = models.RawCustomerData(
        session_id=data.session_id,
        source=data.source,
        document_type=data.document_type,
        raw_payload=data.raw_payload
    )

    db.add(raw)
    db.commit()

    return {
        "status": "stored"
    }


@app.post("/agent-message")
def store_agent_message(data: schemas.AgentMessageSchema):

    db: Session = SessionLocal()

    msg = models.AgentMessage(
        session_id=data.session_id,
        sender=data.sender,
        receiver=data.receiver,
        message=data.message
    )

    db.add(msg)
    db.commit()

    return {
        "status": "message stored"
    }