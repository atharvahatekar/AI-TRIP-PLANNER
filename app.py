import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv
import time
import json
import datetime
import base64

# Apply dark theme and custom settings
st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'About': "# AI Trip Planner\nCreate personalized travel itineraries powered by AI."
    }
)

# Apply custom CSS for dark theme and better styling
st.markdown("""
<style>
    /* Dark theme customization */
    .main {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #0E1117;
    }
    .st-eb, .st-e1, .st-e2, .st-e3, .st-e4, .st-e5, .st-e6, .st-e7, .st-e8, .st-e9 {
        background-color: #1E1E1E !important;
    }
    /* Header styling */
    .title-container {
        display: flex;
        align-items: center;
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .title-text {
        color: #FFFFFF;
        margin-left: 10px;
    }
    /* Card styling */
    .itinerary-container {
        background-color: #262730;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    /* Button styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    /* Input field styling */
    .stTextInput>div>div>input {
        background-color: #333333;
        color: white;
        border: 1px solid #555555;
    }
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #262730;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4CAF50 !important;
        color: white;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #262730;
    }
</style>
""", unsafe_allow_html=True)

load_dotenv()

# Title with emoji and animation
st.markdown('''
<div class="title-container">
    <h1>✈️ AI Trip Planner</h1>
    
</div>
''', unsafe_allow_html=True)

# Create sidebar for inputs
with st.sidebar:
    st.markdown("### 🗺️ Plan Your Perfect Trip")
    
    # Add trip parameters form
    with st.form("planner_form"):
        city = st.text_input("🌆 Destination City", placeholder="e.g., Paris, Tokyo, New York")
        interests = st.text_input("🎯 Your Interests", placeholder="e.g., history, food, adventure")
        
        # New parameters
        trip_duration = st.select_slider(
            "⏱️ Trip Duration",
            options=["Half day", "Full day", "2 days", "3 days", "Week"],
            value="Full day"
        )
        
        budget_options = ["Budget", "Mid-range", "Luxury", "No limit"]
        budget = st.select_slider("💰 Budget Level", options=budget_options, value="Mid-range")
        
        travel_style = st.multiselect(
            "🚶 Travel Style",
            ["Family-friendly", "Adventure", "Cultural", "Relaxation", "Foodie", "Shopping", "Nature"],
            default=["Cultural"]
        )
        
        advanced_options = st.expander("Advanced Options")
        with advanced_options:
            season = st.selectbox("Season of visit", ["Spring", "Summer", "Fall", "Winter", "Current season"])
            accessibility_needs = st.checkbox("Accessibility-friendly options")
        
        submitted = st.form_submit_button("✨ Generate Itinerary")
        
    # Display app info
    st.markdown("---")
    st.markdown("### 📱 About AI Trip Planner")
    st.markdown("""
    This app uses AI to create personalized travel itineraries 
    based on your preferences. Powered by LLaMA 3.3 70B.
    """)

# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Display some travel tips or inspiration before generating
    if not submitted:
        st.markdown('''
        <div class="itinerary-container">
            <h3>🌟 Welcome to AI Trip Planner!</h3>
            <p>Fill out the form in the sidebar to generate your personalized travel itinerary.</p>
            <h4>Popular destinations:</h4>
            <ul>
                <li>Tokyo, Japan - Modern technology meets ancient traditions</li>
                <li>Paris, France - Art, cuisine, and iconic landmarks</li>
                <li>Bali, Indonesia - Beautiful beaches and spiritual experiences</li>
                <li>New York City, USA - The city that never sleeps</li>
            </ul>
        </div>
        ''', unsafe_allow_html=True)

# Process the submission
if submitted:
    if city and interests:
        # Show a loading spinner
        with st.spinner("🔮 Creating your perfect itinerary..."):
            # Initialize planner with new parameters
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(f"{interests}, Duration: {trip_duration}, Budget: {budget}, Style: {', '.join(travel_style)}")
            
            # Add a small delay for better UX
            time.sleep(1)
            
            # Generate the itinerary
            itinerary = planner.create_itineary()
            
            # Create a timestamp for the itinerary
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # Store in session state for reuse
            if 'itineraries' not in st.session_state:
                st.session_state.itineraries = []
            
            st.session_state.itineraries.append({
                "city": city,
                "interests": interests,
                "duration": trip_duration,
                "budget": budget,
                "itinerary": itinerary,
                "created_at": timestamp
            })
            
            st.session_state.current_itinerary = itinerary
            
        # Display success message
        st.success("✅ Your custom itinerary has been created!")
        
        # Display the results in tabs
        tabs = st.tabs(["� Itinerary", "🗺️ Map View", "🔍 Details", "💾 Save & Share"])
        
        with tabs[0]:
            st.markdown(f'''
            <div class="itinerary-container">
                <h2>🌈 Your {trip_duration} Itinerary for {city}</h2>
                <h4>Based on: {interests} • Budget: {budget}</h4>
                <hr>
                {itinerary}
            </div>
            ''', unsafe_allow_html=True)

        with tabs[1]:
            st.info("📍 Map view will display points of interest from your itinerary.")
            # Placeholder for map - would require additional implementation
            st.markdown(f"🗺️ Interactive map for your {city} itinerary would appear here.")
            
        with tabs[2]:
            st.markdown(f'''
            <div class="itinerary-container">
                <h3>📊 Trip Details</h3>
                <ul>
                    <li><b>Destination:</b> {city}</li>
                    <li><b>Interests:</b> {interests}</li>
                    <li><b>Duration:</b> {trip_duration}</li>
                    <li><b>Budget Level:</b> {budget}</li>
                    <li><b>Travel Style:</b> {', '.join(travel_style)}</li>
                </ul>
            </div>
            ''', unsafe_allow_html=True)
            
        with tabs[3]:
            st.markdown("### 💾 Save Your Itinerary")
            col1, col2 = st.columns(2)
            
            # Create download button
            with col1:
                # Convert itinerary to JSON for download
                itinerary_data = {
                    "destination": city,
                    "interests": interests,
                    "duration": trip_duration,
                    "budget": budget,
                    "travel_style": travel_style,
                    "itinerary": itinerary,
                    "created_at": timestamp
                }
                
                json_str = json.dumps(itinerary_data, indent=4)
                b64 = base64.b64encode(json_str.encode()).decode()
                href = f'<a href="data:application/json;base64,{b64}" download="{city}_itinerary.json" class="download-btn">Download Itinerary (JSON)</a>'
                st.markdown(href, unsafe_allow_html=True)
            
            with col2:
                st.download_button(
                    label="Download as Text",
                    data=f"AI Trip Planner - Itinerary for {city}\n\n{itinerary}\n\nGenerated on {timestamp}",
                    file_name=f"{city}_itinerary.txt",
                    mime="text/plain"
                )
            
            st.markdown("### 📱 Share Your Itinerary")
            # Placeholder for share functionality
            st.markdown("Sharing functionality would be implemented here.")
            
    else:
        st.sidebar.warning("⚠️ Please fill in both City and Interests to generate an itinerary")



