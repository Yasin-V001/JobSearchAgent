"""API client for USAJOBS."""

from typing import List, Dict


class USAJobsAPI:
    """Simple USAJOBS client placeholder."""

    def search_jobs(self, keywords: str, location: str = "") -> List[Dict[str, str]]:
        """Return a mock list of job postings."""
        return [
            {
                "title": f"{keywords} Specialist",
                "agency": "USAJOB Example Agency",
                "location": location or "Washington, DC",
            }
        ]
