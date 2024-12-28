import streamlit as st

def footer():
    """Renders the footer for the app."""
    st.markdown("---")
    html_attribution = """
        <div style="background-color:#28a745;padding:10px;margin-bottom:10px">
        <p style="color:white;text-align:center;font-size:20px;">Developed & Designed by Tejas Sinroja</p>
        </div>
        """
    st.markdown(html_attribution, unsafe_allow_html=True)