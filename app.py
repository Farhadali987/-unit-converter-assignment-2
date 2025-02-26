import streamlit as st

# --- Set Page Configuration ---
st.set_page_config(page_title="Unit Converter", layout="wide")

# --- Function to Add Background Image ---
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
            color: white;
        }}
        .result {{
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: yellow;
            animation: fadeIn 2s;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        .info {{
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: white;
            background: rgba(0, 0, 0, 0.7);
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ **بیک گراؤنڈ امیج**
background_image_url = "https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg"
set_background(background_image_url)

# --- Unit Categories ---
unit_categories = {
    "Length": {
        "Millimeters": 0.001,
        "Centimeters": 0.01,
        "Meters": 1.0,
        "Kilometers": 1000.0,
        "Inches": 0.0254,
        "Feet": 0.3048,
        "Yards": 0.9144,
        "Miles": 1609.34
    },
    "Mass": {
        "Milligrams": 0.000001,
        "Grams": 0.001,
        "Kilograms": 1.0,
        "Metric Tons": 1000.0,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    },
    "Time": {
        "Seconds": 1.0,
        "Minutes": 60.0,
        "Hours": 3600.0,
        "Days": 86400.0
    }
}

# --- Function to Convert Units ---
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value
    else:
        return (value * unit_categories[category][from_unit]) / unit_categories[category][to_unit]

# --- Title ---
st.markdown('<h1 style="text-align: center; color: white;">🌟 Unit Converter</h1>', unsafe_allow_html=True)

# --- Unit Category Selection ---
category = st.selectbox("Select Unit Category", list(unit_categories.keys()))

# --- Input Fields for Conversion ---
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From", list(unit_categories[category].keys()))
to_unit = st.selectbox("To", list(unit_categories[category].keys()))

# --- Convert & Display Result ---
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f'<div class="result">✅ {value} {from_unit} = {result:.4f} {to_unit}</div>', unsafe_allow_html=True)
    
    # --- Display Farhad Ali's Information ---
    st.markdown(
        """
        <div class="info">
        My name is <b>Farhad Ali</b>, I am an <b>IT student</b> and learning <b>Latest Technologies</b> at <b>Sindh Governor House</b>.  
        I am <b>18 years old</b> and I am excited to learn and work in <b>Information Technology Industries</b>.
        </div>
        """,
        unsafe_allow_html=True
    )
