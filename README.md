# Veracity AI - Fake Social Media Detection Suite

Veracity AI is a machine learning based system designed to classify social media accounts as authentic or fraudulent.

The system focuses on behavioral and structural account information instead of relying primarily on post content or text analysis. It analyzes characteristics such as follower count, following count, account age, post volume, spam comment activity, and biography length to identify patterns associated with fake accounts.

The project uses Recursive Feature Elimination (RFE) for feature selection and a Random Forest Classifier as the final prediction model. A Flask-based web interface is also included for real-time account classification.

## Project Objectives

The main objectives of the project are:

- Develop a machine learning system for classifying social media accounts as Real or Fake.
- Apply feature selection to identify the most important account characteristics.
- Compare multiple machine learning classification algorithms.
- Select the best-performing model for deployment.
- Develop a web interface for real-time prediction.
- Provide visual analysis of account behavior and model performance.

## Methodology

The machine learning workflow consists of the following stages:

```text
Raw Data
   |
   v
Data Preprocessing
   |
   v
Feature Scaling
   |
   v
Recursive Feature Elimination (RFE)
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
Random Forest Selection
   |
   v
Flask Web Application
   |
   v
Real/Fake Prediction
