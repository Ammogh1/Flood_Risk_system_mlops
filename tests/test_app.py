import pytest
import os
import numpy as np
from utils import generate_dummy_tabular_data, generate_dummy_images

def test_generate_tabular_data():
    df = generate_dummy_tabular_data(10)
    assert len(df) == 10
    assert 'Flood_Risk' in df.columns
    assert os.path.exists('data/dummy_tabular_data.csv')

def test_generate_images():
    generate_dummy_images(10)
    assert os.path.exists('data/images/flood')
    assert os.path.exists('data/images/no_flood')
    flood_imgs = os.listdir('data/images/flood')
    assert len(flood_imgs) == 5

def test_ml_prediction():
    # Only test if model is built, to keep test fast. 
    # Or just mock the prediction. Let's do a basic import test.
    from ml_model import predict_ml
    assert callable(predict_ml)

def test_dl_prediction():
    from dl_model import predict_dl
    assert callable(predict_dl)

def test_qml_prediction():
    from qml_model import predict_qml
    assert callable(predict_qml)
