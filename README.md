# ❤️ Heart Disease Prediction Using KNN Classification

## 📌 Project Overview

The **Heart Disease Prediction System** is a Machine Learning-based web application developed using the **K-Nearest Neighbors (KNN) Classification Algorithm**.

The main objective of this project is to predict whether a patient has heart disease or does not have heart disease based on 20 different health-related attributes.

The application provides a user-friendly interface developed using HTML and CSS, while the backend is developed using Python and Flask. The trained KNN classification model processes the patient information and generates a binary classification result.

### 🎯 Project Objectives

- Develop a machine learning model to classify heart disease.
- Use 20 health-related features for prediction.
- Convert categorical data into numerical values.
- Integrate the trained KNN model with a Flask web application.
- Provide a simple and interactive user interface.
- Display the prediction result as a binary classification.

---

## 🧠 Machine Learning Algorithm

**K-Nearest Neighbors (KNN)**

KNN is a supervised machine learning algorithm used for classification and regression problems.

In this project, KNN is used for binary classification.

The algorithm predicts the class of a new patient by identifying the nearest data points in the training dataset.

### Classification Output

| Predicted Value | Result                          |
| --------------- | ------------------------------- |
| 0               | Patient has No Heart Disease    |
| 1               | Patient is Having Heart Disease |

---

## 📊 Dataset Information

The dataset contains 20 input features related to patient health conditions and lifestyle habits.

### Dataset Features

| No. | Feature Name         | Data Type   |
| --- | -------------------- | ----------- |
| 1   | Age                  | Numerical   |
| 2   | Gender               | Categorical |
| 3   | Blood Pressure       | Numerical   |
| 4   | Cholesterol Level    | Numerical   |
| 5   | Exercise Habits      | Categorical |
| 6   | Smoking              | Categorical |
| 7   | Family Heart Disease | Categorical |
| 8   | Diabetes             | Categorical |
| 9   | BMI                  | Numerical   |
| 10  | High Blood Pressure  | Categorical |
| 11  | Low HDL Cholesterol  | Categorical |
| 12  | High LDL Cholesterol | Categorical |
| 13  | Alcohol Consumption  | Categorical |
| 14  | Stress Level         | Categorical |
| 15  | Sleep Hours          | Numerical   |
| 16  | Sugar Consumption    | Categorical |
| 17  | Triglyceride Level   | Numerical   |
| 18  | Fasting Blood Sugar  | Numerical   |
| 19  | CRP Level            | Numerical   |
| 20  | Homocysteine Level   | Numerical   |

---

## 🔄 Data Preprocessing

Categorical columns are converted into numerical values before providing the data to the machine learning model.

### 1. Gender Encoding

| Gender | Value |
| ------ | ----- |
| Female | 0     |
| Male   | 1     |

### 2. Binary Encoding

The following columns use binary encoding:

- Smoking
- Family Heart Disease
- Diabetes
- High Blood Pressure
- Low HDL Cholesterol
- High LDL Cholesterol

| Category | Value |
| -------- | ----- |
| No       | 0     |
| Yes      | 1     |

### 3. Ordinal Encoding

The following columns use ordinal encoding:

- Exercise Habits
- Alcohol Consumption
- Stress Level
- Sugar Consumption

| Category | Value |
| -------- | ----- |
| Low      | 0     |
| Medium   | 1     |
| High     | 2     |

Numerical features are collected directly through the web application.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- K-Nearest Neighbors (KNN)
- NumPy
- Pickle

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### Development Tools

- Jupyter Notebook
- VS Code
- Python Environment

---

## 📁 Project Structure

```text
Heart_Disease_Project/
│
├── app.py
│
├── KNN_Binary_Heart.pkl
│
├── README.md
│
└── templates/
    └── index.html
```

### File Description

- **app.py:** Flask backend responsible for receiving inputs and generating predictions.
- **KNN_Binary_Heart.pkl:** Saved trained KNN classification model.
- **index.html:** Frontend interface for collecting the 20 patient health features.
- **README.md:** Project documentation.

---

## ⚙️ Installation and Setup

Follow these steps to run the project on your local system.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Heart_Disease_Project
```

### Step 3: Install Required Libraries

```bash
pip install flask numpy scikit-learn
```

### Step 4: Run the Flask Application

```bash
python app.py
```

### Step 5: Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

The Heart Disease Prediction web application will open.

---

## 🔍 Working Process

The project follows the following workflow:

1. The user opens the Flask web application.
2. The frontend displays 20 health-related input fields.
3. The user enters numerical values and selects categorical options.
4. The HTML form sends the collected data to the Flask backend.
5. Flask extracts the 20 input values in the required feature order.
6. The input values are converted into a NumPy array.
7. The trained KNN model processes the input.
8. The model generates a binary classification result.
9. Flask sends the prediction result back to the HTML page.
10. The frontend displays the final classification.

---

## 💻 Prediction Results

The application generates one of the following results:

**Class 0:**

Patient has No Heart Disease.

**Class 1:**

Patient is Having Heart Disease.

---

## 🚀 Future Enhancements

- Add additional machine learning classification algorithms such as Random Forest, Decision Tree, and Logistic Regression.
- Compare the performance of different classification models.
- Improve the user interface and dashboard.
- Display model evaluation metrics such as Accuracy, Precision, Recall, and F1-Score.
- Deploy the application using cloud hosting platforms.
- Add visualizations for patient health parameters.

---

## 📌 Important Notes

- The input feature order must match the order used during model training.
- Categorical encoding must be consistent with the training dataset.
- If feature scaling was used during training, the same fitted scaler or preprocessing pipeline must be applied during prediction.
- The pickle model must be compatible with the installed Scikit-learn version.

**Disclaimer:** This project is developed for educational and machine learning demonstration purposes only. Predictions are not medical diagnoses and should not replace professional medical consultation.

---

## 👨‍💻 Project Information

**Project Name:** Heart Disease Prediction Using KNN Classification

**Domain:** Machine Learning | Healthcare | Classification

**Backend:** Python Flask

**Algorithm:** K-Nearest Neighbors (KNN)

**Input Features:** 20

**Output:** Binary Classification (0 or 1)

**Developed By:** Yashodhar

---

⭐ If you find this project useful, consider giving the repository a star!
