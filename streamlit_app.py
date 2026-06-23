import streamlit as st

# Set up premium clinic branding
st.set_page_config(page_title="Smile Care Dental Clinic", page_icon="🦷", layout="centered")

st.title("🦷 SMILE CARE DENTAL CLINIC")
st.caption("Your Premium Dental & Implant Care Partner")

# --- MOCK PATIENT DATABASE ---
PATIENT_DB = {
    "9876543210": {"name": "Amit Gupta", "points": 350},
    "9999988888": {"name": "Suresh Sharma", "points": 120},
    "9820012345": {"name": "Priya Shah", "points": 500}
}

# --- LOGIN / LOOKUP SECTION ---
st.sidebar.header("Patient Access")
mobile_input = st.sidebar.text_input("Enter Mobile Number to View Account", placeholder="e.g., 9876543210")

if mobile_input in PATIENT_DB:
    current_user = PATIENT_DB[mobile_input]["name"]
    current_points = PATIENT_DB[mobile_input]["points"]
    st.sidebar.success(f"Logged in as: {current_user}")
else:
    current_user = "Valued Guest"
    current_points = 0
    if mobile_input:
        st.sidebar.error("Number not found. Showing guest profile.")

# --- NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["💳 Loyalty Wallet", "📅 Book Appointment", "💬 Message Support"])

# --- TAB 1: LOYALTY WALLET ---
with tab1:
    st.markdown(f"### Welcome back, {current_user}!")
    
    with st.container():
        st.markdown(
            f"""
            <div style="background-color:#1e3d59; padding:25px; border-radius:15px; border-left: 8px solid #ffc13b; color: white;">
                <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin: 0; color: #ffc13b;">Luxury Loyalty Card</p>
                <h4 style="margin: 10px 0 5px 0; color: white;">Your Treatment Points</h4>
                <h1 style="font-size: 48px; margin: 0; color: #ffc13b;">{current_points}</h1>
                <p style="font-size: 14px; opacity: 0.8; margin: 10px 0 0 0;">Equivalent to ₹{current_points}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.info("✨ Collect points with every visit! 1 Point earned for every ₹100 spent.")
    if st.button("🎁 Refer a Friend & Earn 50 Points"):
        st.success("Referral link copied!")

# --- TAB 2: BOOK APPOINTMENT ---
with tab2:
    st.markdown("### Schedule Your Next Visit")
    appointment_date = st.date_input("Select Preferred Date")
    appointment_time = st.selectbox("Select Preferred Time Slot", ["10:00 AM", "11:30 AM", "4:00 PM", "6:30 PM"])
    treatment_type = st.selectbox("Purpose of Visit", ["Routine Checkup", "Dental Implant Consultation", "Cosmetic Dentistry"])
    
    if st.button("Confirm Appointment Request"):
        st.success(f"Request submitted for {appointment_date} at {appointment_time}.")

# --- TAB 3: MESSAGE SUPPORT ---
with tab3:
    st.markdown("### Secure Chat with Front Desk")
    user_msg = st.text_input("Type your question here:")
    if st.button("Send Message"):
        if user_msg:
            st.info("Message sent securely to the clinic dashboard.")