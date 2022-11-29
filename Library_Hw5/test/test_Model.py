import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from pandas.testing import assert_frame_equal
from EinesDeJardiner.Model import return_trained_model_RandomForestClassifier, fill_df_predictions, calc_auc_score

# Testing the functions
class Test_Model(unittest.TestCase):
    def test_return_trained_model(self):
        X= 
        Y=
        model_train = return_trained_model_RandomForestClassifier(X, Y, SEED=0)
        model_expected = model.fit(X, Y)
        assert type(model_expected) == type(model)  
    
    def test_fill_df_predictions(self):
        X= 
        model_prediction = fill_df_predictions(X, model) 
        expected_prediction = model.predict_proba(X)
        assert_frame_equal(model_prediction, expected_prediction)
       

    def test_calc_auc_score(self):
        y =
        y_pred = 
        auc = calc_auc_score(y, y_pred)
        auc_expected = 
        assert_frame_equal(auc, auc_expected)


if __name__ == '__main__':
    unittest.main()

