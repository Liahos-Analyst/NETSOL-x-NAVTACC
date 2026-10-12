# Week 6 | Class 02: Stemming, lemmatization, POS, NER and chunking
# These demonstrations use NLTK when available; POS/NER may need downloaded models.

words = ["connect", "connected", "connecting", "studies", "studying", "cars"]

try:
    import nltk
    from nltk.stem import PorterStemmer, WordNetLemmatizer

    stemmer = PorterStemmer()
    print("Stemming:")
    for word in words:
        print(word, "->", stemmer.stem(word))

    try:
        lemmatizer = WordNetLemmatizer()
        print("\nLemmatization:")
        for word in ["cars", "studies", "running", "better"]:
            print(word, "->", lemmatizer.lemmatize(word))
    except LookupError:
        print("WordNet data missing. Run: python -m nltk.downloader wordnet")

    sentence = "Ayesha studies artificial intelligence in Lahore."
    try:
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        print("\nPOS tags:", tagged)
        named_entities = nltk.ne_chunk(tagged)
        print("Named entities:", named_entities)
    except LookupError:
        print("\nPOS/NER data missing. Run: python -m nltk.downloader punkt punkt_tab averaged_perceptron_tagger_eng maxent_ne_chunker_tab words")
except ImportError:
    print("Install NLTK for these exercises: pip install nltk")

# Regex extraction: find emails and numbers from text
import re
sample = "Contact ai.team@example.com or support@example.org. We have 3 projects in 2026."
print("\nEmails:", re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", sample))
print("Numbers:", re.findall(r"\d+", sample))
