from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, JSONB
from db import Base
import uuid

class WorkflowSession(Base):

    __tablename__ = "workflow_sessions"

    session_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id = Column(String)
    customer_name = Column(String)
    status = Column(String)


class RawCustomerData(Base):

    __tablename__ = "raw_customer_data"

    id = Column(Integer, primary_key=True)

    session_id = Column(UUID(as_uuid=True))

    source = Column(String)

    document_type = Column(String)

    raw_payload = Column(JSONB)


class AgentMessage(Base):

    __tablename__ = "agent_messages"

    id = Column(Integer, primary_key=True)

    session_id = Column(UUID(as_uuid=True))

    sender = Column(String)

    receiver = Column(String)

    message = Column(JSONB)


class WorkflowState(Base):

    __tablename__ = "workflow_state"

    session_id = Column(
        UUID(as_uuid=True),
        primary_key=True
    )

    current_agent = Column(String)

    current_round = Column(Integer)

    paused = Column(Boolean)

    unresolved_issues = Column(JSONB)