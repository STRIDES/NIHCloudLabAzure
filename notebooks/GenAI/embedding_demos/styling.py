import streamlit as st

def global_page_style():  
    st.set_page_config(layout="centered")  
    with open('style.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)