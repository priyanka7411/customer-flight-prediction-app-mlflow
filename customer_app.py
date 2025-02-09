import pandas as pd
import streamlit as st
import mlflow.sklearn
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def customer_satisfaction_prediction():

    # Custom CSS for gradient background and improving UI
    st.markdown("""
        <style>
            body {
                background: linear-gradient(135deg, #0066cc, #00b3e6); /* Gradient from blue to light blue */
                font-family: 'Arial', sans-serif;
                color: white;
            }
            .css-1v3fvcr {
                background-color: rgba(0, 102, 204, 0.8);  /* Apply transparent blue background */
                color: white;
                font-size: 20px;
            }
            .stButton>button {
                background-color: #0066cc;
                color: white;
                font-size: 16px;
            }
            .stInput>input {
                font-size: 18px;
            }
            .stSelectbox>div {
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Cache model loading for performance improvement
    @st.cache_resource
    def load_model():
        model_uri = 'runs:/90e43c8d4ded4b88bff19588c7e9225c/random_forest_model'
        return mlflow.sklearn.load_model(model_uri)

    # Load model
    model = load_model()

    # App title
    st.title("Customer Satisfaction Prediction")

    # Sidebar for inputs
    with st.sidebar:
        st.title("Customer Satisfaction Predictor")
        st.markdown("""
            <p style="text-align: center;">Please fill in the form in order to predict the customer satisfaction for their flight. Enter the required details, and the model will provide a satisfaction prediction based on your inputs.</p>
        """, unsafe_allow_html=True)

    # Create collapsible section for input features
    with st.expander("Input Features", expanded=True):
        col1, col2 = st.columns(2)

        # Input features for column 1 with tooltips and explanations
        with col1:
            age = st.number_input("Age", min_value=1, max_value=100, value=25, help="Enter the customer's age.")
            flight_distance = st.number_input("Flight Distance", min_value=0, value=235, help="Distance of the flight in miles.")
            inflight_wifi_service = st.number_input("Inflight Wifi Service", min_value=0, max_value=5, value=3, help="Rate the inflight Wi-Fi service.")
            departure_convenience = st.number_input("Departure/Arrival Time Convenience", min_value=0, max_value=5, value=2, help="Rate the convenience of departure/arrival times.")
            ease_online_booking = st.number_input("Ease of Online Booking", min_value=0, max_value=5, value=3, help="Rate the ease of booking online.")
            gate_location = st.number_input("Gate Location", min_value=0, max_value=5, value=3, help="Rate the location of the gate.")
            food_drink = st.number_input("Food and Drink", min_value=0, max_value=5, value=3, help="Rate the quality of food and drink.")
            online_boarding = st.number_input("Online Boarding", min_value=0, max_value=5, value=1, help="Rate the online boarding process.")
            seat_comfort = st.number_input("Seat Comfort", min_value=0, max_value=5, value=3, help="Rate the comfort of your seat.")
            inflight_entertainment = st.number_input("Inflight Entertainment", min_value=0, max_value=5, value=1, help="Rate the inflight entertainment.")

        # Input features for column 2 with tooltips and explanations
        with col2:
            onboard_service = st.number_input("Onboard Service", min_value=0, max_value=5, value=1, help="Rate the onboard service quality.")
            leg_room_service = st.number_input("Leg Room Service", min_value=0, max_value=5, value=1, help="Rate the leg room service.")
            baggage_handling = st.number_input("Baggage Handling", min_value=0, max_value=5, value=5, help="Rate the baggage handling.")
            checkin_service = st.number_input("Checkin Service", min_value=0, max_value=5, value=3, help="Rate the check-in service.")
            inflight_service = st.number_input("Inflight Service", min_value=0, max_value=5, value=1, help="Rate the inflight service.")
            cleanliness = st.number_input("Cleanliness", min_value=0, max_value=5, value=4, help="Rate the cleanliness of the flight.")
            departure_delay = st.number_input("Departure Delay in Minutes", min_value=0, value=6, help="Enter the departure delay time in minutes.")
            arrival_delay = st.number_input("Arrival Delay in Minutes", min_value=0, value=0, help="Enter the arrival delay time in minutes.")

        # Categorical variables
        gender = st.selectbox("Gender", ["Male", "Female"])
        customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
        type_of_travel = st.selectbox("Type of Travel", ["Personal Travel", "Business travel"])
        class_type = st.selectbox("Class", ["Eco", "Eco Plus"])

    # Convert text-based input to numerical values
    gender_male = 1 if gender == "Male" else 0
    customer_type_disloyal = 1 if customer_type == "Disloyal Customer" else 0
    type_of_travel_personal = 1 if type_of_travel == "Personal Travel" else 0
    class_eco = 1 if class_type == "Eco" else 0
    class_eco_plus = 1 if class_type == "Eco Plus" else 0

    # Prepare input data for model
    input_data = np.array([age, flight_distance, inflight_wifi_service, departure_convenience, ease_online_booking, 
                           gate_location, food_drink, online_boarding, seat_comfort, inflight_entertainment, 
                           onboard_service, leg_room_service, baggage_handling, checkin_service, inflight_service, 
                           cleanliness, departure_delay, arrival_delay, gender_male, customer_type_disloyal, 
                           type_of_travel_personal, class_eco, class_eco_plus]).reshape(1, -1)

    # Create collapsible section for prediction
    with st.expander("Prediction Result", expanded=True):
        # Progress bar and prediction
        if st.button("Predict Satisfaction"):
            with st.spinner('Making prediction...'):
                time.sleep(2)
                prediction = model.predict(input_data)
                prediction_proba = model.predict_proba(input_data)[0]  # Get prediction probabilities

            # Show Prediction Result
            if prediction[0] == 1:
                st.success(f"Prediction: Satisfied 🟢")
                st.markdown(f"Confidence: **{prediction_proba[1] * 100:.2f}%**")
            else:
                st.error(f"Prediction: Dissatisfied 🔴")
                st.markdown(f"Confidence: **{prediction_proba[0] * 100:.2f}%**")

            # Display Prediction Probability as Pie Chart
            st.subheader("Prediction Probability")
            labels = ['Dissatisfied', 'Satisfied']
            sizes = [prediction_proba[0], prediction_proba[1]]  # Use actual prediction probabilities
            fig2, ax2 = plt.subplots(figsize=(5, 5))  # Adjusted size to 5x5
            ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#ff6666", "#66b3ff"])
            ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig2)

    # Create collapsible section for visualizations
    with st.expander("Visualizations", expanded=True):
        # Visualization: Display Feature Inputs as a Bar Chart
        features = ["Age", "Flight Distance", "Inflight Wifi", "Departure Convenience", "Online Booking", "Gate Location", 
                    "Food and Drink", "Online Boarding", "Seat Comfort", "Inflight Entertainment", "Onboard Service", 
                    "Leg Room Service", "Baggage Handling", "Checkin Service", "Inflight Service", "Cleanliness", 
                    "Departure Delay", "Arrival Delay", "Gender", "Customer Type", "Type of Travel", "Class (Eco)", "Class (Eco Plus)"]

        values = [age, flight_distance, inflight_wifi_service, departure_convenience, ease_online_booking, gate_location, 
                  food_drink, online_boarding, seat_comfort, inflight_entertainment, onboard_service, leg_room_service, 
                  baggage_handling, checkin_service, inflight_service, cleanliness, departure_delay, arrival_delay, gender_male, 
                  customer_type_disloyal, type_of_travel_personal, class_eco, class_eco_plus]

        feature_data = pd.DataFrame({"Feature": features, "Value": values})
        fig = px.bar(feature_data, x="Feature", y="Value", color="Value", title="Input Features")
        st.plotly_chart(fig)

# Run the app
if __name__ == '__main__':
    customer_satisfaction_prediction()
