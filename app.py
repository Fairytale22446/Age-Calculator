import streamlit as st
import datetime

def calculate_age(birth_date):
    today = datetime.date(2025, 3, 13)  # Fixed current date
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day
    
    if age_days < 0:
        age_months -= 1
        age_days += (today - datetime.date(today.year, today.month, 1)).days
    
    if age_months < 0:
        age_years -= 1
        age_months += 12
    
    return age_years, age_months, age_days

def years_until_100(birth_date):
    return 100 - (2025 - birth_date.year)

def main():
    st.set_page_config(page_title="Age Calculator", page_icon="🎂", layout="centered")
    
    # Custom styles
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E6E6FA;
            color: #4B0082;
            font-family: 'Arial', sans-serif;
        }
        .stDateInput label {
            color: #6A0DAD;
            font-weight: bold;
            font-size: 16px;
        }
        .stDateInput input {
            background-color: #ffffff;
            color: #4B0082;
            border-radius: 10px;
            padding: 8px;
            border: 1px solid #D8BFD8;
        }
        .stButton button {
            background-color: #9370DB;
            color: white;
            padding: 12px 26px;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #6A5ACD;
        }
        .stSuccess, .stInfo {
            background-color: #D8BFD8;
            color: #4B0082;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #BA55D3;
            font-weight: bold;
            text-align: center;
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🎂 Age Calculator")
    st.write("Enter your birthdate to find out your exact age!")
    
    birth_date = st.date_input("**Enter your birthdate:**", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2025, 3, 13))
    
    if birth_date:
        years, months, days = calculate_age(birth_date)
        st.markdown(f'<p class="stSuccess">You are {years} years, {months} months, and {days} days old! 🎉</p>', unsafe_allow_html=True)
        
        years_to_100 = years_until_100(birth_date)
        if years_to_100 > 0:
            st.markdown(f'<p class="stInfo">You will turn 100 in {years_to_100} years! 🎂</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="stInfo">Wow! You are already 100+ years old! 🎊</p>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
