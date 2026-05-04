import streamlit as st
import os
import mlflow
mlflow.set_tracking_uri("file:./mlruns")
from PIL import Image
from ml_model import predict_ml
from dl_model import predict_dl
from qml_model import predict_qml

st.set_page_config(page_title="Hybrid Flood Risk Prediction", layout="wide")

st.title("🌊 Hybrid Flood Risk Prediction System")
st.markdown("""
This system uses a hybrid approach combining **Classical Machine Learning (ML)**, 
**Deep Learning (DL)**, and **Quantum Machine Learning (QML)** to predict flood risk.
""")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Tabular Data Input")
    st.markdown("Provide environmental metrics for ML and QML models.")
    rainfall = st.slider("Rainfall (mm)", 0.0, 500.0, 150.0)
    humidity = st.slider("Humidity (%)", 30.0, 100.0, 60.0)
    temperature = st.slider("Temperature (°C)", 10.0, 45.0, 25.0)
    river_level = st.slider("River Level (m)", 1.0, 15.0, 5.0)
    
    features = [rainfall, humidity, temperature, river_level]

with col2:
    st.header("2. Image Data Input")
    st.markdown("Upload a satellite or CCTV image for the DL model.")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    image_path = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # Save temp image for DL prediction
        os.makedirs("temp", exist_ok=True)
        image_path = os.path.join("temp", "uploaded_image.jpg")
        image.save(image_path)
    else:
        st.info("Please upload an image to enable DL prediction.")

st.markdown("---")
st.header("Prediction Results")

if st.button("Predict Flood Risk", type="primary"):
    with st.spinner("Running models..."):
        # 1. ML Prediction
        ml_pred = predict_ml(features)
        ml_text = "Flood" if ml_pred == 1 else "No Flood"
        
        # 2. QML Prediction
        try:
            qml_pred = predict_qml(features)
            qml_text = "Flood" if qml_pred == 1 else "No Flood"
        except Exception as e:
            st.error(f"Error running QML Model: {e}")
            qml_pred = 0
            qml_text = "Error"

        # 3. DL Prediction
        dl_pred = 0
        dl_text = "N/A (No Image)"
        if image_path:
            dl_pred = predict_dl(image_path)
            dl_text = "Flood" if dl_pred == 1 else "No Flood"
            
        # Display individual results
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("ML Model (Random Forest)", ml_text)
        res_col2.metric("DL Model (CNN)", dl_text)
        res_col3.metric("QML Model (VQC)", qml_text)
        
        # Hybrid Fusion (Majority Voting)
        if image_path:
            total_votes = ml_pred + dl_pred + qml_pred
            hybrid_pred = 1 if total_votes >= 2 else 0
        else:
            total_votes = ml_pred + qml_pred
            hybrid_pred = 1 if total_votes >= 1 else 0 # OR logic if only 2 models
            
        st.markdown("---")
        if hybrid_pred == 1:
            st.error(f"🚨 **FINAL HYBRID PREDICTION: HIGH FLOOD RISK** (Votes: {total_votes})")
        else:
            st.success(f"✅ **FINAL HYBRID PREDICTION: LOW FLOOD RISK** (Votes: {total_votes})")

st.markdown("---")
with st.expander("📊 View MLflow Tracking Data"):
    st.markdown("Recent model training runs tracked by MLflow:")
    try:
        df_runs = mlflow.search_runs()
        if not df_runs.empty:
            # Clean up columns to show relevant info
            cols_to_show = ['tags.mlflow.runName', 'status']
            metric_cols = [c for c in df_runs.columns if c.startswith('metrics.')]
            param_cols = [c for c in df_runs.columns if c.startswith('params.')]
            
            final_cols = cols_to_show + metric_cols + param_cols
            final_cols = [c for c in final_cols if c in df_runs.columns]
            
            st.dataframe(df_runs[final_cols])
        else:
            st.info("No MLflow runs found yet. Run predictions to trigger model training.")
    except Exception as e:
        st.warning(f"Could not load MLflow tracking data: {e}")
