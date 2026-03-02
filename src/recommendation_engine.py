def skill_gap(resume_skills, job_skills):
    missing = list(set(job_skills) - set(resume_skills))
    return missing