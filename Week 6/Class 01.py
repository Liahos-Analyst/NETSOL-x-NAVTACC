# Week 6 | Class 01: NLP foundations, text cleanup and tokenization
# NLTK / spaCy are introduced in the course plan. This starter uses Python first.

import re
import string

text = "AI is amazing! AI helps people analyze text, data, and language. Visit https://example.com"

# Remove URLs, lowercase, remove punctuation, and split into tokens.
cleaned = re.sub(r"https?://\S+|www\.\S+", " ", text)
cleaned = cleaned.lower()
cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))
tokens = cleaned.split()

stopwords = {"is", "and", "the", "a", "to", "of", "in", "helps"}
filtered_tokens = [token for token in tokens if token not in stopwords]

print("Original:", text)
print("Cleaned:", cleaned)
print("Tokens:", tokens)
print("After stopword removal:", filtered_tokens)

# Word and sentence tokenization with NLTK, if installed and data is available.
try:
    import nltk
    from nltk.tokenize import word_tokenize, sent_tokenize
    try:
        word_tokens = word_tokenize(text)
        sentence_tokens = sent_tokenize(text)
        print("\nNLTK words:", word_tokens)
        print("NLTK sentences:", sentence_tokens)
    except LookupError:
        print("\nNLTK is installed, but tokenizer data is missing.")
        print("Run: python -m nltk.downloader punkt punkt_tab")
except ImportError:
    print("\nOptional: pip install nltk")
