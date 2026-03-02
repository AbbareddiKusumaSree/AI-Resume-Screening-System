import streamlit as st
from src.parser import extract_text_from_pdf
from src.preprocessing import clean_text
from src.skill_extraction import extract_skills
from src.ats_engine import calculate_ats_score
from src.recommendation_engine import skill_gap
import time

# -------- PAGE SETTINGS --------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -------- HEADER --------
st.title("🚀 AI Resume Screening & ATS Analyzer")
st.caption("Analyze your resume against job descriptions using Machine Learning")

st.divider()

# -------- INPUT SECTION --------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("📝 Paste Job Description Here")

st.divider()

# -------- ANALYZE BUTTON --------
if st.button("🔍 Analyze Resume", use_container_width=True):

    if not uploaded_file or not job_description:
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing Resume..."):
            time.sleep(1)

            resume_text = extract_text_from_pdf(uploaded_file)
            clean_resume = clean_text(resume_text)
            clean_job = clean_text(job_description)

            ats_score = calculate_ats_score(clean_resume, clean_job)

            resume_skills = extract_skills(clean_resume)
            job_skills = extract_skills(clean_job)
            missing_skills = skill_gap(resume_skills, job_skills)
            matched_skills = list(set(resume_skills) & set(job_skills))

        st.success("Analysis Complete ✅")
        st.divider()

        # -------- ATS SCORE SECTION --------
        st.subheader("📊 ATS Compatibility Score")
        st.progress(int(ats_score))
        st.metric(label="Match Percentage", value=f"{ats_score}%")

        st.divider()

        # -------- SKILL ANALYSIS --------
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.success(skill)
            else:
                st.info("No matched skills found.")

        with col4:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    st.error(skill)
            else:
                st.info("No missing skills.")

        st.divider()

        # -------- FULL SKILL LIST --------
        with st.expander("View All Extracted Resume Skills"):
            st.write(resume_skills)

st.caption("Built using Python | NLP | TF-IDF | Cosine Similarity | Streamlit")