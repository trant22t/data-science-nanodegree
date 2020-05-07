import pandas as pd

from sklearn.utils import shuffle
from sklearn.exceptions import NotFittedError
from sklearn.base import BaseEstimator, TransformerMixin

from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from tqdm import tqdm

from src.models.utils import tokenize, vec_for_learning


class TaggedDocumentTransformer(BaseEstimator, TransformerMixin):
    """
    Transform text document into a list of tokens tagged by its target classes.
    This estimator prepares the data set to be fed into a Doc2Vec model
    for document embeddings.
    """
    def fit(self, X, Y):
        """Perform nothing but need to exist to comply with Transformer API"""
        return self

    def transform(self, X, Y):
        """
        Represent document as list of tokens and tags
        :param X: text messages from data
        :param y: their target classes
        :return: the tagged representation of document
        """
        data = pd.concat([X, Y], axis=1)
        data_tagged = data.apply(
            lambda r: TaggedDocument(words=tokenize(r['message']),
                                     tags=r[Y.columns],
                                     axis=1))
        return data_tagged


class Doc2VecTransformer(BaseEstimator, TransformerMixin):
    """
    Transform text data into Doc2Vec embeddings while maintaining
    tags that indicate their classes.

    This estimator builds a Doc2Vec (Distributed Memory) model based on
    the vocabulary of the training set. This model can then be applied
    to text of unseen data to infer their embeddings. Outputs of the estimator
    can be fed directly into a traditional machine learning method (e.g.:
    logistic regression, random forest, etc.)

    :attr model_d2v_: fitted Doc2Vec model
    """
    def _reset(self):
        """Reset internal data-dependent state of the transformer, if necessary"""
        if hasattr(self, 'model_d2v_'):
            del self.model_d2v_

    def fit(self, data_tagged):
        """
        Fit the Doc2Vec model used for transforming
        :param data_tagged: lists of word tokens from texts and their tagged classes
        :return: estimator with its Doc2Vec model as an attribute
        """
        # reset internal state before fitting
        self._reset()

        # build Doc2Vec Distributed Memory model based on training data
        # Tips on how to improve gensim.doc2vec model (https://stackoverflow.com/questions/47890052/improving-gensim-doc2vec-results)
        # Don't make min_alpha the same as alpha. Only expert users should be changing alpha/min_alpha defaults.
        # Don't set min_count=1. Rare words that only appear once are generally not helpful. Default is 5.
        # Don't call train() multiple times in a loop with explicit alpha management, unless you're positive you know what you're doing.
        # Instead, call train() once, with a correct total_examples, and a well-chosen epochs value.
        # Make sure corpus can be iterated over multiple times and not a single-use iterator.
        model_dmm = Doc2Vec(dm=1, dm_mean=1, workers=5, seed=42)
        model_dmm.build_vocab([x for x in tqdm(data_tagged.values)])
        model_dmm.train(shuffle([x for x in tqdm(data_tagged.values)]),
                        total_examples=len(data_tagged.values),
                        epochs=20)

        self.model_d2v_ = model_dmm

        return self

    def transform(self, data_tagged):
        """
        Infer embeddings
        :param data_tagged: lists of word tokens from texts and their tagged classes
        :return: word embeddings for texts and their target classes
        """
        if hasattr(self, 'model_d2v_'):
            X_d2v, Y_d2v = vec_for_learning(self.model_d2v_, data_tagged)
        else:
            raise NotFittedError('This instance is not fitted yet. Call "fit" with'
                                 'appropriate arguments before using this estimator.')

        return X_d2v, Y_d2v

