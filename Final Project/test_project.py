import spacy
from project import extract_keywords
from project import score_resume
from project import suggest_keywords
import pytest
# ---------------- TEST FUNCTIONS ----------------

def main():
    test_extract_keywords()
    test_score_resume()
    test_suggest_keywords()

def test_extract_keywords():
    text = "I have experience in Python, data analysis, and machine learning."
    keywords = extract_keywords(text)
    assert "python" in keywords
    assert "analysis" in keywords
    assert "learning" in keywords
    print("✅ test_extract_keywords passed.")

def test_score_resume():
    resume = {"python", "analysis", "sql"}
    job = {"python", "sql", "communication", "teamwork"}
    score = score_resume(resume, job)
    assert round(score) == 50
    print("✅ test_score_resume passed.")

def test_suggest_keywords():
    resume = {"python", "sql"}
    job = {"python", "sql", "excel", "teamwork"}
    suggestions = suggest_keywords(resume, job)
    assert "excel" in suggestions and "teamwork" in suggestions
    print("✅ test_suggest_keywords passed.")


if __name__ == "__main__":
    main()
