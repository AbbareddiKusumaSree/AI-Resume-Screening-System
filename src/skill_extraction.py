SKILLS_DB = [
    "python", "sql", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy",
    "scikit-learn", "excel", "power bi", "streamlit"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))