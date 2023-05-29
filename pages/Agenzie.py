import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Agenzie",
    layout="wide",
    initial_sidebar_state="expanded",

)


db_list = [1, 2, 3, 4, 5, 6, 7, 7]



st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

if st.button("premi", type="primary"):
    st.write(db_list)


