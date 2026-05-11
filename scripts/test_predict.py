from app.inference.predict import predict_aqi

result = predict_aqi("Delhi")

print("Predicted AQI (1 hour ahead):", result)