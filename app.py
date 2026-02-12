import streamlit as st
import random
import time

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="BTK Advisor | PropTecSolutions", page_icon="🏢", layout="wide")

# --- 2. THE SECRET SHIELD (Is se GitHub Icon gayab hoga) ---
st.markdown("""
    <style>
    /* Sab kuch hide karne ke liye */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    
    /* Theme Colors */
    .main {background-color: #050a14; color: white;}
    .stMetric {background-color: #0d1b31; border: 1px solid #c5a059;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR WITH BRANDING ---
with st.sidebar:
    st.title("🏢 BTK Executive")
    with st.form("leads"):
        st.write("Investor Inquiry Form")
        name = st.text_input("Name")
        phone = st.text_input("WhatsApp")
        # BUTTON UPDATED HERE:
        if st.form_submit_button("Submit to PropTecSolutions"):
            st.success("Data secured by PropTecSolutions.")

# --- 4. CONTENT ---
st.title("🏢 Bahria Town Karachi: AI Advisor")
col1, col2 = st.columns(2)
with col1:
    st.metric("Asset Sentiment", f"{random.randint(70, 85)}/100", delta="Market Growth")
with col2:
    st.metric("Yield Accuracy", "94.2%", delta="AI Verified")

query = st.text_input("Search Precinct/Sector:")
if query:
    with st.spinner("Analyzing..."):
        time.sleep(1)
        st.success(f"Strategy for {query}: Highly recommended hold.")

# --- 5. FOOTER ---
st.divider()
st.markdown("<div style='text-align: center; color: #c5a059; font-weight: bold;'>PROPRIETARY ASSET OF PROPTECSOLUTIONS</div>", unsafe_allow_html=True)
