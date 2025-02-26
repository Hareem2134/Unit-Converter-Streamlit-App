import streamlit as st
from pint import UnitRegistry

st.set_page_config(page_title="Google Unit Converter", page_icon="🔄", layout="centered")

# Initialize unit registry
ureg = UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg[from_unit]).to(to_unit)
        return result.magnitude, result.units
    except Exception as e:
        st.error(f"Error converting units: {e}")
        return None, None

# Streamlit UI
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f6;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #00008B;
        }
        div[data-baseweb="select"] > div {
            border-radius: 10px !important;
            border: 2px solid #00008B !important;
        }
        input[type="number"] {
            border-radius: 10px !important;
            border: 2px solid #00008B !important;
            padding: 5px;
        }
        button[kind="secondary"] {
            border-radius: 10px !important;
            border: 2px solid #00008B !important;
            background-color: white;
            color: #00008B;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Unit Conversion Google App</div>", unsafe_allow_html=True)

# Unit Categories
categories = {
    "Length": ["meters", "kilometers", "miles", "feet", "yards", "inches"],
    "Weight": ["grams", "kilograms", "pounds", "ounces", "milligrams", "micrograms", "tonnes"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liters", "milliliters", "gallons", "cups", "cubic meters", "cubic feet", "pints", "quarts", "gallons"],
    "Area": ["square meters", "square kilometers", "square miles", "acres", "hectares"],
    "Time": ["seconds", "minutes", "hours", "days", "weeks", "months", "years"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour", "knots"],
    "Energy": ["joules", "kilojoules", "calories", "kilocalories"],
    "Pressure": ["pascals", "kilopascals", "bars", "atmospheres", "torr", "millimeters of mercury"],
}

category = st.selectbox("Select a category", list(categories.keys()))
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])
value = st.number_input("Enter value", min_value=0.0, format="%.6f")

if st.button("Convert"):
    converted_value, converted_unit = convert_units(value, from_unit, to_unit)
    if converted_value is not None:
        st.success(f"{value} {from_unit} = {converted_value:.6f} {converted_unit}")
    else:
        st.error(f"Error: {converted_unit}")

# Footnotes
st.markdown("""
<div style="font-size: 15px; color: gray; margin-top: 50px; text-align: center;">
    <p>This app uses the Pint library for unit conversion & its made by Hareem Farooqi, Alhamdulillah</p>
</div>
""", unsafe_allow_html=True)