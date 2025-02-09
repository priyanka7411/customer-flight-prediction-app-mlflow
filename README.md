# Flight Price and Customer Satisfaction Prediction

## Overview

This repository contains two machine learning projects:

1. **Flight Price Prediction (Regression)**
2. **Customer Satisfaction Prediction (Classification)**

Both projects focus on building machine learning models using Python, Streamlit, and MLflow for tracking experiments. The models are deployed in interactive web apps that allow users to input relevant information and get real-time predictions.

---

## Project 1: Flight Price Prediction

### Problem Statement
This project aims to predict flight ticket prices based on factors like departure time, source, destination, and airline type. The goal is to develop a regression model and deploy it as a Streamlit app that allows users to input filters and get a predicted flight price.

### Approach

#### 1. Data Preprocessing
- Cleaned the dataset by removing duplicates and handling missing values.
- Converted date and time columns into standard formats.
- Feature engineering to derive new features like flight duration and price per minute.

#### 2. Model Building
- Performed Exploratory Data Analysis (EDA) to identify trends and correlations.
- Trained regression models like **Linear Regression**, **Random Forest**, and **Gradient Boosting**.
- Tuning of **Gradient Boosting Regressor** achieved:
  - **RMSE**: 1809.13
  - **R2**: 0.8454

#### 3. MLflow Integration
- Logged experiments, hyperparameters, and metrics (e.g., RMSE, R2).
- Tracked all models in MLflow's model registry for easy access and comparison.

#### 4. Streamlit App
The Streamlit app allows users to:
- Filter flights by route, time, and airline.
- Get a real-time prediction of flight prices.

#### Screenshot
![Flight Price Prediction App](https://github.com/priyanka7411/customer-flight-prediction-app-mlflow/blob/main/screencapture-localhost-8512-2025-02-09-13_01_59.png)

---

## Project 2: Customer Satisfaction Prediction

### Problem Statement
This project focuses on predicting customer satisfaction levels based on features such as demographics, flight services, and feedback ratings. The goal is to build a classification model and deploy it as a Streamlit app that predicts whether a customer is satisfied or dissatisfied.

### Approach

#### 1. Data Preprocessing
- Cleaned the dataset by handling missing values and duplicates.
- Encoded categorical variables and standardized numerical features.

#### 2. Model Building
- Performed EDA to understand feature relationships and trends.
- Trained classification models like **Logistic Regression**, **Random Forest**, and **Gradient Boosting**.
- The **Best Random Forest Model** achieved:
  - **Accuracy**: 0.9626
  - **F1-Score**: 0.9564

#### 3. MLflow Integration
- Logged experiments, metrics (e.g., accuracy, F1-score), and confusion matrices.
- Tracked all models in MLflow for versioning and performance tracking.

#### 4. Streamlit App
The Streamlit app allows users to:
- Input customer demographics, travel preferences, and service ratings.
- Get a prediction of customer satisfaction levels.

#### Screenshot
![Customer Satisfaction Prediction App](https://github.com/priyanka7411/customer-flight-prediction-app-mlflow/blob/main/screencapture-localhost-8512-2025-02-09-13_01_29.png)
![Customer Satisfaction Prediction App]()

---

## Skills Takeaway

- **Python**: Data cleaning, feature engineering, and machine learning implementation.
- **Streamlit**: Developed interactive web applications for real-time predictions.
- **MLflow**: Tracked and logged model performance, hyperparameters, and artifacts.
- **Machine Learning**: Regression models for flight prices, classification models for customer satisfaction.

---

## Datasets

### Flight Price Prediction
Dataset includes:
- Airline
- Date of Journey
- Source and Destination
- Route
- Departure and Arrival Time
- Duration
- Number of Stops
- Additional Information



### Customer Satisfaction Prediction
Dataset includes:
- Gender, Age, and Customer Type
- Flight Distance
- Service Ratings (e.g., Inflight Wi-Fi, Seat Comfort)
- Delay Information
- Overall Satisfaction



---

## How to Run the App Locally

1. Clone the repository.
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

   streamlit run app.py



