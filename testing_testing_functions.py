import pandas as pd
import numpy as np

def clearNA_from_column(df, list_of_columns):
    return df.dropna(subset=list_of_columns, how="any")


data_to_test = pd.DataFrame(data = {"age":[18, 22, np.nan]})
expected_output = pd.DataFrame(data = {"age":[18, 22]})
result = clearNA_from_column(data_to_test, ["age"]).astype(int)
assert list(result["age"]) == list(expected_output["age"])

print(expected_output.info())
print(expected_output)
print(result.info())
print(result)