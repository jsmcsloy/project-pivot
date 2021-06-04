

import pandas as pd
from pandas import DataFrame, read_csv
import streamlit as st
import numpy as np
import base64

#App to pretty up excel data 

st.title("Report processor v1")

st.sidebar.header("Project Processor")

in_file = st.sidebar.file_uploader("Pick or drag in your file", type="xlsx", engine='openpyxl')

project_button = st.sidebar.button("Process")

if project_button == True:
    df = pd.read_excel(in_file)
       

    df["Job Card Number"] = df["Job Card Number"].astype("category")
    allocation = pd.pivot_table(df, index=["Colorist","Project #"], columns = ["Job Card Type"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)
    projects =  pd.pivot_table(df, index=["Project #"], columns = ["Colorist"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)
    
    st.subheader("Work Allocation")
    allocation
    st.subheader("Projects #")
    projects



    # #create teh dataframe
    # try:
    #     df = pd.read_excel(in_file)
    #     print('read ok')


    # except:
    #     print ('failed 1')
    #     pass


    # try:

    #     df["Job Card Number"] = df["Job Card Number"].astype("category")

    #     allocation = pd.pivot_table(df, index=["Colorist","Project #"], columns = ["Job Card Type"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)
    #     projects =  pd.pivot_table(df, index=["Project #"], columns = ["Colorist"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)





    #     st.subheader("Work Allocation")
    #     allocation
    #     st.subheader("Projects #")
    #     projects


    #     # grp = df.groupby(["Project #"])
    #     # grp.describe()



    


    # except:
    #     st.header("Not the file we are looking for, move along, move along..")




