"""Tracking utilities for applications and files."""

import csv
from datetime import datetime
from pathlib import Path
import re

from .config import Config


def save_cover_letter_file(job_title: str, cover_letter: str, directory: Path = Config.COVER_LETTERS_DIR) -> Path:
    """Save a generated cover letter to disk."""
    sanitized_title = re.sub(r"[^\w\-_ ]", "_", job_title).strip()
    directory.mkdir(parents=True, exist_ok=True)
    filename = f"{sanitized_title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = directory / filename
    filepath.write_text(cover_letter, encoding="utf-8")
    return filepath


def log_application(job_title: str, agency: str, resume_summary: str, filepath: Path = Config.APPLICATIONS_LOG) -> None:
    """Append an application record to the CSV log."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    exists = filepath.exists()
    with filepath.open("a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not exists:
            writer.writerow(["Job Title", "Agency", "ResumeSummary", "DateApplied"])
        writer.writerow([job_title.strip(), agency.strip(), resume_summary.strip()[:150], datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
