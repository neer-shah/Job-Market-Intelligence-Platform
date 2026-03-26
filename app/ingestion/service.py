from app.ingestion.client import AdzunaClient
from app.ingestion.parser import parse_adzuna_job
from app.db.repo import create_job, get_job_by_source_and_external_id

def ingest_job(db, keyword: str, location: str, page: int=1) -> int:
    client = AdzunaClient()
    response = client.search_jobs(keyword=keyword, location=location, page=page)
    
    results = response.get("results", [])
    created_count = 0
    
    for raw_job in results:
        parsed_job = parse_adzuna_job(raw_job)
        
        existing_job = get_job_by_source_and_external_id(
            db,
            source = parsed_job["source"],
            external_job_id = parsed_job["external_job_id"]
        )
        
        if existing_job:
            continue
        
        create_job(db, parsed_job)
        created_count += 1
    
    return created_count