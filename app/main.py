from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.db.repo import get_jobs, get_job_by_id, search_jobs
from app.schemas.job import JobResponse

app = FastAPI(title="Job Market Intelligence Platform")

@app.get("/health")
def health_status():
    return {"status": "ok"}

@app.get("/jobs", response_model=list[JobResponse])
def read_jobs(limit: int=20, db: Session = Depends(get_db)):
    return get_jobs(db, limit=limit)
