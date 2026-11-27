
import pickle
from flask import Flask, render_template, request
import numpy as np

# Load KNN Heart Disease Classification Model
with open("KNN_Binary_Heart.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)


@app.route("/")
def fun():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction():

    try:
        # Extract all 20 input features

        age = float(request.form["age"])
        gender = float(request.form["gender"])
        blood_pressure = float(request.form["blood_pressure"])
        cholesterol = float(request.form["cholesterol"])
        exercise = float(request.form["exercise"])
        smoking = float(request.form["smoking"])
        family_heart = float(request.form["family_heart"])
        diabetes = float(request.form["diabetes"])
        bmi = float(request.form["bmi"])
        high_bp = float(request.form["high_bp"])
        low_hdl = float(request.form["low_hdl"])
        high_ldl = float(request.form["high_ldl"])
        alcohol = float(request.form["alcohol"])
        stress = float(request.form["stress"])
        sleep = float(request.form["sleep"])
        sugar = float(request.form["sugar"])
        triglyceride = float(request.form["triglyceride"])
        fasting_sugar = float(request.form["fasting_sugar"])
        crp = float(request.form["crp"])
        homocysteine = float(request.form["homocysteine"])

        # Arrange features in the exact training order
        features = np.array([[
            age,
            gender,
            blood_pressure,
            cholesterol,
            exercise,
            smoking,
            family_heart,
            diabetes,
            bmi,
            high_bp,
            low_hdl,
            high_ldl,
            alcohol,
            stress,
            sleep,
            sugar,
            triglyceride,
            fasting_sugar,
            crp,
            homocysteine
        ]])

        # Predict using KNN model
        prediction_result = model.predict(features)[0]

        # Classification result
        if int(prediction_result) == 0:
            result = "Patient has No Heart Disease"
        elif int(prediction_result) == 1:
            result = "Patient is Having Heart Disease"
        else:
            result = "Unexpected prediction result"

        return render_template(
            "index.html",
            prediction_text=result
        )

    except (ValueError, KeyError):
        return render_template(
            "index.html",
            prediction_text="Please enter valid values in all fields."
        )


if __name__ == "__main__":
    app.run(debug=True)
