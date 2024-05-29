import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(
    page_title="Pywalker in Streamlit...",
    layout="wide"
)

updaloaded_file = st.file_uploader("your csv data")

if updaloaded_file is not None:
    df = pd.read_csv(updaloaded_file)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
