from sqlalchemy import create_engine
import pandas as pd
import great_expectations as ge

engine = create_engine('sqlite:///{}'.format('data/DisasterResponse.db'))
df = pd.read_sql_table('disaster_responses', engine)
binary_target_cols = [i for i in df.columns if i not in ['id', 'message', 'original', 'genre', 'related']]
all_cols = df.columns

df_ge = ge.dataset.PandasDataset(df)
df_ge.expect_table_column_count_to_be_between(min_value=37)  # minimum 36 targets + 1 text predictor
df_ge.expect_multicolumn_values_to_be_unique(all_cols)  # no duplicates
df_ge.expect_column_distinct_values_to_be_in_set('related', [0, 1, 2])
for col in binary_target_cols:
    df_ge.expect_column_distinct_values_to_be_in_set(col, [0, 1])
df_ge.save_expectation_suite('great_expectations/expectations/processed_data_validation.json')

