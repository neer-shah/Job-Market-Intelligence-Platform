from sqlalchemy import Column, Integer, String, DateTime, Text, UniqueConstraint
from sqlalchemy.types import JSON
from datetime import datetime
from app.db.session import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    external_job_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    company = Column(String, nullable=True)
    location = Column(String, nullable=True)
    description_snippet = Column(Text, nullable=True)
    url = Column(String, nullable=True)
    posted_at = Column(DateTime, nullable=True)
    fetched_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    raw_payload = Column(JSON, nullable=True)

    __table_args__ = (
        UniqueConstraint("source", "external_job_id", name="uq_source_external_job_id"),
    )
