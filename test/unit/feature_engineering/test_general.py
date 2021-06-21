from unittest import TestCase

import pandas as pd
import numpy as np

from openstf.feature_engineering.general import enforce_feature_order


class TestGeneral(TestCase):
    def test_enforce_feature_order_with_horizon_columns(self):

        df = pd.DataFrame(
            np.arange(12).reshape(3, 4), columns=["load", "Horizon", "A", "E"]
        )

        result = enforce_feature_order(df)

        self.assertEqual(result.columns.to_list(), ["load", "A", "E", "Horizon"])

    def test_enforce_feature_order(self):

        df = pd.DataFrame(np.arange(9).reshape(3, 3), columns=["load", "A", "E"])
        result = enforce_feature_order(df)
        self.assertEqual(result.columns.to_list(), ["load", "A", "E"])
