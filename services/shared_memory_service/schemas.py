from pydantic import BaseModel
from typing import Dict, Any

class CreateSession(BaseModel):

    customer_id: str

    customer_name: str


class StoreRawData(BaseModel):

    session_id: str

    source: str

    document_type: str

    raw_payload: Dict[str, Any]


class AgentMessageSchema(BaseModel):

    session_id: str

    sender: str

    receiver: str

    message: Dict[str, Any]