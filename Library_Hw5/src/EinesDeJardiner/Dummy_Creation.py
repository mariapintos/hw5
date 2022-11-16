import pandas as pd


def OneHotEncoding(df, list_of_columns):
    # Generate dummies for ethnicity column (One hot encoding)
    return pd.get_dummies(df, columns=list_of_columns, drop_first=True)


def binary_var(df, column, labels):
    # Create a binary variable for gender M/F. labels = ["M","F"]
    df[column] = df[column].apply(lambda x: 1 if x == labels[0] else 0)
    df[column] = pd.to_numeric(df[column])

    return df
