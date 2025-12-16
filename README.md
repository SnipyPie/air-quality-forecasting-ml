# Air Quality Forecasting using Machine Learning

## Overview
This project implements an end-to-end air quality monitoring and forecasting system using both historical and real-time air pollution data. The system collects pollution data via OpenWeather APIs, performs feature engineering, trains multiple machine learning models, compares their performance, and deploys the best-performing model for short-term AQI prediction.

The project focuses on predicting **AQI one hour ahead** using pollutant concentration trends and temporal features.

---

## Objectives
- Collect real-time air pollution data at 15-minute intervals
- Extract historical pollution data for model training
- Perform feature engineering on pollutant and time-based features
- Train and compare multiple ML models
- Deploy the best model for real-time AQI forecasting
- Validate predictions using live incoming data

---

## Data Sources
- **OpenWeather Geocoding API** – for city coordinates
- **OpenWeather Air Pollution API** – for AQI and pollutant data

Pollutants used:
- PM2.5
- PM10
- NO₂
- SO₂
- O₃

---

## Feature Engineering
The following features were used:
- Pollutant concentrations (PM2.5, PM10, NO₂, SO₂, O₃)
- Rolling averages (3-step moving average) for PM2.5 and PM10
- Time-based features:
  - Hour of day
  - Day of week

Target variable:
- **AQI shifted by 1 hour (aqi_future_1h)** to avoid data leakage

---

## Machine Learning Models Used

Three models were trained and evaluated using the same dataset and features:

### 1. Linear Regression (Baseline)
Used to establish a baseline and test linear assumptions.

### 2. Random Forest Regressor
A non-linear ensemble model capable of capturing complex pollutant interactions.

### 3. Gradient Boosting Regressor (Best Model)
An advanced ensemble model that iteratively corrects prediction errors and achieved the best performance.

---

## Model Performance Comparison (1-Hour Forecast)
| Model | MAE | RMSE | R² |
|------|-----|------|----|
| Linear Regression | 0.8191 | 1.1634 | -15.2845 |
| Random Forest | ~0.05–0.08 | ~0.14–0.20 | ~0.70 |
| Gradient Boosting | **0.0698** | **0.1515** | **0.7239** |

**Conclusion:**  
Linear Regression failed due to strong non-linear relationships in AQI data. Ensemble-based models significantly outperformed the linear baseline. Gradient Boosting achieved the best overall performance and was selected for deployment.

---

## Deployment & Real-Time Prediction
- Real-time pollution data is logged every 15 minutes
- Latest data is transformed using the same feature pipeline
- Gradient Boosting model predicts AQI 1 hour ahead
- Predictions are validated using actual AQI values collected later

---

## Project Structure
AirQualityProject/
├── dashboards/
│ └── pollution_dashboard.ipynb
├── data/
│ ├── raw/
│ └── processed/
├── models/
├── src/
│ ├── api/
│ └── logging_script/
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
