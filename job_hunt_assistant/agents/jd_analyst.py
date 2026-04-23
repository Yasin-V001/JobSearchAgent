"""Job description analysis utilities."""

from typing import Dict


class JDAnalyst:
    """Analyze job descriptions and extract key information."""

    def analyze(self, job_description: str) -> Dict[str, str]:
        """Return a simple analysis of the job description."""
        lines = [line.strip() for line in job_description.splitlines() if line.strip()]
        summary = " ".join(lines[:3])
        return {
            "summary": summary,
            "requirements": "; ".join(lines[3:6]) if len(lines) > 3 else "",
        }
