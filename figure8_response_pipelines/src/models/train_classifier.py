from sqlalchemy import create_engine
import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score

from src.models.utils import tokenize
from src.models.DocumentTransformer import TaggedDocumentTransformer, Doc2VecTransformer


def load_clean_data(database_filepath):
    """
    Retrieve data from database
    :param database_filepath: file path of database
    :return: messages (as predictors), target variables and names of these targets
    """
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('disaster_responses', engine)
    X = df['message']
    Y = df.drop(['id', 'message', 'original', 'genre'], axis=1)
    category_names = Y.columns
    return X, Y, category_names


def build_tfidf_rf_model():
    """
    Build a pipeline that processes text into a matrix of token counts,
    applies TF-IDF, and then performs multi-output classification
    based on random forest. The pipeline also goes through grid search to
    find the best parameters for the model.
    :return: pipeline
    """
    pipeline = Pipeline([
        ('cnt_vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('multi_output_clf', MultiOutputClassifier(RandomForestClassifier(random_state=42)))
    ])
    parameters = {
        # lower and upper bound for n-grams
        'cnt_vect__ngram_range': ((1, 1), (1, 2)),
        # upper bound for document frequency
        'cnt_vect__max_df': (0.5, 0.75, 1.0),
        # # build vocab based on top max_features ordered by term-frequency
        'cnt_vect__max_features': (None, 5000, 10000),
        # whether to enable reweighting for inverse-document-frequency
        'tfidf__use_idf': (True, False),
        # number of trees in random forest
        'multi_output_clf__estimator__n_estimators': (50, 100),
        # min number of samples required to split
        'multi_output_clf__estimator__min_samples_split': (2, 4)
    }
    cv = GridSearchCV(pipeline, param_grid=parameters)
    return cv


def build_d2v_rf_model():
    """
    Build a pipeline that transforms texts into list of tokens accompanied with
    their tags, infers their embeddings from Doc2Vec model, and then performs
    a multi-output classifier based on random forest.
    :return: pipeline
    """
    pipeline = Pipeline([
        ('tagged_data', TaggedDocumentTransformer()),
        ('d2v_embs', Doc2VecTransformer()),
        ('multi_output_clf', MultiOutputClassifier(RandomForestClassifier(random_state=42)))
    ])
    return pipeline


def evaluate_model(model, model_name, X_test, Y_test, category_names):
    """
    Display and save auc, precision, recall and F1 score on the test set for all categories
    :param model: trained model
    :param model_name: name of the trained model to used for output file name
    :param X_test: predictors/text messages of test set
    :param Y_test: categories of test set
    :param category_names: names of the corresponding categories
    :return: None
    """
    Y_pred = model.predict(X_test)
    target_lst, auc_lst, recall_lst, precision_lst, f1_lst = [], [], [], [], []
    for i in range(Y_test.shape[1]):
        y_true = Y_test.iloc[:, i]
        y_pred = Y_pred[:, i]
        target_lst.append(category_names[i])
        auc_lst.append(roc_auc_score(y_true, y_pred))
        recall_lst.append(recall_score(y_true, y_pred))
        precision_lst.append(precision_score(y_true, y_pred))
        f1_lst.append(f1_score(y_true, y_pred))
    results = pd.DataFrame({'target_variable': target_lst,
                            'auc': auc_lst,
                            'recall': recall_lst,
                            'precision': precision_lst,
                            'f1_score': f1_lst})
    results.to_csv('output/{}_eval_res.csv'.format(model_name))
    print(results)


def save_model(model, model_filepath):
    """
    Save trained model to pickle file
    :param model: trained model
    :param model_filepath: location to save file
    :return: None
    """
    pickle.dump(model, open(model_filepath, 'wb'))


def create_modeling_pipeline(model, model_name, X_train, X_test, Y_train, Y_test, category_names, model_filepath):
    """
    Execute the whole process from fitting, to evaluating, to saving model
    :param model: instantiated model
    :param model_name: name of trained model to be used for output file name
    :param X_train: predictors of training set
    :param X_test: predictors of test set
    :param Y_train: targets of training set
    :param Y_test: targets of test set
    :param category_names: names of targets
    :param model_filepath: location to save trained model
    :return: None
    """
    print('Training model...')
    model.fit(X_train, Y_train)

    print('Evaluating model...')
    evaluate_model(model, model_name, X_test, Y_test, category_names)

    print('Saving model...\n    MODEL: {}'.format(model_filepath))
    save_model(model, model_filepath)

    print('Trained model saved!')

