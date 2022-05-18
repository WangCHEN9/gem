import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

def write(state):
    with st.spinner("Loading Home ..."):
        task_type = st.radio("Please Select the Task Type: ", options=[
            "Regression", 
            "Classification", 
            # "Clustering",  #remove this feature for the moment
            ])
        state = st.file_uploader('Upload csv file for project', type=["csv", "xlsx"])
        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')
        csv = convert_df(pd.read_csv(r'./public/delaney_solubility_with_descriptors.csv'))
        st.download_button(
            label="Download Example CSV file",
            data=csv,
            file_name='example_for_gem.csv',
            mime='text/csv',
        )
        if state is not None:
            file_extension = state.name.split('.')[1]
            if file_extension == "csv":
                state.df = pd.read_csv(state)
            else:
                state.df = pd.read_excel(state)
            st.header("The First 20 Rows of Data")
            #st.table(state.df.head(20))
            AgGrid(state.df.head(20))
            
            if state.df is not None:
                state.task_type=task_type
                return state.df, state.task_type
            return state.df,"No Defined"


