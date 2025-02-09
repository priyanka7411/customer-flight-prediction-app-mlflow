import pandas as pd
import streamlit as st
import mlflow.sklearn
import plotly.express as px

def flight_price_prediction():
    # Set gradient background and adjust UI colors
    st.markdown(
        """
        <style>
        .stSidebar {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            color: white;
        }
        .stTitle {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #6A4E23;  /* Dark brown text color */
        }
        .stHeader {
            font-size: 28px;
            color: #6A4E23;  /* Dark brown text color */
            text-align: center;
            font-weight: 600;
        }
        .stSubheader {
            font-size: 22px;
            color: #6A4E23;  /* Dark brown text color */
            font-weight: 500;
            margin-top: 20px;
        }
        .stInput, .stSelectbox, .stSlider {
            width: 90%;
            margin: 10px auto;
            background-color: rgba(255, 255, 255, 0.9);  /* Light white background for inputs */
            padding: 12px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 16px;
            border: 1px solid #D3A54C;  /* Border color to match the cream theme */
        }

        .stButton>button {
            background-color: #6A4E23;  /* Dark brown button color */
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #8E6E46;  /* Slightly lighter brown on hover */
        }

        .price-box {
            background-color: #F4D03F;  /* Yellowish box for prediction */
            color: #6A4E23;  /* Dark brown text */
            padding: 15px;
            font-size: 18px;
            text-align: center;
            border-radius: 10px;
            width: 50%;
            margin: 20px auto;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Load model from MLflow
    model_uri = 'runs:/752c02cb9c1041cd8eb909540372da3b/Gradient Boosting Regressor Tuning'
    model = mlflow.sklearn.load_model(model_uri)

    # Streamlit app UI
    st.title("Flight Price Prediction")

    st.header("Flight Details")
    st.subheader("Enter the details of your flight to predict the price.")

    # Use columns to align input boxes
    col1, col2 = st.columns(2)

    # Arrange inputs in columns for better alignment
    with col1:
        duration = st.number_input("Flight Duration (in minutes)", min_value=1, key="duration", help="Enter the total duration of the flight in minutes.")
        dep_hour = st.slider("Departure Time (Hour)", 0, 23, key="dep_hour", help="Select the departure hour (0-23).")
        dep_minute = st.slider("Departure Time (Minute)", 0, 59, key="dep_minute", help="Select the departure minute (0-59).")
        arrival_hour = st.slider("Arrival Time (Hour)", 0, 23, key="arrival_hour", help="Select the arrival hour (0-23).")

    with col2:
        total_stops = st.selectbox("Number of Stops", options=[0, 1, 2, 3, 4], key="total_stops", help="Select the number of stops in the flight.")
        arrival_minute = st.slider("Arrival Time (Minute)", 0, 59, key="arrival_minute", help="Select the arrival minute (0-59).")
        date_of_journey = st.date_input("Date of Journey", key="date_of_journey", help="Select the date of your flight journey.")

    st.subheader("Airline Information")
    airline = st.selectbox("Choose the Airline ✈️", options=[
        'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
        'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
        'Trujet', 'Vistara', 'Vistara Premium economy'
    ], key="airline", help="Select the airline for your flight.")

    st.subheader("Source and Destination")
    col1, col2 = st.columns(2)

    # Arrange source and destination in two columns
    with col1:
        source = st.selectbox("Flight Origin", ['Chennai', 'Delhi', 'Kolkata', 'Mumbai'], key="source", help="Select the origin city of your flight.")

    with col2:
        destination = st.selectbox("Flight Destination", ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi'], key="destination", help="Select the destination city for your flight.")

    # Extract day and month
    day_of_journey = date_of_journey.day
    month_of_journey = date_of_journey.month

    # One-hot encoding mappings
    airlines_map = {
        'Air India': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'GoAir': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'IndiGo': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        'Jet Airways': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        'Jet Airways Business': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        'Multiple carriers': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        'Multiple carriers Premium economy': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        'SpiceJet': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        'Trujet': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        'Vistara': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        'Vistara Premium economy': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    }

    sources_map = {
        'Chennai': [1, 0, 0, 0],
        'Delhi': [0, 1, 0, 0],
        'Kolkata': [0, 0, 1, 0],
        'Mumbai': [0, 0, 0, 1]
    }

    destinations_map = {
        'Cochin': [1, 0, 0, 0, 0],
        'Delhi': [0, 1, 0, 0, 0],
        'Hyderabad': [0, 0, 1, 0, 0],
        'Kolkata': [0, 0, 0, 1, 0],
        'New Delhi': [0, 0, 0, 0, 1]
    }

    # Encode airline, source, and destination
    airline_encoding = airlines_map[airline]
    source_encoding = sources_map[source]
    destination_encoding = destinations_map[destination]

    # Create DataFrame for prediction
    input_data = pd.DataFrame({
        'Duration': [duration],
        'Total_Stops': [total_stops],
        'Day_of_Journey': [day_of_journey],
        'Month_of_Journey': [month_of_journey],
        'Dep_Hour': [dep_hour],
        'Dep_Minute': [dep_minute],
        'Arrival_Hour': [arrival_hour],
        'Arrival_Minute': [arrival_minute],
        'Airline_Air India': [airline_encoding[0]],
        'Airline_GoAir': [airline_encoding[1]],
        'Airline_IndiGo': [airline_encoding[2]],
        'Airline_Jet Airways': [airline_encoding[3]],
        'Airline_Jet Airways Business': [airline_encoding[4]],
        'Airline_Multiple carriers': [airline_encoding[5]],
        'Airline_Multiple carriers Premium economy': [airline_encoding[6]],
        'Airline_SpiceJet': [airline_encoding[7]],
        'Airline_Trujet': [airline_encoding[8]],
        'Airline_Vistara': [airline_encoding[9]],
        'Airline_Vistara Premium economy': [airline_encoding[10]],
        'Source_Chennai': [source_encoding[0]],
        'Source_Delhi': [source_encoding[1]],
        'Source_Kolkata': [source_encoding[2]],
        'Source_Mumbai': [source_encoding[3]],
        'Destination_Cochin': [destination_encoding[0]],
        'Destination_Delhi': [destination_encoding[1]],
        'Destination_Hyderabad': [destination_encoding[2]],
        'Destination_Kolkata': [destination_encoding[3]],
        'Destination_New Delhi': [destination_encoding[4]]
    })

    # Add prediction button with a spinner
    if st.button("Predict Price"):
        # Make prediction
        predicted_price = model.predict(input_data)[0]
        st.markdown(f'<div class="price-box">Estimated Price: ₹ {predicted_price:.2f}</div>', unsafe_allow_html=True)

        # Load data and show visuals
        df = pd.read_csv('data/cleaned_flight_price.csv')

        # Flight Price Distribution
        st.subheader("Flight Price Distribution")
        fig = px.histogram(df, x='Price', nbins=30, title='Distribution of Flight Prices', labels={'Price': 'Price (₹)'})
        st.plotly_chart(fig)

# Call the function to run the app
if __name__ == '__main__':
    flight_price_prediction()
