# Customer-Churn-Prediction
An end-to-end data science project to predict customer churn using Python, scikit-learn, and Streamlit. This project covers data analysis, feature engineering, machine learning modeling, and web app deployment.

## 🧠 Project Objective

The goal is to build a predictive model that helps telecom businesses identify customers likely to churn based on:

- Age  
- Gender  
- Tenure (how long they've been a customer)  
- Monthly Charges  

---

## 🚀 Demo

You can run the project locally using the steps below. The app allows users to input details and instantly receive a churn prediction (`Yes` or `No`).

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── app.py                  # Streamlit app
├── model.pkl               # Trained ML model
├── Scaler.pkl              # StandardScaler object
├── customer_churn_data.csv # Sample dataset
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 📦 Tech Stack

- **Python**
- **Scikit-learn** – Model training
- **Pandas & NumPy** – Data processing
- **Streamlit** – Web app
- **Joblib** – Model and scaler serialization
- **Imbalanced-learn** – (Optional) Handling imbalanced data

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

> Or manually:
```bash
pip install pandas numpy scikit-learn streamlit joblib imbalanced-learn
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Model Inputs

| Feature          | Description                       | Type    |
|------------------|-----------------------------------|---------|
| Age              | Age of the customer               | Numeric |
| Gender           | Male or Female                    | Categorical (converted to 1/0) |
| Tenure           | Number of months as a customer    | Numeric |
| Monthly Charges  | Monthly subscription cost         | Numeric |

---

## 🧠 Model Output

- **Yes** – Customer is predicted to churn  
- **No** – Customer is predicted to stay

---

## ✅ Example Input

| Age | Gender | Tenure | Monthly Charges |
|-----|--------|--------|------------------|
| 24  | Female | 80     | 50               |

### Example Output:
> Prediction: **Yes** (Customer may churn)

---

## 📌 Notes

- Ensure `model.pkl` and `Scaler.pkl` are in the same directory as `app.py`
- Input features are scaled before prediction using the same scaler used during model training

---

## 📈 Future Improvements

- Add more features (e.g., contract type, internet service, payment method)
- Display model evaluation metrics (accuracy, precision, recall)
- Visualize data and model performance
- Deploy on **Streamlit Cloud**, **Render**, or **Heroku**

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Disha Tejnath Suryawanshi**  
📧 [Your Email]  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile)  
🌐 [Portfolio or GitHub](https://github.com/yourusername)
