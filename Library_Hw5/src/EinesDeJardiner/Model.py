import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


def return_trained_model_RandomForestClassifier(X, Y, SEED=0):
    # Creates and trains a RandomForestClassifier
    model = RandomForestClassifier(max_depth=9, random_state=SEED)
    model.fit(X, Y)
    return model


def fill_df_predictions(X, model):
    # 
    df = pd.DataFrame(data=X)
    target_prediction = model.predict_proba(X)
    df["predictions"] = target_prediction[:, 1]

    return df


def calc_auc_score(y, y_pred):
    return roc_auc_score(y, y_pred)