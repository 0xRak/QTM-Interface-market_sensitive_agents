import streamlit as st
from UserInterface.plots import *
from UserInterface.helpers import to_excel, ui_base, returnToStart

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one folder
parent_dir = os.path.abspath(os.path.join(os.path.abspath(current_dir), os.pardir))
# Append the parent directory to sys.path
sys.path.append(parent_dir)

if 'authentication_status' in st.session_state:
    if st.session_state["authentication_status"]:
        ui_base(parent_dir)

        st.sidebar.markdown("## Data 💾")

        # main page
        st.markdown("## Data 💾")
        st.markdown("### Full Timeseries Data")
        if 'param_id' in st.session_state:
            if st.session_state['param_id'] != "":
                df = get_simulation_data('simulationData.db', 'simulation_data_'+str(st.session_state['param_id']))
                st.dataframe(df)
                df_xlsx = to_excel(df)
                st.download_button(label='📥 Download Data as .xlsx',
                                        data=df_xlsx ,
                                        file_name= f"QTM_Results_{st.session_state['project_name']}.xlsx")
    else:
        returnToStart(parent_dir)
else:
    returnToStart(parent_dir)
