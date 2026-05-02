import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.algorithms import VQC
from qiskit_algorithms.optimizers import COBYLA

_GLOBAL_QML_MODEL = None
_GLOBAL_SCALER = None

def get_qml_model_and_scaler(data_path="data/dummy_tabular_data.csv", num_samples=100):
    """Trains a Variational Quantum Classifier (VQC) and caches it in memory.
    Bypasses serialization bugs in Qiskit 1.x by keeping the model in RAM.
    """
    global _GLOBAL_QML_MODEL, _GLOBAL_SCALER
    if _GLOBAL_QML_MODEL is not None:
        return _GLOBAL_QML_MODEL, _GLOBAL_SCALER

    if not os.path.exists(data_path):
        from utils import generate_dummy_tabular_data
        generate_dummy_tabular_data()
        
    df = pd.read_csv(data_path)
    
    # Take a smaller sample for faster training
    df_sample = df.sample(n=num_samples, random_state=42)
    
    X = df_sample[['Rainfall', 'Humidity', 'Temperature', 'River_Level']].values
    y = df_sample['Flood_Risk'].values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    num_features = X.shape[1]
    feature_map = ZZFeatureMap(feature_dimension=num_features, reps=1)
    ansatz = RealAmplitudes(num_qubits=num_features, reps=1)
    optimizer = COBYLA(maxiter=40)
    
    vqc = VQC(
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=optimizer,
    )
    
    print("Training QML model in memory. This may take a moment...")
    vqc.fit(X_train, y_train)
    
    acc = vqc.score(X_test, y_test)
    print(f"QML Model Accuracy: {acc:.4f}")
    
    _GLOBAL_QML_MODEL = vqc
    _GLOBAL_SCALER = scaler
    return vqc, scaler

def predict_qml(features):
    """Predicts flood risk using the trained QML model.
    features: list or numpy array of [Rainfall, Humidity, Temperature, River_Level]
    """
    # This will train it once and then reuse the cached object
    vqc, scaler = get_qml_model_and_scaler()
        
    features_scaled = scaler.transform([features])
    prediction = vqc.predict(features_scaled)
    
    # Extract prediction value correctly whether it's 0-D or 1-D array
    val = prediction[0] if prediction.ndim > 0 else prediction
    return int(val)

if __name__ == "__main__":
    get_qml_model_and_scaler()
