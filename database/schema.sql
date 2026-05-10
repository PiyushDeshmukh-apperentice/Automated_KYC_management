CREATE TABLE workflow_sessions (
    session_id UUID PRIMARY KEY,
    customer_id TEXT,
    customer_name TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE TABLE raw_customer_data (
    id SERIAL PRIMARY KEY,
    session_id UUID,
    source TEXT,
    document_type TEXT,
    raw_payload JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE agent_messages (
    id SERIAL PRIMARY KEY,
    session_id UUID,
    sender TEXT,
    receiver TEXT,
    message JSONB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE workflow_state (
    session_id UUID PRIMARY KEY,
    current_agent TEXT,
    current_round INTEGER,
    paused BOOLEAN DEFAULT FALSE,
    unresolved_issues JSONB
);