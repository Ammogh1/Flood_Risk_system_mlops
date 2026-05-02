import traceback
import sys

def test():
    try:
        from qml_model import predict_qml
        features = [150.0, 60.0, 25.0, 5.0]
        print("Calling predict_qml...")
        qml_pred = predict_qml(features)
        print(f"Success! Prediction is: {qml_pred}")
    except Exception as e:
        print("Error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    test()
