import streamlit as pd_app

# Set up a premium look for Smile Care Dental Clinic
pd_app.set_page_config(page_title="SMILE CARE DENTAL CLINIC", page_icon="🦷", layout="centered")

# Custom Styling for a premium Gold and Navy Blue Look
pd_app.markdown("""
    <style>
    .main { background-color: #FAF9F6; }
    .wallet-card {
        background: linear-gradient(135deg, #0A2540 0%, #1A365D 100%);
        color: #DFBA6B;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #0A2540 !important;
        color: #DFBA6B !important;
        border-radius: 8px !important;
        border: 1px solid #DFBA6B !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App Title with your specific branding
pd_app.title("🦷 SMILE CARE DENTAL CLINIC")
pd_app.caption("Your Premium Dental & Implant Care Partner")

# Navigation Tabs
tab1, tab2, tab3 = pd_app.tabs(["💳 Loyalty Wallet", "📅 Book Appointment", "💬 Message Support"])

# Simulated Patient Data
if 'points' not in pd_app.session_state:
    pd_app.session_state.points = 350

with tab1:
    pd_app.markdown(f"""
    <div class="wallet-card">
        <p style="font-size: 14px; text-transform: uppercase; letter-spacing: 2px; color: #BEE3F8;">Luxury Loyalty Card</p>
        <p style="font-size: 16px; margin-bottom: 5px;">Your Treatment Points</p>
        <h1 style="font-size: 48px; color: #DFBA6B; margin: 0;">{pd_app.session_state.points}</h1>
        <p style="font-size: 14px; color: #E2E8F0;">Equivalent to ₹{pd_app.session_state.points}</p>
    </div>
    """, unsafe_allow_html=True)
    
    pd_app.info("✨ Collect points with every visit! 1 Point earned for every ₹100 spent.")
    
    # Referral Button
    if pd_app.button("🎁 Refer a Friend & Earn 50 Points"):
        pd_app.session_state.points += 50
        pd_app.success("Referral link generated! 50 Points provisionally added to your wallet! 🎉")
        pd_app.rerun()

with tab2:
    pd_app.subheader("Schedule Your Next Visit")
    
    treatment = pd_app.selectbox("Select Treatment Area", [
        "Routine Consultation & Cleaning",
        "Advanced Implant Consultation",
        "Cosmetic & Smile Design",
        "Follow-up / Post-Op Check"
    ])
    
    date = pd_app.date_input("Choose Preferred Date")
    timeslot = pd_app.radio("Select Timeslot", ["10:00 AM - 12:00 PM", "12:00 PM - 02:00 PM", "06:00 PM - 09:00 PM"])
    
    if pd_app.button("Confirm Appointment Booking"):
        pd_app.success(f"Request submitted for {treatment} on {date} during {timeslot}. Our team will confirm via WhatsApp shortly!")

with tab3:
    pd_app.subheader("Direct Message Support")
    pd_app.caption("Our clinic team typically replies within 2 hours during clinic hours (10 AM - 8 PM).")
    
    user_msg = pd_app.text_area("How can we help you today?", placeholder="e.g., Experiencing mild sensitivity after my procedure...")
    
    if pd_app.button("Send Message"):
        if user_msg:
            pd_app.success("Message sent! Our support team will review your note shortly.")
            pd_app.info("We’ll follow up as soon as possible during clinic hours.")
        else:
            pd_app.warning("Please type a message before sending.")
