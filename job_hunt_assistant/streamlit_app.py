"""Streamlit app for the job hunt assistant."""

import streamlit as st

from .orchestrator import Orchestrator


def main() -> None:
    st.title("Job Hunt Assistant")
    orchestrator = Orchestrator()

    job_title = st.text_input("Job Title")
    company = st.text_input("Company")
    job_description = st.text_area("Job Description")
    resume_text = st.text_area("Resume Text", value="")

    if st.button("Generate Application"):
        if not (job_title and company and job_description and resume_text):
            st.warning("Please fill in all fields.")
        else:
            result = orchestrator.process_job_application(
                job_title=job_title,
                company=company,
                job_description=job_description,
                resume_text=resume_text,
            )
            st.subheader("Resume Summary")
            st.write(result["resume_summary"])
            st.subheader("Cover Letter")
            st.text_area("Generated Cover Letter", value=result["cover_letter"], height=250)


if __name__ == "__main__":
    main()
