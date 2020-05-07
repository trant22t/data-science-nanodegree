import string

import nltk
nltk.download(['punkt', 'stopwords', 'wordnet'])

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def tokenize(text):
    """
    Normalize, lemmatize and tokenize text
    :param text: message from data
    :return: list of tokens
    """
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(clean_text)
    lemmatizer = WordNetLemmatizer()
    final_tokens = [lemmatizer.lemmatize(tok).lower().strip()
                    for tok in tokens if tok not in set(stopwords.words('english'))]
    return final_tokens


def vec_for_learning(model, tagged_docs):
    """
    Build the vector feature that represents text from the trained doc2vec embeddings
    :param model: doc2vec model that has been trained and will be used for inference
    :param tagged_docs: documents which have been tagged
    :return: tagged documents and their inferred classes based on trained model
    """
    sents = tagged_docs.values
    targets, regressors = zip(*[(doc.tags, model.infer_vector(doc.words, steps=20)) for doc in sents])
    return regressors, targets
