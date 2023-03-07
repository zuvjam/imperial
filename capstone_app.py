# Zuveir Jameer
# 7 March 2023

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

try:
    feasibilityChart = Image.open('Feasibility_Chart.jpg')
    HS_default = 6000
    SA_default = 1400
    
    def synchdata():
        HS_units = st.session_state["HS_key"]
        if st.session_state["HS_key"] > 2285 and st.session_state["HS_key"] <6000:
            sessiondf = df.loc[(df["HeartSafe"] == HS_units)]
            arrdf=sessiondf.to_numpy()
            SA_units = arrdf[0,1]
            st.session_state.SA_key = SA_units
        else:
            pass
        return
    
    st.title("HeartSafe and SmartAlert production optimisation")

    with st.expander("About"):
        st.write("Use to simulate production and profit")
        st.image(image=feasibilityChart)
                    
    df=pd.read_csv("output_file.csv")
    df["SmartAlert"]=df["SmartAlert"].round(decimals=0).astype(int)
    df["HeartSafe"]=df["HeartSafe"].round(decimals=0).astype(int)
    df = df.sort_values(by="HeartSafe")
    
    # Display of the dataframe table on screen for debugging
    # st.subheader("Optimisation Data Table")  
    # st.write(df)

    HeartSafe_Units = st.slider("Choose number of HeartSafe to produce", min_value=0, max_value=6000, value=HS_default, step=1, key="HS_key" , on_change= synchdata)
    SmartAlert_Units = st.slider("Choose number of SmartAlert to produce",min_value=0, max_value=4000, value=SA_default, key="SA_key", step=1)

    resultdf = df.loc[(df["HeartSafe"] == HeartSafe_Units) & (df["SmartAlert"] == SmartAlert_Units)]
    
    # Display of the dataframe on screen for debugging
    # st.dataframe(resultdf)

    arrdf=resultdf.to_numpy()
    profit = arrdf[0,2]
    st.metric('Dollar ($)', profit)

except IndexError as e:
    st.info("The combination does not exist")
    HeartSafe_Units = HS_default
    SmartAlert_Units = SA_default