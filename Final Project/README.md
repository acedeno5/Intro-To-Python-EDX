# Smart Resume Analyzer and Optimizer
#### Video Demo:  <https://youtu.be/WLYBsKZjAlU>
#### Description:

The **Smart Resume Analyzer and Optimizer** is a Python-based command-line application designed to help job seekers evaluate and improve their resumes by comparing them against specific job descriptions. By leveraging natural language processing (NLP), the tool extracts meaningful keywords from both a resume and a job listing, calculates a match score, and suggests missing keywords that could enhance the resume’s relevance for the job.

This project was created with the intent to provide a practical, privacy-respecting, and fully offline solution for resume optimization—one that is especially helpful for students, job seekers, and developers applying to technical roles. It is built using Python and the `spaCy` NLP library, with minimal dependencies to keep the setup simple and accessible.

---

### Project Functionality

When the program is executed, it prompts the user to input the file paths to two text files:
1. A resume (`.txt`) file.
2. A job description (`.txt`) file.

The application then:
- **Loads and processes both documents.**
- **Extracts keywords** using part-of-speech filtering and lemmatization to identify the most relevant skills and qualifications.
- **Calculates a match score** based on the overlap of keywords between the resume and job description.
- **Prints a list of suggested keywords** that are present in the job description but missing from the resume.

The result is a match percentage and a list of specific, actionable keyword suggestions to help users tailor their resumes more effectively.

---

### File Overview

- `optimizer.py`: This is the main Python script for the project. It contains:
  - `main()`: Orchestrates the overall workflow of prompting the user, running keyword extraction, scoring, and printing results.
  - `load_text(path)`: Loads and reads the content of a text file.
  - `extract_keywords(text)`: Uses `spaCy` to parse the input text, extracting and normalizing nouns, verbs, and proper nouns while removing stop words and short tokens.
  - `score_resume(resume_keywords, job_keywords)`: Calculates the match score as a percentage of job description keywords present in the resume.
  - `suggest_keywords(resume_keywords, job_keywords)`: Identifies missing but relevant terms to suggest to the user.
  - Three unit test functions (`test_extract_keywords()`, `test_score_resume()`, `test_suggest_keywords()`) are also included and can be toggled via comments.

- `sample_resume.txt`: A sample resume written in plain text to demonstrate how the tool works. This file contains mock experience and skills commonly seen in software engineering roles.

- `sample_job_description.txt`: A realistic job description containing the qualifications and responsibilities of a software engineering position. This file is used to simulate what a company might list in an actual posting.

---

### Design Choices

Several thoughtful decisions went into the architecture of this project:
- **Using plain `.txt` files** instead of PDFs or Word docs keeps the project lightweight and avoids complications with parsing. (That said, it could be expanded later to support richer formats.)
- **Keyword extraction** focuses on nouns, proper nouns, and verbs—these tend to represent skills, tools, and actions relevant to hiring managers.
- **Lemmatization** ensures that different forms of a word (e.g., “develop”, “developing”, “development”) are normalized to a single representation.
- **Set-based comparison** was chosen for simplicity and clarity. While cosine similarity or TF-IDF vectorization could offer more nuance, the current design prioritizes transparency and ease of understanding for beginner to intermediate users.

In future iterations, this project could be expanded to include synonym detection, PDF/Word support, resume formatting tips, or even a Streamlit-based web app interface.

---

### Final Thoughts

This project not only reinforces fundamental skills in Python, text processing, and natural language processing, but also solves a real-world problem that most professionals face at some point. It demonstrates how even a simple, focused script can offer meaningful value and utility. I'm proud of how this turned out and see clear paths to improve and scale it going forward.
