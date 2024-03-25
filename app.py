#pip install joblib

import streamlit as st
import joblib

# Load the model
model = joblib.load('Fastag_Fraud_Detection_Model')
st.image("2.jpg")
# Streamlit app
st.title('Decoding Fastag Fraud')
st.markdown('## A Detection Approach by Naveen')
# Input fields
transaction_amount = st.number_input('Transaction Amount', value=0)
amount_paid = st.number_input('Amount Paid', value=0)
vehicle_speed = st.number_input('Vehicle Speed', value=0)
hour = st.number_input('Hour', value=0)
day = st.number_input('Day', value=0)
month = st.number_input('Month', value=0)
amount_difference = st.number_input('Amount Difference', value=transaction_amount-amount_paid)
payment_ratio = st.number_input('Payment Ratio', value=0)
vehicle_type_bus = st.checkbox('Vehicle Type Bus')
vehicle_type_car = st.checkbox('Vehicle Type Car')
vehicle_type_motorcycle = st.checkbox('Vehicle Type Motorcycle')
vehicle_type_suv = st.checkbox('Vehicle Type SUV')
vehicle_type_sedan = st.checkbox('Vehicle Type Sedan')
vehicle_type_truck = st.checkbox('Vehicle Type Truck')
vehicle_type_van = st.checkbox('Vehicle Type Van')
lane_type_express = st.checkbox('Lane Type Express')
lane_type_regular = st.checkbox('Lane Type Regular')
vehicle_dimensions_large = st.checkbox('Vehicle Dimensions Large')
vehicle_dimensions_medium = st.checkbox('Vehicle Dimensions Medium')
vehicle_dimensions_small = st.checkbox('Vehicle Dimensions Small')
latitude = st.number_input('Latitude', value=0.0)
longitude = st.number_input('Longitude', value=0.0)

# Prediction
if st.button('Predict'):
    prediction = model.predict([[transaction_amount, amount_paid, vehicle_speed, hour, day, month,
                                  amount_difference, payment_ratio, vehicle_type_bus, vehicle_type_car,
                                  vehicle_type_motorcycle, vehicle_type_suv, vehicle_type_sedan,
                                  vehicle_type_truck, vehicle_type_van, lane_type_express,
                                  lane_type_regular, vehicle_dimensions_large, vehicle_dimensions_medium,
                                  vehicle_dimensions_small, latitude, longitude]])

    if prediction[0] == 0:
        st.error('Fraud Detected')
    else:
        st.success('Not Fraud')
        
#st.image("2.jpg")

#st.markdown(background_html, unsafe_allow_html=True)


