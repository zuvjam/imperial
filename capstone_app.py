import streamlit as st
import pandas as pd
import numpy as np

try:
    st.title("HeartSafe and SmartAlert production optimisation")

    with st.expander("About"):
        st.write("Use to simulate production and profit")
                    
    st.subheader("Optimisation Data Table")                 
 

    df=pd.read_csv("output_file.csv")
    df["SmartAlert"]=df["SmartAlert"].round(decimals=0).astype(int)
    df["HeartSafe"]=df["HeartSafe"].round(decimals=0).astype(int)
    df = df.sort_values(by="HeartSafe")
    st.write(df)

    HeartSafe_Units = st.slider("Choose number of HeartSafe to produce", min_value=0, max_value=6000, value=6000, step=1)
    SmartAlert_Units = st.slider("Choose number of SmartAlert to produce",min_value=0, max_value=4000, value=1400, step=1)

    resultdf = df.loc[(df["HeartSafe"] == HeartSafe_Units) & (df["SmartAlert"] == SmartAlert_Units)]
    
    # Display of the dataframe on screen
    # st.dataframe(resultdf)

    arrdf=resultdf.to_numpy()
    profit = arrdf[0,2]
    st.metric('Dollar ($)', profit)

except IndexError as e:
    st.info("The combination does not exist")
    HeartSafe_Units = 6000
    SmartAlert_Units = 1400