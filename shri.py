import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="AI Blood Network", layout="wide")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

if not st.session_state.logged_in:

    st.title("🩸 AI Blood Network Login")

    role = st.selectbox("Login As", ["Patient / Donor", "Hospital"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if role == "Hospital" and username == "hospital" and password == "1234":
            st.session_state.logged_in = True
            st.session_state.role = "Hospital"
            st.rerun()

        elif role == "Patient / Donor":
            st.session_state.logged_in = True
            st.session_state.role = "Patient"
            st.rerun()

        else:
            st.error("Invalid login")

    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🩸 AI Blood Network")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Find Blood", "Donor Registration",
     "Hospital Panel", "Map", "Analytics", "AI Assistant"]
)

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ---------------- DATA WITH COMPONENTS ----------------
data = {
    "Hospital": ["Apollo", "City Bank", "Life Care"],
    "Latitude": [12.9716, 12.2958, 12.9141],
    "Longitude": [77.5946, 76.6394, 77.6101],

    "O+ RBC": [5,2,4],
    "O+ Platelets": [3,1,2],
    "O+ Plasma": [2,2,1],

    "A+ RBC": [4,3,2],
    "A+ Platelets": [2,1,3],
    "A+ Plasma": [1,2,2],
}

df = pd.DataFrame(data)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.title("🩸 Smart Blood Network Dashboard")

    st.subheader("Component Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("O+ RBC", "11 Units")
    col2.metric("O+ Platelets", "6 Units")
    col3.metric("O+ Plasma", "5 Units")

    st.subheader("Hospital Inventory")
    st.dataframe(df)

    st.subheader("🚨 Emergency Alert")
    st.error("O+ Platelets urgently required")

    # Expiry alert
    st.subheader("⚠ Expiry Alerts")
    st.warning("Platelets at Apollo will expire in 2 days")

# ---------------- FIND BLOOD ----------------
elif page == "Find Blood":

    st.title("🔍 Search Blood Components")

    blood_group = st.selectbox("Blood Group", ["O+","A+"])
    component = st.selectbox("Component", ["RBC","Platelets","Plasma"])

    column = blood_group + " " + component

    if st.button("Search"):
        st.table(df[["Hospital", column]])

# ---------------- DONOR ----------------
elif page == "Donor Registration":

    st.title("❤️ Donor Registration")

    name = st.text_input("Name")
    group = st.selectbox("Blood Group", ["O+","A+"])
    phone = st.text_input("Phone")

    if st.button("Register"):
        st.success("Donor Registered")

# ---------------- HOSPITAL PANEL ----------------
elif page == "Hospital Panel":

    if st.session_state.role != "Hospital":
        st.warning("Hospital login required")
        st.stop()

    st.title("🏥 Hospital Dashboard")

    group = st.selectbox("Blood Group", ["O+","A+"])
    component = st.selectbox("Component", ["RBC","Platelets","Plasma"])

    units = st.number_input("Units", min_value=0)

    if st.button("Update Inventory"):
        st.success("Updated Successfully")

# ---------------- MAP ----------------
elif page == "Map":

    st.title("🗺 Blood Bank Map")

    st.map(df[["Latitude","Longitude"]])

# ---------------- ANALYTICS + AI ----------------
elif page == "Analytics":

    st.title("📊 Blood Usage Analytics")

    chart_data = pd.DataFrame({
        "Day": ["Mon","Tue","Wed","Thu","Fri"],
        "Platelets Usage": [10,12,8,9,11]
    })

    st.line_chart(chart_data.set_index("Day"))

    st.subheader("🤖 AI Prediction")

    days = np.array([1,2,3,4,5]).reshape(-1,1)
    usage = np.array([10,12,8,9,11])

    model = LinearRegression()
    model.fit(days, usage)

    pred = model.predict([[6]])

    st.success(f"Predicted Platelets demand tomorrow: {int(pred[0])}")

# ---------------- AI ASSISTANT ----------------
elif page == "AI Assistant":

    st.title("🤖 AI Assistant")

    q = st.text_input("Ask about blood availability")

    if q:
        if "platelets" in q.lower():
            st.write("Platelets available at Apollo")
        elif "rbc" in q.lower():
            st.write("RBC available at City Bank")
        else:
            st.write("Try asking about RBC, Platelets, Plasma")