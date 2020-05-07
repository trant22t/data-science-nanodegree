import pandas as pd
from sqlalchemy import create_engine


def load_raw_data(messages_filepath, categories_filepath):
    """
    Merge messages and categories data sets
    :param messages_filepath: file path to messages data
    :param categories_filepath: file path to categories data
    :return: merged data
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df


def clean_data(df):
    """
    Split categories columns into separate, clearly named columns,
    convert values to binary and drop duplicates
    :param df: merged data set from messages and categories
    :return: cleaned version of merged data set
    """
    categories = df['categories'].str.split(';', expand=True)
    categories.columns = categories.head(1).apply(lambda x: x.str.split('-')[0][0])
    cleaned_categories = categories.applymap(lambda x: pd.to_numeric(x[-1]))
    df.drop('categories', inplace=True, axis=1)
    df = pd.concat([df, cleaned_categories], axis=1)
    df.drop_duplicates(inplace=True)
    return df


def save_data(df, database_filename):
    """
    Store the clean data into a SQLite database in the specified database file path
    :param df: clean data
    :param database_filename: name of database
    :return: None
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('disaster_responses', engine, index=False, if_exists='replace')
