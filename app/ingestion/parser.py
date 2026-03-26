from datetime import datetime

def parse_adzuna_job(raw_job: dict) -> dict:
    return {
        "source": "adzuna",
        "external_job_id": str(raw_job.get("id")),
        "title": raw_job.get("title"),
        "company": (raw_job.get("company") or {}).get("display_name"),
        "location": (raw_job.get("location") or {}).get("display_name"),
        "description_snippet": raw_job.get("description"),
        "url": raw_job.get("redirect_url"),
        "posted_at": _parse_datetime(raw_job.get("created")),
        "raw_payload": raw_job
    }

def _parse_datetime(value: str | None):
    if not value:
        return None
    
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
