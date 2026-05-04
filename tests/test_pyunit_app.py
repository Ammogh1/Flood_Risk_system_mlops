import unittest
import os
import sys

sys.path.insert(0, os.path.abspath('src'))
from utils import generate_dummy_tabular_data, generate_dummy_images

class TestFloodRiskSystem(unittest.TestCase):

    def test_generate_tabular_data(self):
        df = generate_dummy_tabular_data(10)
        self.assertEqual(len(df), 10)
        self.assertIn('Flood_Risk', df.columns)
        self.assertTrue(os.path.exists('data/dummy_tabular_data.csv'))

    def test_generate_images(self):
        generate_dummy_images(10)
        self.assertTrue(os.path.exists('data/images/flood'))
        self.assertTrue(os.path.exists('data/images/no_flood'))
        flood_imgs = os.listdir('data/images/flood')
        self.assertGreaterEqual(len(flood_imgs), 5)

    def test_ml_prediction_import(self):
        try:
            from ml_model import predict_ml
            self.assertTrue(callable(predict_ml))
        except ImportError:
            self.fail("Failed to import predict_ml")

    def test_dl_prediction_import(self):
        try:
            from dl_model import predict_dl
            self.assertTrue(callable(predict_dl))
        except ImportError:
            self.fail("Failed to import predict_dl")

    def test_qml_prediction_import(self):
        try:
            from qml_model import predict_qml
            self.assertTrue(callable(predict_qml))
        except ImportError:
            self.fail("Failed to import predict_qml")

if __name__ == '__main__':
    unittest.main()
