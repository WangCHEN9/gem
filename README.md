# Give Everybody MachineLearning

---

An End-to-End Machine Learning Web Application for Classification and Regression problem. Supported for csv and excel files. The application relies on these two excellent libraries for
machine learning:

- streamlit: https://github.com/streamlit/streamlit
- pycaret: https://github.com/pycaret/pycaret

---

## Features

1. Drap and drop file from local system for training.

2. Simple Data Exploration.

3. Many Preprocessing methods:

   - Sample and Split
   - Data Preprocessing (Missing Values Imputation, One Hot Encoding, Handle Unknown Levels, Fix Imbalance for Classification)
   - Scale and Transform (Normalization, Transformation, Target Transformation)
   - Feature Engineering (Feature Interaction, Polynomial Features, Trigonometry Features, Group Features, Bin Numeric Features, Combine Rare Levels)
   - Feature Selection (Feature Importance, Remove Multicollinearity, Principal Components Analysis, Ignore Variances)
   - Unsupervised (Create Clusters, Remove Outliers)

4. Model Training:

   - Compare all available Machine Learning Algorithm automatically.
   - Train a selected single model
   - Train an ensemble model
   - Hyperparameter tuning for single model

5. Model Result Visualization:

   - All plots for Regression and Classification
   - SHAP Value

<!-- 6. Prediction and Save Model:

   - Online Prediction
   - Batch Prediction
   - Save whole Machine Learning Pipeline as pickle file -->

---

## Install and Run

1. Clone the repository to you computer:

```shell script
git clone https://github.com/redcican/pycaret-eidodata.git
cd pycaret-eidodata
```

2. Creata a conda virtual or python virtual environment and then activate it.

```shell script
conda create -n myvirtual-name python=3.8 -y
conda activate myvirtual-name
```

3. Install requirements

```shell script
pip install -r requirements.txt
```

4. Run streamlit locally and start web service:

```shell script
streamlit run app.py
```

---
