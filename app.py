# --- Is code ko app.py mein replace karein ---

import streamlit as st
from groq import Groq
from tavily import TavilyClient
import pandas as pd
import plotly.express as px

# 1. Ultra-Premium Page Config (White Font & Dark Mode)
st.set_page_config(page_title="Karachi Real Estate Pro", page_icon="🏢", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff !important; }
    h1, h2, h3, p, span, label, .stMarkdown { color: #ffffff !important; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stChatMessage { background-color: #1e2129; border: 1px solid #3d4450; border-radius: 10px; color: #ffffff !important; }
    [data-testid="stMetricValue"] { color: #00ffcc !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Keys Check
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    tavily = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])
except:
    st.error("API Keys missing!")
    st.stop()

# 3. Sidebar: Multi-Market Dashboard
with st.sidebar:
    st.header("🏢 Market Selection")
    market = st.radio("Focus Area:", ["DHA Karachi", "Bahria Town Karachi", "Both"])
    
    st.markdown("---")
    st.header("📈 Live Trends")
    # Comparison Data for DHA vs Bahria
    df_compare = pd.DataFrame({
        'Project': ['DHA Ph 8', 'BTK Precinct 1', 'DHA City', 'BTK Sports City'],
        'ROI %': [12, 15, 9, 18]
    })
    fig = px.line(df_compare, x='Project', y='ROI %', title="Projected Annual ROI", markers=True)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# 4. Professional Search (DHA + Bahria)
def get_market_intelligence(query, area):
    search_query = f"Latest property rates and news for {area} {query} Karachi February 2026"
    results = tavily.search(query=search_query, search_depth="advanced")
    return "\n".join([f"Source: {res['url']}\nData: {res['content']}" for res in results['results']])

# 5. UI Layout
st.title("⚖️ Karachi Enterprise Advisory")
st.subheader(f"Strategic Intelligence: {market}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about DHA Phase 8 or Bahria Precinct 10 rates..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status(f"Scanning {market} Markets...", expanded=False):
            intel = get_market_intelligence(prompt, market)
        
        system_msg = f"""
        You are the 'Karachi Real Estate Strategist'. 
        Tone: Professional, Corporate, Fact-based.
        Current Market Focus: {market}
        Latest Intel: {intel}
        Compare DHA and Bahria if the user asks. 
        Always provide a 'Investment Verdict' (Buy/Hold/Sell) based on the data.
        """
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages
        )
        
        response = completion.choices[0].message.content
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
