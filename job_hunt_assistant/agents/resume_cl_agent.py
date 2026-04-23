"""Resume and cover letter generation utilities."""

from typing import Dict


class ResumeCoverLetterAgent:
    """Generate resume and cover letter content."""

    def create_resume_summary(self, resume_text: str) -> str:
        """Return a brief summary of the supplied resume."""
        return resume_text.strip().replace("\n", " ")[:300]

    def create_cover_letter(self, job_title: str, company: str, resume_summary: str) -> str:
        """Generate a basic cover letter template."""
        return (
            f"Dear {company} Hiring Team,\n\n"
            f"I am writing to apply for the {job_title} role. "
            f"My experience aligns well with the requirements, and I am excited about the opportunity to contribute.\n\n"
            f"Resume summary:\n{resume_summary}\n\n"
            "Thank you for your consideration.\n\nSincerely,\nYour Name"
        )
