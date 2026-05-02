# Test Plan

## 1. Unit Testing Strategy
Unit tests are implemented using `pytest`. The strategy involves:
- Testing data generation utilities to ensure inputs are formatted correctly.
- Testing the availability and structural correctness of model prediction functions.
- Mocking complex model inferences if needed to speed up CI/CD pipelines.

## 2. Functional Testing
Functional testing will be conducted manually through the Streamlit interface:
1. **Form Validation:** Verify sliders accept expected ranges.
2. **Image Upload:** Verify image preview renders correctly.
3. **Prediction Execution:** Verify clicking "Predict" yields four distinct outputs (ML, DL, QML, Hybrid).

## 3. Sample Test Cases

| Test ID | Description | Input Data | Expected Output | Status |
|---|---|---|---|---|
| TC01 | Generate Tabular Data | `num_samples=10` | CSV file created with 10 rows | Passed |
| TC02 | Generate Images | `num_samples=10` | 10 images generated in proper folders | Passed |
| TC03 | Test ML Model | `[150, 60, 25, 5]` | Binary classification (0 or 1) | Passed |
| TC04 | Test DL Model | Dummy image | Binary classification (0 or 1) | Passed |
| TC05 | Test QML Model | `[150, 60, 25, 5]` | Binary classification (0 or 1) | Passed |
| TC06 | Hybrid Fusion (Image + Tabular) | `[150, 60, 25, 5]`, Image | Voting output correctly aggregates sub-models | Passed |

## 4. Test Execution Summary
- **Total Test Cases Designed:** 6
- **Test Cases Executed:** 6
- **Test Cases Passed:** 6
- **Test Cases Failed:** 0
- **Success Rate:** 100%
