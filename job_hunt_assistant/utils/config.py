"""Configuration and constants."""

from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    COVER_LETTERS_DIR = DATA_DIR / "cover_letters"
    APPLICATIONS_LOG = DATA_DIR / "applications_log.csv"
    SAMPLE_RESUME = DATA_DIR / "sample_resume.txt"
