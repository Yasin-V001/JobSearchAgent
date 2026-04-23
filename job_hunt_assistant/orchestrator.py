"""Orchestration logic for the job hunt assistant."""

from .agents.jd_analyst import JDAnalyst
from .agents.messaging_agent import MessagingAgent
from .agents.resume_cl_agent import ResumeCoverLetterAgent
from .utils.tracking import log_application, save_cover_letter_file


class Orchestrator:
    """Coordinate analysis, document generation, and tracking."""

    def __init__(self) -> None:
        self.jd_analyst = JDAnalyst()
        self.messaging_agent = MessagingAgent()
        self.resume_cl_agent = ResumeCoverLetterAgent()

    def process_job_application(
        self,
        job_title: str,
        company: str,
        job_description: str,
        resume_text: str,
    ) -> dict:
        analysis = self.jd_analyst.analyze(job_description)
        resume_summary = self.resume_cl_agent.create_resume_summary(resume_text)
        cover_letter = self.resume_cl_agent.create_cover_letter(job_title, company, resume_summary)
        save_cover_letter_file(job_title, cover_letter)
        log_application(job_title, company, resume_summary)
        self.messaging_agent.send_message(
            recipient="self@example.com",
            subject=f"Applied for {job_title}",
            body=f"Application submitted to {company}.",
        )
        return {
            "analysis": analysis,
            "resume_summary": resume_summary,
            "cover_letter": cover_letter,
        }
