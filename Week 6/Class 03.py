# Week 6 | Class 03: Bag of Words, document similarity and evaluation metrics

documents = [
    "machine learning makes useful predictions",
    "deep learning uses neural networks",
    "machine learning and deep learning",
]

try:
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(documents)
    print("Vocabulary:", vectorizer.get_feature_names_out())
    print("Bag-of-Words matrix:\n", matrix.toarray())
    similarity = cosine_similarity(matrix)
    print("\nCosine similarity:\n", similarity)
except ImportError:
    print("Install scikit-learn: pip install scikit-learn")

# Classification evaluation example
y_true = [1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

try:
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
    print("\nAccuracy:", round(accuracy_score(y_true, y_pred), 3))
    print("Precision:", round(precision_score(y_true, y_pred, zero_division=0), 3))
    print("Recall:", round(recall_score(y_true, y_pred, zero_division=0), 3))
    print("F1 score:", round(f1_score(y_true, y_pred, zero_division=0), 3))
    print("Confusion matrix:\n", confusion_matrix(y_true, y_pred))
except ImportError:
    pass
