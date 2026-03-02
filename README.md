AI Resume Screening & ATS Analyzer

Live Demo Link: https://ai-resume-screening-system-5dy2cbbqehh8e6iq7hmdm8.streamlit.app/

Overview

AI Resume Screening & ATS Analyzer is an NLP-based Machine Learning application that evaluates how well a resume matches a given job description.

The system extracts text from PDF resumes, preprocesses it using Natural Language Processing techniques, converts text into numerical vectors using TF-IDF, and computes similarity using cosine similarity to generate an ATS compatibility score.

This tool helps job seekers identify missing skills and improve their resumes to increase the chances of passing Applicant Tracking Systems (ATS).

Objective

To build an end-to-end AI application that:

Extracts text from resume PDFs


Applies NLP preprocessing

Computes resume-job similarity score

Performs skill gap analysis

Displays results in an interactive dashboard

Machine Learning Concepts Used

Natural Language Processing (NLP)


Text Cleaning & Stopword Removal

TF-IDF (Term Frequency – Inverse Document Frequency)

Cosine Similarity

Vector Space Modeling

Skill Gap Analysis

Features

Resume PDF text extraction using pdfplumber


NLP-based text preprocessing using NLTK

ATS compatibility score calculation

Matched skills identification

Missing skills detection

Interactive Streamlit dashboard

Visual score representation

Tech Stack

Python

scikit-learn

NLTK

pdfplumber

Streamlit

Pandas

NumPy

Project Structure

AI_Resume_Intelligence_System/
│
├── src/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── skill_extraction.py
│   ├── ats_engine.py
│   └── recommendation_engine.py
│
├── app.py
├── requirements.txt
└── README.md

How It Works

User uploads a Resume (PDF).


User pastes a Job Description.

System extracts text from the resume.

Text is cleaned using NLP preprocessing.

TF-IDF converts text into numerical vectors.

Cosine similarity computes ATS compatibility score.


Skill gap analysis identifies missing skills.

Results are displayed in the Streamlit dashboard.

 How to Run Locally

1️ Clone Repository

git clone https://github.com/yourusername/AI-Resume-Screening-System.git

cd AI-Resume-Screening-System

2️ Install Dependencies

pip install -r requirements.txt

3️ Run Application

streamlit run app.py

📌 Sample Use Case

Upload your resume.

Paste a Machine Learning job description.

Get:

ATS Match Percentage

Matched Skills

Missing Skills


Learning Outcomes


Through this project, I gained hands-on experience in:

Applying NLP techniques to real-world problems

Implementing TF-IDF and cosine similarity

Building end-to-end ML applications

Deploying interactive apps using Streamlit

Structuring modular Python projects


Author


Abbareddi Kusuma Sree
B.Tech – Information Technology
