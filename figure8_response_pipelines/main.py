import sys
from src.data.process_data import load_raw_data, clean_data, save_data
from src.models.train_classifier import load_clean_data, build_tfidf_rf_model, build_d2v_rf_model, create_modeling_pipeline
from sklearn.model_selection import train_test_split

command = sys.argv[1]
args = sys.argv[2:]

if __name__ == '__main__':
    if command == 'process_data':
        if len(args) == 3:
            messages_filepath, categories_filepath, database_filepath = args

            print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
                  .format(messages_filepath, categories_filepath))
            df = load_raw_data(messages_filepath, categories_filepath)

            print('Cleaning data...')
            df = clean_data(df)

            print('Saving data...\n    DATABASE: {}'.format(database_filepath))
            save_data(df, database_filepath)

            print('Cleaned data saved to database!')

        else:
            print('Please provide the file paths of the messages and categories',
                  'data sets as the second and third argument respectively, as',
                  'well as the file path of the database to save the cleaned data',
                  'to as the fourth argument. \n\nExample: python main.py process_data',
                  'data/disaster_messages.csv data/disaster_categories.csv',
                  'data/DisasterResponse.db')

    elif command == 'train_classifier':
        if len(args) == 2:
            database_filepath, model_name = args

            print('Loading data...\n    DATABASE: {}'.format(database_filepath))
            X, Y, category_names = load_clean_data(database_filepath)
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

            if model_name == 'tfidf_rf':
                model_filepath = 'models/tfidf_rf.pkl'

                print('Instantiating TF-IDF/random forest model...')
                tfidf_rf_model = build_tfidf_rf_model()

                print('Executing TF-IDF/random forest pipeline...')
                create_modeling_pipeline(tfidf_rf_model, model_name, X_train, X_test, Y_train, Y_test,
                                         category_names, model_filepath)

            elif model_name == 'd2v_rf':
                model_filepath = 'models/d2v_rf.pkl'

                print('Instantiating Doc2Vec/random forest model...')
                d2v_rf_model = build_d2v_rf_model()

                print('Executing Doc2Vec/random forest pipeline...')
                create_modeling_pipeline(d2v_rf_model, model_name, X_train, X_test, Y_train, Y_test,
                                         category_names, model_filepath)

            else:
                print('Please provide the correct model name that you want to train.',
                      'There are two options: "tfidf_rf" which trains a TF-IDF then a random forest model',
                      'or "d2v_rf" which trains a Doc2Vec then a random forest model. \n\nExample: python main.py',
                      'train_classifier data/DisasterResponse.db tfidf_rf')

        else:
            print('Please provide the file path of the disaster messages database',
                  'as the second argument and the name of the model you want to train',
                  'as the third argument. \n\nExample: python main.py train_classifier',
                  'data/DisasterResponse.db tfidf_rf')

    else:
        print('Please provide a command of what script you want to run as the first argument.',
              'There are two options: process_data for building the ETL pipeline and train_classifier',
              'for building the ML pipeline.')
