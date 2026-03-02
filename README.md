AI Resume Screening & ATS Analyzer

Live Demo Link: https://ai-resume-screening-system-5dy2cbbqehh8e6iq7hmdm8.streamlit.app/


Overview

AI Resume Screening and ATS Analyzer is a Natural Language Processing based Machine Learning application that evaluates how well a resume matches a given job description.

The system extracts text from PDF resumes, preprocesses it using NLP techniques, converts the text into numerical vectors using TF-IDF, and computes similarity using cosine similarity to generate an ATS compatibility score.

This tool helps job seekers identify missing skills and improve their resumes to increase their chances of passing Applicant Tracking Systems.

Objective

The objective of this project is to build an end-to-end AI application that:

Extracts text from resume PDFs

Applies NLP preprocessing

Computes resume and job description similarity

Generates an ATS compatibility score

Identifies matched and missing skills

Displays results using an interactive dashboard

Machine Learning Concepts Used

Natural Language Processing

Text Cleaning and Stopword Removal using NLTK

TF-IDF Vectorization

Cosine Similarity

Vector Space Modeling

Skill Gap Analysis

Features

Resume PDF text extraction

NLP based preprocessing

ATS compatibility score calculation

Matched skills identification

Missing skills detection

Interactive Streamlit dashboard

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

User uploads a resume in PDF format.

User pastes a job description.

The system extracts and cleans the text.

TF-IDF converts the text into numerical vectors.

Cosine similarity computes the ATS score.

Skill gap analysis identifies missing skills.

Results are displayed on the dashboard.

How to Run the Project

Clone the repository
git clone https://github.com/yourusername/AI-Resume-Screening-System.git

Install dependencies
pip install -r requirements.txt

Run the application
streamlit run app.py

Learning Outcomes

Applied NLP techniques to real-world text data

Implemented TF-IDF and cosine similarity

Built an end-to-end machine learning application

Developed and deployed an interactive Streamlit app

Structured a modular Python project

Author

Your Name
B.Tech Information Technology
Machine Learning and Data Science Enthusi
