import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    else:
        feedback.append("Make it at least 12 characters long!")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters!")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters!")

    # Check numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers!")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters!")

    # Decide strength
    if score >= 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium 😐"
    else:
        strength = "Weak 😟"

    return strength, feedback


# === Main Program ===
print("=== Simple Password Strength Checker ===\n")

pwd = input("Enter a password to check: ")

strength, tips = check_password_strength(pwd)

print("\nResult:")
print(f"Password strength: {strength}")

if tips:
    print("\nSuggestions to make it stronger:")
    for tip in tips:
        print("→ " + tip)
else:
    print("\nGreat! This password looks very strong.")