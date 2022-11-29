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
        y=
        model = return_trained_model_RandomForestClassifier(X, Y, SEED=0)
        model_expected = model.fit(dummy_y, dummy_msgs)
        assert type(model_expected) == type(model)  # must return the same type of object



if __name__ == '__main__':
    unittest.main()