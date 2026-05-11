from app.inference.predict import predict_aqi


def get_prediction(city: str):
    prediction = predict_aqi(city)

    return {
        "city": city,
        "predicted_aqi_1h": float(prediction)
    }