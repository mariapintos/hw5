
import unittest
import pandas as pd

# Defining the functions
def clearNA_from_column(df, list_of_columns):
    return df.dropna(subset=list_of_columns, how="any")

def fillNA(df, list_of_columns):
    # Fill NaN with the mean value of the column in the columns: height, weight.
    for column in list_of_columns:
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)
    return df

# Testing the functions
class Test_Data_Processing(unittest.TestCase):
    def test_clearNA(self):
        df = pd.read_csv('/Users/lluisarull/Desktop/DSDM/Computing_for_Data_Science/Homework_5/sample_diabetes_mellitus_data - sample_diabetes_mellitus_data.csv')
        list_of_columns = ['gender', 'age', 'ethnicity']
        result = clearNA_from_column(df, list_of_columns)
        expected_output = df.dropna(subset=['gender','age','ethnicity'], how="any")
        self.assertEqual(result, expected_output)

    def test_fillNA(self):
        df = pd.read_csv('/Users/lluisarull/Desktop/DSDM/Computing_for_Data_Science/Homework_5/sample_diabetes_mellitus_data - sample_diabetes_mellitus_data.csv')
        columns_to_fill = ['height', 'weight']
        result = fillNA(df,columns_to_fill)
        expected_output = df['height','weight'].fillna(df[['height','weight']].mean())
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

