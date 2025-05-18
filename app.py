import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('archive (1)/creditcard.csv')
    return df

df = load_data()

# Prepare data
X = df.drop(['Class', 'Time'], axis=1)
y = df['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model (for demo; in production, load a pre-trained model)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

st.title("Credit Card Fraud Detection")

st.write("Enter transaction details to predict if it's fraudulent:")

# Dynamically create input fields for each feature except 'Time'
user_input = {}
for col in X.columns:
    user_input[col] = st.number_input(col, value=float(X[col].mean()))

# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ Likely Fraudulent Transaction!")
    else:
        st.success("✅ Transaction appears legitimate.")
