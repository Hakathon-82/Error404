import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model', 'weather_model.pkl')
with open(model_path, 'rb') as f:
    weather_model = pickle.load(f)

def predict_weather(features):
    """
    Predict weather based on input features.
    :param features: list of input values [temperature, humidity, ...]
    :return: prediction result
    """
    prediction = weather_model.predict([features])
    return prediction