
import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

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
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
        expected_output = pd.DataFrame(data = {"age":[18, 22]})
        result = clearNA_from_column(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

    def test_fillNA(self):
        data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
        expected_output = pd.DataFrame(data = {"age":[18, 22, 20]})
        result = fillNA(data_to_test, ["age"])
        assert_frame_equal(result, expected_output, check_dtype=False)

if __name__ == "__main__":
    unittest.main()
