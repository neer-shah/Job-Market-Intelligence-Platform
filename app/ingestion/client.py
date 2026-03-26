# Call the external API and return raw JSON

import httpx
from app.core.config import settings
class AdzunaClient:
    BASE_URL = "https://api.adzuna.com/v1/api/jobs/gb/search"

    def __init__(self) -> None:
        self.app_id = settings.adzuna_app_id
        self.app_key = settings.adzuna_app_key

    def search_jobs(self, keyword: str, location: str, page: int = 1) -> dict:
        url = f"{self.BASE_URL}/{page}"
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "what": keyword,
            "where": location,
            "results_per_page": 10,
            "content-type": "application/json",
        }

        response = httpx.get(url, params=params, timeout=30.0)
        response.raise_for_status()
        return response.json()
