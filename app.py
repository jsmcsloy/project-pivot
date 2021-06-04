import pandas as pd
from pandas import DataFrame, read_csv
import streamlit as st
import numpy as np
import base64

#App to pretty up excel data 

st.title("Select Excel report")

in_file = st.file_uploader("Pick or drag in your file")


#create teh dataframe
try:
    df = pd.read_excel(in_file)



except:
    pass

try:

    df["Job Card Number"] = df["Job Card Number"].astype("category")

    allocation = pd.pivot_table(df, index=["Colorist","Project #"], columns = ["Job Card Type"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)
    projects =  pd.pivot_table(df, index=["Project #"], columns = ["Colorist"], values="Job Card Number", aggfunc=[len], fill_value=0 ,margins=True)





    st.subheader("Work Allocation")
    allocation
    st.subheader("Projects")
    projects


    # grp = df.groupby(["Project #"])
    # grp.describe()



    table = pd.pivot_table(df,index=["Colorist","Project #"], values=["Job Card Number"],aggfunc=[len],fill_value=0)
    writer = pd.ExcelWriter('output.xlsx')
    for manager in table.index.get_level_values(0).unique():
        temp_df = table.xs(manager, level=0)
        temp_df.to_excel(writer,manager)
    writer.save()


except:
    st.header("Not the file we are looking for, move along, move along..")




