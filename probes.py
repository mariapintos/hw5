from sklearn.ensemble import RandomForestClassifier
import pandas as pd
def fill_df_predictions(X, model):
    # 
    df = pd.DataFrame(data=X).copy()
    target_prediction = model.predict_proba(X)
    df["predictions"] = target_prediction[:, 1]

    return df

data = {
            "age" : [18,22],
            "beautifullness":[9,4],
            "followers":[10000, 244]
        }

df = pd.DataFrame(data = data)
X = df[["age", "beautifullness"]]
Y = df["followers"]

model = RandomForestClassifier()
model.fit(X,Y)

df_test = df.copy()
df_test = fill_df_predictions(X, model)

df_expected = df.copy()
df_expected = df_expected.drop("followers", axis = 1)
print(X)
df_expected["predictions"] = model.predict_proba(X)[:, 1]

print(df_expected)
print(df_test)