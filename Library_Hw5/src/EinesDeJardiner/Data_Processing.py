def clearNA_from_column(df, list_of_columns):
    # Remove those rows that contain NaN values in the columns: age, gender, ethnicity
    return df.dropna(subset=list_of_columns, how="any")


def fillNA(df, list_of_columns):
    # Fill NaN with the mean value of the column in the columns: height, weight.
    for column in list_of_columns:
        mean = df[column].mean()
        df[column] = df[column].fillna(mean)
    return df
    
