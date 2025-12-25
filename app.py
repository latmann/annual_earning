import streamlit as st
from salary_predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox('Explorer or Predict', ('Predict', 'Explorer'))

if page == 'Predict':
    show_predict_page()
else:
    show_explore_page()