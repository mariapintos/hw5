
import unittest
import pandas as pd

# Defining the functions
def OneHotEncoding(df, list_of_columns):
    # Generate dummies for ethnicity column (One hot encoding)
    return pd.get_dummies(df, columns=list_of_columns, drop_first=True)


def binary_var(df, column, labels):
    # Create a binary variable for gender M/F. labels = ["M","F"]
    df[column] = df[column].apply(lambda x: 1 if x == labels[0] else 0)
    df[column] = pd.to_numeric(df[column])
    return df

# Testing the functions
class Test_Dummy_Creation(unittest.TestCase):
    def test_OneHotEncoding(self):
        df = pd.read_csv('/Users/lluisarull/Desktop/DSDM/Computing_for_Data_Science/Homework_5/sample_diabetes_mellitus_data - sample_diabetes_mellitus_data.csv')
        list_of_columns_OneHotEncoding = ["ethnicity"]
        result = OneHotEncoding(df, list_of_columns_OneHotEncoding)
        expected_output = pd.get_dummies(df, columns=['ethnicity'])
        self.assertEqual(result, expected_output)

    def test_binary_var(self):
        df = pd.read_csv('/Users/lluisarull/Desktop/DSDM/Computing_for_Data_Science/Homework_5/sample_diabetes_mellitus_data - sample_diabetes_mellitus_data.csv')
        column = "gender"
        labels = ["M", "F"]
        result_df = binary_var(df, column, labels)
        result_column = result_df['gender']
        dummy = pd.get_dummies(df['gender']) 
        df2 = pd.concat((df, dummy), axis=1)
        df3 = df2.drop(['gender','F'])
        expected_output= df3['M']
        self.assertEqual(result_column, expected_output)

if __name__ == '__main__':
    unittest.main()