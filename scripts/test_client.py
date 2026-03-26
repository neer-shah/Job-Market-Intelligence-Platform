from app.ingestion.client import AdzunaClient
from app.ingestion.parser import parse_adzuna_job


def main() -> None:
    client = AdzunaClient()

    response = client.search_jobs(
        keyword="junior software engineer",
        location="London",
        page=1,
    )
    
    results = response.get("results", [])
    print(f"Found {len(results)} jobs")
    
    if results:
        parsed = parse_adzuna_job(results[0])
        print(parsed)

if __name__ == "__main__":
    main()