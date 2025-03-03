# Spam/Junk email detector
# This script is designed to detect spam/junk email messages.

import re

def calculate_spam_score(message, spam_keywords):
    # Calculates the spam score of a message based on keyword occurrences.

    # Args:
    #     message: The email message as a string.
    #     spam_keywords: A list of spam keywords and phrases.

    # Returns:
    #     A tuple containing the spam score (int) and a list of triggered keywords (list).
    # 

    spam_score = 0
    triggered_keywords = []

    for keyword in spam_keywords:
        # Use regex for case-insensitive and whole-word matching
        matches = re.findall(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE)  # \b for word boundaries
        spam_score += len(matches)
        if matches:
            triggered_keywords.append(keyword)

    return spam_score, triggered_keywords


def rate_spam_likelihood(spam_score):
    # Rates the likelihood of a message being spam based on its score.

    # Args:
    #     spam_score: The spam score of the message.

    # Returns:
    #     A string representing the spam likelihood.
    # 

    if spam_score >= 10:
        return "Very High"
    elif spam_score >= 5:
        return "High"
    elif spam_score >= 2:
        return "Medium"
    else:
        return "Low"


def main():
    # Main function to interact with the user and analyze the email.

    spam_keywords = [
        "free", "win", "guaranteed", "discount", "offer", "limited time", "act now", "click here",
        "urgent", "important information", "special offer", "prize", "congratulations", "bonus",
        "100% free", "work from home", "make money fast", "online casino", "lottery", "debt consolidation",
        "miracle cure", "weight loss", "enlarge", "guarantee", "cancel anytime", "subscribe",
        "unsubscibe", "remove", "address", "recipient", "dear", "friend"
    ]

    email_message = input("Enter the email message:\n")

    spam_score, triggered_keywords = calculate_spam_score(email_message, spam_keywords)
    spam_likelihood = rate_spam_likelihood(spam_score)

    print("\nSpam Score:", spam_score)
    print("Spam Likelihood:", spam_likelihood)

    if triggered_keywords:
        print("Triggered Keywords:", ", ".join(triggered_keywords))
    else:
        print("No spam keywords found.")


if __name__ == "__main__":
    main()