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

def get_jobs(db: Session, limit: int=20):
    return db.query(Job).limit(limit).all()

def get_job_by_id(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def search_jobs(db: Session, keyword: str | None = None, location: str | None = None):
    query = db.query(Job)

    if keyword:
        query = query.filter(Job.title.ilike(f"%{keyword}%"))
    
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))

    return query.all()
