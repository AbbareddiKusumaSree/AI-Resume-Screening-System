AI Resume Screening & ATS Analyzer

Live Demo Link: https://ai-resume-screening-system-5dy2cbbqehh8e6iq7hmdm8.streamlit.app/


AI Resume Screening and ATS Analyzer
Overview

This project is a Machine Learning based Resume Screening System that evaluates how well a resume matches a given job description.

The system extracts text from resume PDFs, applies Natural Language Processing techniques, and calculates an ATS compatibility score using TF-IDF and cosine similarity.

It also identifies matched and missing skills to help improve the resume.

Objective

The objective of this project is to:
Extract text from resume PDF. Preprocess text using NLP. Convert text into numerical vectors. Compute similarity between resume and job description. Generate an ATS match percentage. Identify missing skills.

Machine Learning Techniques Used

Natural Language Processing (NLP). Stopword Removal (NLTK). TF-IDF Vectorization. Cosine Similarity. Skill Gap Analysis

Tech Stack

Python

scikit-learn

NLTK

pdfplumber

Streamlit

Pandas

NumPy

Project Structure

AI_Resume_Intelligence_System

src

parser.py

preprocessing.py

skill_extraction.py

ats_engine.py

recommendation_engine.py

app.py
requirements.txt
README.md

How It Works

Upload Resume (PDF)

Paste Job Description

System processes and cleans text. TF-IDF converts text into vectors. Cosine similarity calculates ATS score. Displays matched and missing skills

How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Learning Outcomes

Applied NLP techniques to real-world data

Implemented TF-IDF and cosine similarity

Built an end-to-end ML application

Developed a deployable Streamlit app
