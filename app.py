import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="💧",
    layout="wide",
)

st.title("💧 Hello from Streamlit Cloud")
st.caption("Deploy verification test")

col1, col2, col3 = st.columns(3)
col1.metric("Reservoirs", "1")
col2.metric("Months of data", "24")
col3.metric("Status", "Deployed ✅")

st.divider()

st.info("If you can see the metric cards above, the deploy pipeline works.")