import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
mlflow.set_tracking_uri("file:./mlruns")

MODEL_PATH = "models/ml_rf_model.pkl"

def train_ml_model(data_path="data/dummy_tabular_data.csv"):
    """Trains a Random Forest classifier on tabular data."""
    if not os.path.exists(data_path):
        from utils import generate_dummy_tabular_data
        generate_dummy_tabular_data()
        
    df = pd.read_csv(data_path)
    X = df[['Rainfall', 'Humidity', 'Temperature', 'River_Level']]
    y = df['Flood_Risk']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    with mlflow.start_run(run_name="RandomForest_ML"):
        mlflow.log_param("n_estimators", 100)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"ML Model Accuracy: {acc:.4f}")
        
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "rf_model")
        
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")
    return model

def predict_ml(features):
    """Predicts flood risk using the trained ML model.
    features: list or numpy array of [Rainfall, Humidity, Temperature, River_Level]
    """
    if not os.path.exists(MODEL_PATH):
        train_ml_model()
    
    model = joblib.load(MODEL_PATH)
    # Return 1 for Flood, 0 for No Flood
    return int(model.predict([features])[0])

if __name__ == "__main__":
    train_ml_model()
