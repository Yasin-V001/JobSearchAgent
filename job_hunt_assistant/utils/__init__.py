"""Utility modules for the job hunt assistant."""

from .config import Config
from .tracking import log_application, save_cover_letter_file

__all__ = ["Config", "log_application", "save_cover_letter_file"]
