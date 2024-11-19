import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)

# Load the trained model
model = pickle.load(open("dtc_model.pkl", "rb"))

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input features from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Prepare data for prediction
        data = [[sepal_length, sepal_width, petal_length, petal_width]]
        result = model.predict(data)[0]  # Get the first prediction (single result)

        # Return prediction to the webpage
        return render_template("index.html", prediction_text=f"The flower species is {result}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    flask_app.run(debug=True)
