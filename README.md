# Give Everybody MachineLearning

[![Docker Image CI](https://github.com/WangCHEN9/gem/actions/workflows/docker-image.yml/badge.svg)](https://github.com/WangCHEN9/gem/actions/workflows/docker-image.yml)

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
git clone https://github.com/WangCHEN9/gem
cd gem
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

## Run on Docker

1. Pull the Docker image:

```
docker pull wangchen9/gem:latest
```

2. Run the Docker image locally:

```
docker run -p 8501:8501 wangchen9/gem
```

3. Open the localhost:8501

- [http://localhost:8501](http://localhost:8501)

## Deploy in heroku

1. Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

```
heroku login
```

2. You must have Docker set up locally to continue. You should see output when you run this command.

```
docker ps
```

3. Now you can sign into Container Registry.

```
heroku container:login
```

4. Build the Dockerfile in the current directory and push the Docker image.

```
heroku container:push web --app=g-e-m
```

5. Release the newly pushed images to deploy your app.

```
heroku container:release web

```
