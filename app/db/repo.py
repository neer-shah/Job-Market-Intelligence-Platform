from sqlalchemy.orm import Session
from app.db.models import Job

def get_job_by_source_and_external_id(db: Session, source: str, external_job_id: str) -> Job | None: 
    return (
        db.query(Job)
        .filter(Job.source == source, Job.external_job_id == external_job_id)
        .first()
    )

def create_job(db: Session, job_data: dict) -> Job:
    job = Job(**job_data)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
