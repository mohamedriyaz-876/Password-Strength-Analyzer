import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=<>?/]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    return score, feedback

