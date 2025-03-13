# ML Intern Task - Hyperspectral Imaging and Mycotoxin Prediction

## Objective
Process hyperspectral imaging data, perform dimensionality reduction, and develop a machine learning model to predict mycotoxin levels (DON concentration) in corn samples.

## Repository Structure
- `.ipynb_checkpoints/` 
- `TASK-ML-INTERN.csv/` 
- `app.py/` 
- `don_prediction_model.pkl/` 
- `scaler.pkl` 
- `vomitoxin_ppb.ipynb` 
## Features & Workflow
### 1. Data Exploration and Preprocessing
- Handle missing values and normalize spectral data.
- Visualize spectral bands.

### 2. Dimensionality Reduction
- Apply PCA or t-SNE for feature reduction.
- Visualize reduced feature space.

### 3. Model Training
- Train a deep learning model (CNN/GNN/LSTM).
- Optimize hyperparameters.

### 4. Model Evaluation
- Evaluate with MAE, RMSE, and R² score.
- Generate actual vs. predicted value plots.

## Deliverables
- **Jupyter Notebooks**: Code implementation.
- **Short Report**: Summary of preprocessing, modeling, and key findings.
- **Trained Model**: Saved checkpoint.

## Bonus Features (Optional)
- Implement attention mechanism or transformer-based model.
- Develop a Streamlit app for interactive predictions.

## Evaluation Criteria
- **Code Quality (30%)**: Organized and documented.
- **EDA & Visualization (25%)**: Clear data exploration.
- **Model Performance (25%)**: Well-chosen model and evaluation.
- **Interpretability (20%)**: Meaningful insights and improvements.

