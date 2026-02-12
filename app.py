import streamlit as st
import random
import time
import datetime

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Bahria Town AI Advisor | PropTecSolutions",
    page_icon="🏢",
    layout="wide"
)

# --- 2. PREMIUM BTK THEME (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #050a14; color: #ffffff; }
    .stMetric { background-color: #0d1b31; padding: 20px; border-radius: 12px; border: 1px solid #c5a059; }
    .stTextInput>div>div>input { background-color: #16243a; color: #f1f1f1; border: 1px solid #c5a059; }
    h1, h2, h3 { color: #c5a059; }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: LEAD CAPTURE ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059;'>🏢 BTK Executive</h2>", unsafe_allow_html=True)
    st.write("Proprietary Investment Desk for Bahria Town Karachi.")
    
    with st.form("btk_lead_form"):
        st.subheader("Investor Onboarding")
        name = st.text_input("Investor Name")
        whatsapp = st.text_input("WhatsApp Number")
        interest = st.selectbox("Area", ["Precinct 1", "Sports City", "Golf City", "Bahria Paradise"])
        
        submit = st.form_submit_button("Request ROI Analysis")
        if submit:
            if name and whatsapp:
                st.success(f"Protocol Initiated. Data transmitted to PropTecSolutions.")
            else:
                st.warning("Please provide credentials.")

# --- 4. DASHBOARD HEADER ---
st.title("🏢 Bahria Town Karachi: AI Asset Intelligence")
st.markdown(f"**Enterprise Protocol:** Enabled | **Market Status:** {datetime.date.today().strftime('%B, 2026')}")

# --- 5. SENTIMENT GAUGE ---
col1, col2, col3 = st.columns(3)

with col1:
    btk_score = random.randint(68, 85)
    st.metric(label="Market Sentiment Score", value=f"{btk_score}/100", delta="Growth Trend")

with col2:
    st.metric(label="Rental Yield Average", value="7.2%", delta="↑ 0.4%")

with col3:
    st.metric(label="Development Velocity", value="Fast-Track", delta="Stable")

st.divider()

# --- 6. PRECINCT-LEVEL SEARCH ---
st.subheader("🔍 Precinct Intelligence Search")
query = st.text_input("Enter Precinct (e.g., Precinct 15, Sports City):", placeholder="Accessing BTK Data Lake...")

if query:
    with st.spinner(f"Analyzing Bahria Town Market Depth for {query}..."):
        time.sleep(1.2)
        
        st.write(f"### Intelligence Brief: {query}")
        
        t1, t2 = st.tabs(["Investment Outlook", "Market Liquidity"])
        
        with t1:
            st.info(f"AI Model indicates high absorption rates in **{query}**. Projected capital gains of 12-15% expected over the next 18 months.")
        
        with t2:
            st.write("Recent Transaction Volume (Simulated AI Data):")
            st.bar_chart([random.randint(10, 40) for _ in range(5)])

# --- 7. SECURITY SHIELD (Proprietary Footer) ---
st.divider()
st.markdown("""
    <div style='text-align: center; color: #c5a059; font-size: 11px; font-weight: bold;'>
        PROPRIETARY ASSET OF PROPTECSOLUTIONS <br>
        <span style='color: gray;'>© 2026 Salman Raja | Founder & CEO. <br>
        CONFIDENTIAL PROTOTYPE: UNAUTHORIZED REPLICATION OR DISTRIBUTION IS STRICTLY PROHIBITED.</span>
    </div>
    """, unsafe_allow_html=True)
