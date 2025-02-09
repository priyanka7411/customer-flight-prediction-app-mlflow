import streamlit as st
from customer_app import customer_satisfaction_prediction  # Import function from customer_app.py
from flight_app import flight_price_prediction            # Import function from flight_app.py

# Custom CSS for a professional look and feel
st.markdown("""
    <style>
    /* Title styling */
    .title {
        font-size: 48px;
        color: #2C3E50;
        font-weight: 700;
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* Header and Subheader styling */
    .header {
        font-size: 36px;
        color: #2980B9;
        font-weight: bold;
        padding-top: 10px;
        padding-bottom: 20px;
        text-align: center;
    }
    .subheader {
        font-size: 24px;
        color: #34495E;
        font-weight: bold;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    /* Button and radio styling */
    .stButton>button {
        background-color: #2980B9;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #1A5276;
        transition: background-color 0.3s ease;
    }

    /* Card-like box for content */
    .content-box {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .content-text {
        font-size: 18px;
        color: #2C3E50;
    }

    /* Sidebar styling */
    .sidebar {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    
    /* Footer */
    .footer {
        font-size: 16px;
        text-align: center;
        color: #888;
        padding: 20px;
        margin-top: 20px;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = "Introduction"

# Introduction Page (Page 1)
if st.session_state.page == "Introduction":
    st.markdown("<div class='header'>Welcome to the Prediction App</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='content-box'>
        <p class='content-text'>This Streamlit app allows you to predict:</p>
        <ul class='content-text'>
            <li> <b>Customer Satisfaction Prediction</b>: Predict customer satisfaction based on flight-related features.</li>
            <li> <b>Flight Price Prediction</b>: Estimate the price of a flight based on various parameters.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Button to go to the next page (Project Selection)
    if st.button("Go to Project Selection ➡️", key="go_to_selection"):
        st.session_state.page = "Project Selection"

# Project Selection Page (Page 2)
elif st.session_state.page == "Project Selection":
    # Sidebar for selecting which app to use
    with st.sidebar:
        st.markdown("<div class='subheader'>Select a Project</div>", unsafe_allow_html=True)
        app_option = st.radio("", ["Customer Satisfaction Prediction", "Flight Price Prediction"])

    st.markdown("<div class='subheader'>Project Selection</div>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>Please choose which prediction app you want to proceed with:</p>", unsafe_allow_html=True)

    # Displaying selection buttons with icons
    col1, col2 = st.columns(2)

    if app_option == "Customer Satisfaction Prediction":
        with col1:
            if st.button("🚀 Customer Satisfaction Prediction", key="customer_app"):
                st.session_state.page = "Customer Satisfaction Prediction"
    
    elif app_option == "Flight Price Prediction":
        with col2:
            if st.button("✈️ Flight Price Prediction", key="flight_app"):
                st.session_state.page = "Flight Price Prediction"

    # Add a 'Back to Introduction' button
    if st.button("⬅️ Back to Introduction", key="back_to_intro"):
        st.session_state.page = "Introduction"

# Main Prediction App - Customer Satisfaction Prediction (Page 3)
elif st.session_state.page == "Customer Satisfaction Prediction":
    st.markdown("<div class='subheader'>Customer Satisfaction Prediction</div>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>You can predict customer satisfaction using this app.</p>", unsafe_allow_html=True)
    customer_satisfaction_prediction()  # Call the function from customer_app.py

    # Add a 'Back to Project Selection' button
    if st.button("⬅️ Back to Project Selection", key="back_to_selection_1"):
        st.session_state.page = "Project Selection"

# Main Prediction App - Flight Price Prediction (Page 4)
elif st.session_state.page == "Flight Price Prediction":
    st.markdown("<div class='subheader'>Flight Price Prediction</div>", unsafe_allow_html=True)
    st.markdown("<p class='content-text'>You can estimate flight prices using this app.</p>", unsafe_allow_html=True)
    flight_price_prediction()  # Call the function from flight_app.py

    # Add a 'Back to Project Selection' button
    if st.button("⬅️ Back to Project Selection", key="back_to_selection_2"):
        st.session_state.page = "Project Selection"

# Footer for a professional touch
#st.markdown("<div class='footer'>Powered by Streamlit | © 2025 Your Company</div>", unsafe_allow_html=True)
