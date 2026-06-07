# 🎓 Student Performance Predictor

A machine learning web app that predicts a student's final grade (G3) based on academic history, lifestyle, and behavioral features — built end-to-end from raw data to deployed API.

---

## 🚀 Live Demo
👉 [student-performance-predictor.onrender.com](https://student-performance-predictor.onrender.com/app)

---

## 📸 Preview

> *(Add a screenshot of your UI here)*

---

## 🧠 What It Does

Enter a student's details — previous grades, study time, absences, alcohol consumption, family relations — and the model predicts their final exam grade out of 20.

Built on the **UCI Student Performance Dataset** (Math course, 395 students).

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| ML Model | Random Forest Regressor (sklearn) |
| Backend API | FastAPI + Uvicorn |
| Frontend | HTML, CSS, Vanilla JS |
| Deployment | Render |
| Data Analysis | Pandas, NumPy, Matplotlib, Seaborn |

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| R² Score | 0.85 |
| RMSE | 1.74 |

> Model explains **85% of variance** in final student grades.

---

## 🏗️ Project Structure

```
student-performance-predictor/
├── main.py                 # FastAPI backend
├── index.html              # Frontend UI
├── student_model.pkl       # Trained Random Forest model
├── requirements.txt        # Dependencies
└── Student_EDA.ipynb       # Full EDA + model training notebook
```

---

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/Mukilkani23/student-performance-predictor.git
cd student-performance-predictor

# Install dependencies
pip install -r requirements.txt

# Start the server
python -m uvicorn main:app --reload

# Open in browser
http://127.0.0.1:8000/app
```

---

## 🔌 API Usage

**POST** `/predict`

```json
{
  "G1": 14,
  "G2": 15,
  "age": 17,
  "studytime": 3,
  "failures": 0,
  "absences": 2,
  "famrel": 4,
  "freetime": 2,
  "goout": 2,
  "Dalc": 1,
  "Walc": 1,
  "health": 5
}
```

**Response:**
```json
{
  "predicted_G3": 15.4,
  "message": "Predicted final grade is 15.4 out of 20"
}
```

---

## 📚 ML Concepts Applied

- Exploratory Data Analysis (EDA)
- Feature Selection & Engineering
- Train/Test Split
- Linear Regression vs Random Forest comparison
- Model Evaluation (RMSE, R²)
- Model serialization with joblib
- REST API with FastAPI
- End-to-end deployment

---

## 👨‍💻 Author

**Mukilkani** — BE CSE Student | Aspiring ML Engineer  
📍 Tamil Nadu, India  
🔗 [GitHub](https://github.com/Mukilkani23)

---

## ⭐ If this helped you, drop a star!
