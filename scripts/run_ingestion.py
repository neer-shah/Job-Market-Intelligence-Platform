from app.db.session import SessionLocal
from app.ingestion.service import ingest_job

def main() -> None:
    db = SessionLocal()
    try:
        created_count = ingest_job(
            db=db,
            keyword="junior software engineer",
            location="London",
            page=1
        )
        print(f"Inserted {created_count} new jobs")
    finally:
        db.close()
        
if __name__ == "__main__":
    main()
