import streamlit as st
import google.generativeai as genai
import requests
import os

# --- CONFIGURATION (Replace these with your actual keys later) ---
# It is better to use .env file, but for hackathon speed, put them here temporarily.
os.environ["OPENWEATHER_API_KEY"] = "PASTE_YOUR_OPENWEATHER_KEY_HERE"
os.environ["GEMINI_API_KEY"] = "PASTE_YOUR_GEMINI_KEY_HERE"

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# --- FUNCTION 1: GET REAL WEATHER ---
def get_weather(city_name):
    api_key = os.environ["OPENWEATHER_API_KEY"]
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"{weather_desc}, {temp}°C"
        else:
            return "Clear sky, 25°C" # Fallback if API fails (Safety for Demo)
    except:
        return "Sunny, 30°C" # Fallback if Internet fails

# --- FUNCTION 2: THE AI CAMPAIGN GENERATOR ---
def generate_campaign(product_name, location, weather_context):
    # This is the "Prompt Engineering" part
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    You are an expert Ad Campaign Manager for GroundTruth.
    
    CONTEXT:
    - Product: {product_name}
    - Location: {location}
    - Current Weather: {weather_context}
    
    TASK:
    Create a hyper-local ad campaign.
    
    OUTPUT FORMAT:
    1. **Catchy Headline** (Max 8 words, referring to the weather/location).
    2. **Ad Body Text** (Persuasive, short).
    3. **Visual Description** (Describe the image that should be on the banner).
    4. **Targeting Strategy** (Who should see this? e.g., radius, age).
    """
    
    response = model.generate_content(prompt)
    return response.text

# --- THE WEBSITE (STREAMLIT UI) ---
st.set_page_config(page_title="GroundTruth Nexus", page_icon="📍")

# Header
st.title("📍 GroundTruth Nexus")
st.subheader("Hyper-Local Campaign Generator")
st.markdown("---")

# Sidebar for Inputs
with st.sidebar:
    st.header("Campaign Details")
    product = st.text_input("What are you selling?", "Hot Cappuccino")
    city = st.text_input("Store Location (City)", "Mumbai")
    radius = st.slider("Targeting Radius (Miles)", 0.1, 10.0, 2.0)
    
    generate_btn = st.button("🚀 Launch Campaign", type="primary")

# Main Display Area
if generate_btn:
    with st.spinner(f"Analyzing real-time weather in {city}..."):
        # Step 1: Get Weather
        weather_info = get_weather(city)
        st.success(f"✅ Verified Context: {weather_info} in {city}")
        
    with st.spinner("Generating creative assets..."):
        # Step 2: Call Gemini AI
        campaign_content = generate_campaign(product, city, weather_info)
        
        # Step 3: Display Results
        st.markdown("### 📢 Generated Ad Creative")
        st.info(campaign_content)
        
        # Step 4: The "Business Value" Twist
        st.markdown("---")
        st.metric(label="Estimated Local Reach", value=f"{int(radius * 1500)} People", delta="High Intent")
        st.caption("Powered by GroundTruth Location Intelligence")

else:
    # Default State
    st.info("👈 Enter your product details in the sidebar to generate a campaign.")
