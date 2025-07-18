# Smart Resume Analyzer & Optimizer
import spacy
# Pip install spacy
# python -m spacy download en_core_web_sm

def main():
    print("📄 Resume Analyzer\n")

    resume_path = input("Enter your resume text file path: ").strip()
    job_path = input("Enter job description text file path: ").strip()

    resume_text = load_text(resume_path)
    job_text = load_text(job_path)

    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)

    score = score_resume(resume_keywords, job_keywords)
    suggestions = suggest_keywords(resume_keywords, job_keywords)

    print(f"\n✅ Resume Match Score: {score:.2f}%")
    print("\n🔍 Suggested keywords to add:")
    for word in suggestions:
        print(f" - {word}")

def load_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def extract_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    keywords = set()

    for token in doc:
        if token.pos_ in {"NOUN", "PROPN", "VERB"} and not token.is_stop and token.is_alpha:
            lemma = token.lemma_.strip().lower()
            if len(lemma) > 2:  # Skip overly short words like "go"
                keywords.add(lemma)

    return keywords

def score_resume(resume_kw, job_kw):
    if not job_kw:
        return 0.0
    matched = resume_kw.intersection(job_kw)
    return (len(matched) / len(job_kw)) * 100

def suggest_keywords(resume_kw, job_kw):
    return sorted(job_kw - resume_kw)

if __name__ == "__main__":
    main()
