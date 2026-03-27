from datetime import datetime
from pydantic import BaseModel

class JobResponse(BaseModel):
    id: int
    source: str
    external_job_id: str
    title: str
    company: str | None
    location: str | None
    description_snippet: str | None
    url: str | None
    posted_at: datetime | None
    fetched_at: datetime

    class Config:
        from_attributes = True
