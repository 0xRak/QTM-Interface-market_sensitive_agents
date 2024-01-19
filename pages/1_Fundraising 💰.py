import streamlit as st
from UserInterface.plots import *
from UserInterface.helpers import ui_base

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one folder
parent_dir = os.path.abspath(os.path.join(os.path.abspath(current_dir), os.pardir))
# Append the parent directory to sys.path
sys.path.append(parent_dir)

ui_base(parent_dir)

st.sidebar.markdown("## Fundraising 💰")

# main page
st.markdown("## Fundraising 💰")

if 'param_id' in st.session_state:
    if st.session_state['param_id'] != "":
        plot_fundraising(st.session_state['param_id'])
