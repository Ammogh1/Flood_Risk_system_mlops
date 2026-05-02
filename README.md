# Hybrid Flood Risk Prediction System

This project implements an end-to-end Full Stack AI system for predicting flood risks. It uses a hybrid approach, combining:
1. **Classical Machine Learning (ML):** Random Forest
2. **Deep Learning (DL):** Convolutional Neural Network (PyTorch)
3. **Quantum Machine Learning (QML):** Variational Quantum Classifier (Qiskit)

The frontend is built using **Streamlit**, providing an intuitive interface for both tabular and image inputs.

## Project Structure
```text
project/
├── app.py                  # Streamlit application
├── ml_model.py             # Random Forest model training & inference
├── dl_model.py             # PyTorch CNN model training & inference
├── qml_model.py            # Qiskit VQC model training & inference
├── utils.py                # Data generation and utilities
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker configuration
├── k8s-deployment.yaml     # Kubernetes deployment configuration
├── .pylintrc               # Linting configuration
├── .github/workflows/      # CI/CD pipeline
├── docs/                   # Documentation (SRS, TestPlan)
└── tests/                  # Unit tests
```

## Setup Instructions

### 1. Local Environment
1. Clone the repository or navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
   *Note: On the first run, the system will automatically generate dummy datasets (tabular and image) and train the ML, DL, and QML models. The QML model might take a minute to train on the simulator.*

### 2. Docker
1. Build the Docker image:
   ```bash
   docker build -t flood-risk-app .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8501:8501 flood-risk-app
   ```
3. To push to Docker Hub:
   ```bash
   docker tag flood-risk-app yourdockerhubusername/flood-risk-app:latest
   docker push yourdockerhubusername/flood-risk-app:latest
   ```

### 3. Kubernetes
Apply the deployment file to your local or cloud Kubernetes cluster:
```bash
kubectl apply -f k8s-deployment.yaml
kubectl get pods
kubectl get services
```

## DevOps & MLOps Integration

- **CI/CD:** A GitHub Actions workflow (`.github/workflows/ci.yml`) is provided for automated linting (pylint) and testing (pytest).
- **Git/GitHub:** Initialize Git (`git init`), add files, commit, and push to your remote repository to trigger the CI pipeline.
- **MLflow Tracking (Optional):** You can integrate MLflow by running `mlflow server` and adding tracking code in `train_*_model()` functions.
- **DVC (Optional):** Use Data Version Control to track the `data/` folder:
  ```bash
  dvc init
  dvc add data/
  git add data.dvc .gitignore
  ```

## Documentation
- Read the [Software Requirements Specification (SRS)](docs/SRS.md) for detailed requirements and architecture.
- Read the [Test Plan](docs/TestPlan.md) for the testing strategy.
"# Flood_Risk_system_mlops" 
