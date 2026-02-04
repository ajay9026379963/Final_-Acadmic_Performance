import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('final_Examscore_model.pkl')
st.title('Exam Score Prediction App')

# Input fields with unique keys and proper labels
attendance = st.number_input('Enter the attendance percentage', min_value=0, max_value=100, key="attendance")
internal_test1 = st.number_input('Enter Internal Test 1 score (out of 40)', min_value=0, max_value=40, key="test1")
internal_test2 = st.number_input('Enter Internal Test 2 score (out of 40)', min_value=0, max_value=40, key="test2")
assignments = st.number_input('Enter assignment score (out of 10)', min_value=0, max_value=10, key="assignments")
study_hours = st.number_input('Enter daily study hours', min_value=0, max_value=24, key="study_hours")

# Predict button
if st.button('Predict Exam Score'):
    # Create input data with EXACT column names that match the trained model
    input_data = pd.DataFrame({
        'Attendance (%)': [attendance],
        'Internal Test 1 (out of 40)': [internal_test1],
        'Internal Test 2 (out of 40)': [internal_test2],
        'Assignment Score (out of 10)': [assignments],
        'Daily Study Hours': [study_hours]
    })
    
    # Predict
    try:
        prediction = model.predict(input_data)[0]
        st.success(f'The predicted exam score is: {prediction:.2f}')
    except Exception as e:
        st.error(f'Prediction error: {str(e)}')