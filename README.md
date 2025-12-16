# Air Quality Forecasting System (ML Project)

## Overview
An end-to-end machine learning system for real-time air quality monitoring (but trained on historical data) and short-term AQI forecasting using OpenWeather APIs.

## Features
- City geocoding via API
- Real-time pollution logging (15-minute interval)
- Historical pollution data extraction (90 days)
- Exploratory data analysis and visualization
- Leakage-free AQI forecasting (1–6 hours ahead)
- Health risk classification based on predicted AQI

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- OpenWeather API

## Project Structure
AirQualityProject/
├── data/
│ ├── raw/
│ │ ├── pollution_log.csv
│ │ └── pollution_history.csv
│ └── processed/
│ └── cleaned_history_data.csv
├── src/
│ ├── api/
│ │ ├── get_coordinates.py
│ │ ├── fetch_pollution.py
│ │ └── fetch_pollution_history.py
│ └── logging_script/
│ └── continuous_logger.py
├── dashboards/
│ └── pollution_dashboard.ipynb
└── README.md


## Modeling Approach
- Random Forest Regressor
- Time-aware train-test split
- Forecast horizons: 1h, 3h, 6h
- Evaluation using MAE, RMSE, R²

## Results
| Horizon | MAE | RMSE | R² |
|-------|-----|------|----|
| 1h | 0.086 | 0.206 | 0.489 |
| 3h | 0.098 | 0.244 | 0.284 |
| 6h | 0.165 | 0.364 | -0.591 |

## Key Insights
- PM2.5 and PM10 are dominant AQI drivers
- AQI peaks during night and early morning
- Short-term AQI forecasting is feasible without weather data

## Future Work
- Incorporate meteorological features
- LSTM-based temporal modeling
- Web dashboard deployment
