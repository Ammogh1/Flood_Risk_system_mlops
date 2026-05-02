# Software Requirements Specification (SRS)
**Hybrid Flood Risk Prediction System**

## 1. Introduction
### 1.1 Purpose
The primary objective of this Software Requirements Specification (SRS) is to detail the functional and non-functional prerequisites of the Hybrid Flood Risk Prediction System. This software solution integrates classical Machine Learning (ML), Deep Learning (DL), and advanced Quantum Machine Learning (QML) methodologies to accurately evaluate and forecast the likelihood of flood events based on diverse user-provided datasets.

### 1.2 Scope
This platform operates as an interactive web-based application enabling users to:
- Submit environmental metrics (tabular data) and geographical images.
- Obtain real-time flood risk assessments from three distinct computational paradigms.
- Review a synthesized "Hybrid Prediction" derived from a majority voting algorithm.

The core architecture encompasses:
- A Streamlit-powered graphical user interface.
- Backend processing scripts for ML, DL, and QML inference.
- An automated data pipeline for seamless setup and dummy data generation.

### 1.3 Definitions, Acronyms, Abbreviations
- **ML**: Machine Learning (Classical approaches like Random Forest)
- **DL**: Deep Learning (Neural networks, e.g., CNN)
- **QML**: Quantum Machine Learning (Quantum-assisted algorithms)
- **VQC**: Variational Quantum Classifier
- **CNN**: Convolutional Neural Network
- **UI**: User Interface

### 1.4 References
- Project Architecture Blueprint
- Data Generation Utility Documentation
- IEEE 830-1998 Software Standards

---

## 2. Overall Description
### 2.1 Product Perspective
The application functions as an independent, fully containerized web utility constructed with:
- A Streamlit frontend framework.
- Independent modeling modules (`ml_model.py`, `dl_model.py`, `qml_model.py`).
- Pre-configured Docker and Kubernetes deployment environments.

### 2.2 Product Functions
The application is designed to:
- Capture numerical environmental data via interactive sliders.
- Ingest satellite or CCTV imagery through file uploads.
- Route data to appropriate analytical models.
- Generate independent binary classifications (Flood / No Flood).
- Aggregate the individual model outputs to establish a final, conclusive risk level.

### 2.3 User Classes and Characteristics
- **Environmental Researchers/Analysts**: Utilize the tool to test data against varied predictive models.
- **General Public**: Input local conditions to gauge immediate environmental threats.
- **System Administrators**: Manage deployment, monitor Kubernetes clusters, and update model parameters.

### 2.4 Operating Environment
- **Browser Compatibility**: Modern web browsers (Chrome, Firefox, Safari, Edge).
- **Runtime Environment**: Python 3.10+
- **Core Frameworks**: Streamlit, PyTorch, Scikit-learn, Qiskit.

### 2.5 Constraints
- Quantum simulation speed is limited by classical hardware capabilities.
- Deep Learning accuracy is highly dependent on the quality and resolution of uploaded imagery.

### 2.6 Assumptions and Dependencies
- It is assumed that the Python runtime has sufficient memory to cache the QML models globally.
- The system depends on the successful installation of all packages detailed in `requirements.txt`.

---

## 3. System Features
### 3.1 User Interface
- A responsive, dual-column dashboard.
- Real-time parameter adjustment tools (sliders).
- Clear, distinct metric cards for displaying individual model results.

### 3.2 Input Validation
- Hardcoded min/max boundaries for environmental metrics (e.g., Rainfall capped at 500mm).
- Restrictions on file uploads to only accept specific image formats (JPG, PNG, JPEG).

### 3.3 Prediction Modules
- **Classical ML**: Evaluates tabular data using a Random Forest classifier.
- **Deep Learning**: Analyzes spatial image features utilizing a PyTorch CNN.
- **Quantum ML**: Processes normalized tabular data through a simulated Qiskit Variational Quantum Classifier.

### 3.4 Aggregated Result Display
- A logic-based voting system that calculates total positive alerts.
- Dynamic color-coded alerts (Green for safe, Red for high risk).

---

## 4. External Interface Requirements
### 4.1 User Interface
The UI must be web-accessible, intuitive, and require zero command-line interaction from the end-user. It should visually separate tabular data inputs from image uploads.

### 4.2 Software Interface
- The system requires internal integration between the Streamlit event loop and the Python modeling scripts.
- Interoperability with the host OS filesystem for reading/writing temporary image uploads.

### 4.3 Hardware Interface
Minimum recommended specifications:
- 8GB RAM (To accommodate in-memory QML caching).
- Multi-core CPU to handle concurrent Qiskit simulations and PyTorch inference.

---

## 5. Functional Requirements
| ID | Requirement Description |
|---|---|
| FR1 | The system shall render the primary Streamlit dashboard upon launch. |
| FR2 | The system shall auto-generate foundational dummy datasets if none exist locally. |
| FR3 | The system shall enforce defined numeric ranges on all tabular input sliders. |
| FR4 | The system shall accept and temporarily store user-uploaded image files. |
| FR5 | The system shall compute independent binary predictions across ML, DL, and QML models. |
| FR6 | The system shall calculate a final hybrid prediction using an OR logic gate (2 models) or Majority Voting (3 models). |
| FR7 | The system shall clearly present the individual voting breakdown to the user. |

---

## 6. Non-Functional Requirements
### 6.1 Performance
- Classical and DL predictions must execute in under 3 seconds.
- Initial QML training (cached) may take up to 45 seconds, but subsequent predictions must resolve instantly.

### 6.2 Reliability
- The system must consistently handle missing image uploads gracefully by adjusting its voting logic dynamically.

### 6.3 Usability
- The interface must remain uncluttered, providing immediate visual feedback during computation phases (via loading spinners).

### 6.4 Maintainability
- The codebase must strictly separate concerns: UI logic (`app.py`), individual model training/inference scripts, and data utilities (`utils.py`).

### 6.5 Security
- The Streamlit framework shall inherently sanitize inputs to prevent injection attacks. Temporary files must be managed safely.

---

## 7. System Risks
- **Simulation Timeouts**: Potential delays caused by complex quantum circuit simulations on low-end hardware.
- **Dependency Conflicts**: Risk of library version clashes (e.g., Qiskit updates) requiring strict environment management.
- **False Positives**: The cautious OR-logic (when images are omitted) may lead to over-reporting of flood risks.

---

## 8. Test Requirements
- **Unit Testing**: Validating the mathematical output of `utils.py` and model shape outputs.
- **Functional Testing**: Verifying the Streamlit UI elements interact correctly with the backend state.
- **Integration Testing**: Ensuring the majority voting logic accurately reflects the combined model outputs.

---

## 9. Acceptance Criteria
- The application successfully launches without fatal Python exceptions.
- The hybrid logic correctly aggregates a "Flood" decision when the prerequisite number of models flag a risk.
- The system smoothly handles the absence of an image upload without crashing.

---

## 10. Project Schedule
| Phase | Estimated Duration |
|---|---|
| Requirement Structuring | 2 Days |
| UI & Logic Design | 3 Days |
| Model Integration Testing | 4 Days |
| Optimization & Bug Fixing | 3 Days |
| Final Verification | 2 Days |

---

## 11. Conclusion
The Hybrid Flood Risk Prediction System is a state-of-the-art implementation that bridges classical machine learning, deep neural networks, and experimental quantum algorithms. By synthesizing these technologies into a single, cohesive web application, it provides a robust, fail-safe environment for risk assessment modeling.
