import streamlit as st

# Set up premium clinic branding
st.set_page_config(page_title="Smile Care Dental Clinic", page_icon="🦷", layout="centered")

st.title("🦷 SMILE CARE DENTAL CLINIC")
st.caption("Your Premium Dental & Implant Care Partner")

# --- INITIALIZE DATABASE IN SESSION STATE ---
# This keeps track of data changes while the app is running
if "patient_db" not in st.session_state:
    st.session_state.patient_db = {
        "9876543210": {"id": "PT101", "name": "Amit Gupta", "points": 350},
        "9999988888": {"id": "PT102", "name": "Suresh Sharma", "points": 120}
    }

# --- SIDEBAR: STAFF / ADMIN PANEL ---
st.sidebar.header("🛡️ Staff Control Panel")
admin_action = st.sidebar.selectbox("Choose Action", ["Patient Lookup", "Add New Patient", "Manage Points"])

if admin_action == "Add New Patient":
    st.sidebar.subheader("Register New Account")
    new_id = st.sidebar.text_input("Patient ID (e.g., PT103)")
    new_name = st.sidebar.text_input("Patient Full Name")
    new_phone = st.sidebar.text_input("Mobile Number (10 digits)")
    
    if st.sidebar.button("Register Patient"):
        if new_id and new_name and len(new_phone) == 10:
            st.session_state.patient_db[new_phone] = {"id": new_id, "name": new_name, "points": 0}
            st.sidebar.success(f"Successfully registered {new_name}!")
        else:
            st.sidebar.error("Please fill all fields correctly (Phone must be 10 digits).")

elif admin_action == "Manage Points":
    st.sidebar.subheader("Update Loyalty Wallet")
    search_phone = st.sidebar.text_input("Enter Patient Mobile Number")
    
    if search_phone in st.session_state.patient_db:
        patient = st.session_state.patient_db[search_phone]
        st.sidebar.text(f"Patient: {patient['name']} ({patient['id']})")
        st.sidebar.text(f"Current Balance: {patient['points']} Points")
        
        # Add points section
        amount_spent = st.sidebar.number_input("Treatment Amount Spent (₹)", min_value=0, step=100)
        if st.sidebar.button("➕ Calculate & Add Points"):
            earned_points = int(amount_spent / 100)  # 1 Point per ₹100
            st.session_state.patient_db[search_phone]["points"] += earned_points
            st.sidebar.success(f"Added {earned_points} points! New Balance: {st.session_state.patient_db[search_phone]['points']}")
            st.rerun()
            
        # Redeem points section
        points_to_redeem = st.sidebar.number_input("Points to Redeem (₹1 discount per point)", min_value=0, max_value=patient['points'], step=10)
        if st.sidebar.button("🛑 Redeem Points Automatically"):
            st.session_state.patient_db[search_phone]["points"] -= points_to_redeem
            st.sidebar.success(f"Redeemed {points_to_redeem} points successfully!")
            st.sidebar.info(f"Apply a discount of ₹{points_to_redeem} to the current invoice.")
            st.rerun()
    elif search_phone:
        st.sidebar.error("Patient phone number not found.")

# --- SIDEBAR: PATIENT LOGIN ---
st.sidebar.markdown("---")
st.sidebar.header("📱 Patient Login")
mobile_input = st.sidebar.text_input("Enter Mobile Number to View Account", placeholder="e.g., 9876543210")

if mobile_input in st.session_state.patient_db:
    current_user = st.session_state.patient_db[mobile_input]["name"]
    current_points = st.session_state.patient_db[mobile_input]["points"]
    current_id = st.session_state.patient_db[mobile_input]["id"]
    st.sidebar.success(f"Logged in as: {current_user} ({current_id})")
else:
    current_user = "Valued Guest"
    current_points = 0
    current_id = "N/A"

# --- MAIN INTERFACE TABS ---
tab1, tab2, tab3 = st.tabs(["💳 Loyalty Wallet", "📅 Book Appointment", "💬 Message Support"])

# TAB 1: LOYALTY WALLET
with tab1:
    st.markdown(f"### Welcome back, {current_user}!")
    st.caption(f"Patient ID: {current_id}")
    
    with st.container():
        st.markdown(
            f"""
            <div style="background-color:#1e3d59; padding:25px; border-radius:15px; border-left: 8px solid #ffc13b; color: white;">
                <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 12px; margin: 0; color: #ffc13b;">Luxury Loyalty Card</p>
                <h4 style="margin: 10px 0 5px 0; color: white;">Your Balance</h4>
                <h1 style="font-size: 48px; margin: 0; color: #ffc13b;">{current_points} <span style="font-size:20px; color:white;">Points</span></h1>
                <p style="font-size: 14px; opacity: 0.8; margin: 10px 0 0 0;">Redeemable Value: ₹{current_points}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.info("✨ 1 Point earned for every ₹100 spent on dental treatments.")

# TAB 2 & 3 remain basic for layout continuity
with tab2:
    st.markdown("### Schedule Your Next Visit")
    st.date_input("Select Preferred Date")
    st.selectbox("Select Time Slot", ["10:00 AM", "4:00 PM"])
    st.button("Confirm Request")

with tab3:
    st.markdown("### Secure Chat with Front Desk")
    st.text_input("Type your question here:")
    st.button("Send Message")
    