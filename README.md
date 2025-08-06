# Heart Disease Prediction Project

This project implements a machine learning pipeline for heart disease prediction using the Cleveland Heart Disease dataset. The project includes data preprocessing, feature selection, and various machine learning models to predict the presence of heart disease.

## Project Structure

```
Heart_Disease_Project/
├── data/
│   ├── cleveland.csv             # Original dataset
│   ├── cleaned_cleveland.csv     # Preprocessed dataset
│   ├── cleveland_selected_features.csv  # Dataset with selected features
│   └── Description.txt           # Dataset description
├── models/
│   └── final_model.pkl          # Trained model
├── notebooks/
│   ├── 01_data_preprocessing.ipynb      # Data cleaning and preprocessing
│   ├── 02_pca_analysis.ipynb           # Principal Component Analysis
│   ├── 03_feature_selection.ipynb      # Feature selection process
│   ├── 04_supervised_learning.ipynb    # Model training and evaluation
│   ├── 05_unsupervised_learning.ipynb  # Clustering analysis
│   └── 06_hyperparameter_tuning.ipynb  # Model optimization
└── results/                      # Model evaluation results
    └── evaluation_metrics.txt    # Detailed model performance metrics
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/rahmamohax/Heart_Disease_Project.git
cd Heart_Disease_Project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Data Processing Pipeline

1. **Data Preprocessing** (`01_data_preprocessing.ipynb`):
   - Handles missing values
   - Removes outliers
   - Validates data ranges
   - Standardizes categorical variables

2. **Feature Analysis** (`02_pca_analysis.ipynb`, `03_feature_selection.ipynb`):
   - Principal Component Analysis
   - Feature importance evaluation
   - Dimension reduction

3. **Model Development** (`04_supervised_learning.ipynb`, `06_hyperparameter_tuning.ipynb`):
   - Model training and validation
   - Hyperparameter optimization
   - Performance evaluation

4. **Additional Analysis** (`05_unsupervised_learning.ipynb`):
   - Clustering analysis
   - Pattern discovery

## Dataset Description

The Cleveland Heart Disease dataset includes various patient attributes:
- Demographic information (age, sex)
- Medical measurements (blood pressure, cholesterol)
- Test results (ECG, thallium scan)
- Target variable: Presence of heart disease (0 = no, 1 = yes)

## Dependencies

Major dependencies include:
- Python >= 3.8
- NumPy >= 1.21.0
- Pandas >= 1.3.0
- Scikit-learn >= 0.24.0
- Matplotlib >= 3.4.0
- Seaborn >= 0.11.0
- XGBoost >= 1.7.0
- Jupyter >= 1.0.0

For a complete list of dependencies, see `requirements.txt`.

## Usage

1. Start with the data preprocessing notebook:
```bash
jupyter notebook notebooks/01_data_preprocessing.ipynb
```

2. Follow the notebooks in numerical order to understand the complete analysis pipeline.

3. The final trained model is saved in `models/final_model.pkl` and can be loaded using:
```python
import joblib
model = joblib.load('models/final_model.pkl')
```

## Results

The project implements various machine learning models for heart disease prediction. The final model achieves 87% accuracy with balanced precision and recall scores. Detailed performance metrics, including model comparisons, feature importance, and cross-validation results, can be found in `results/evaluation_metrics.txt`.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


