
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


