import pickle

# Load saved model and vectorizer
model = pickle.load(open("ml/question_model.pkl", "rb"))
vectorizer = pickle.load(open("ml/vectorizer.pkl", "rb"))


def generate_questions(job_description_text, role, experience, num_questions):
    # Convert JD to vector
    vect = vectorizer.transform([job_description_text])
    predicted = model.predict(vect)

    # Get questions string → split by ? to return individual
    questions = predicted[0].split("?")
    cleaned = [q.strip() + "?" for q in questions if q.strip()]

    return cleaned[:num_questions]


# import re
# import random

# def extract_keywords(text):
#     # Very simple keyword extraction (we'll improve this later)
#     words = re.findall(r'\b\w+\b', text.lower())
#     common_words = {"and", "the", "with", "for", "using", "from", "this", "that", "your", "you", "a", "an", "of", "in", "to", "on"}
#     keywords = [word for word in words if word not in common_words and len(word) > 3]
#     return list(set(keywords))

# def generate_questions(job_description_text, role, experience, num_questions):
#     keywords = extract_keywords(job_description_text)
#     questions = []

#     templates = [
#         "Can you explain your experience with {}?",
#         "How would you use {} in your current project?",
#         "What challenges have you faced while working with {}?",
#         "Can you walk me through a use case involving {}?",
#         "What are some best practices with {}?"
#     ]

#     for i in range(num_questions):
#         if keywords:
#             kw = random.choice(keywords)
#             template = random.choice(templates)
#             questions.append(template.format(kw))
#         else:
#             questions.append(f"Describe a scenario in your role as {role} with {experience} years of experience.")

#     return questions
