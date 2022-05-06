import streamlit as st
from pages import (
    home,
    data_info,
    reg_preprocessing,
    prediction,
    reg_training,
    reg_model_analysis,
    cls_preprocessing,
    cls_training,
    cls_model_analysis,
    cluster_preprocessing,
    cluster_training,
    cluster_model_analysis,
)

# from utils.session import _get_state
from pathlib import Path
from utils.image_loader import *


PAGES = {
    "Home": home,
    "DataInfo": data_info,
    "Preprocessing": (reg_preprocessing, cls_preprocessing, cluster_preprocessing),
    "Training": (reg_training, cls_training, cluster_training),
    "Model Performance Analysis": (
        reg_model_analysis,
        cls_model_analysis,
        cluster_model_analysis,
    ),
    # "Prediction and Save": prediction,
}

IMAGE_FOLDER = Path("images/")


def run():
    # state = _get_state()
    state = st.session_state
    st.set_page_config(
        page_title="Give Everybody MachineLearning",
        layout="centered",
        page_icon= str(IMAGE_FOLDER / "gem_logo.png"),
        initial_sidebar_state="expanded",
    )
    load_nav_image(IMAGE_FOLDER / "gem_logo.png")

    st.title("Give Everybody MachineLearning")
    st.markdown(
        "Please check github repo here :point_right: [gem github repo](https://github.com/WangCHEN9/gem)"
    )
    st.markdown("""---""")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("To be done step by step", list(PAGES.keys()))

    if selection == "Home":
        try:
            state_df, task = PAGES[selection].write(state)
            state.df, state.task = state_df, task

            state.log_history = {}
            state.is_remove = False
            state.ignore_columns = []
        except:
            st.header("Please Upload Csv or Excel File first!")
            st.stop()
    if selection == "DataInfo":
        try:
            PAGES[selection].write(state.df)
        except AttributeError:
            st.error("Please Upload Csv or Excel File first!")

    if selection == "Preprocessing":
        try:
            if state.task == "Regression":
                PAGES[selection][0].write(state)
            elif state.task == "Classification":
                PAGES[selection][1].write(state)
            else:
                PAGES[selection][2].write(state)
        except AttributeError:
            st.error("Please Upload Csv or Excel File first!")

    if selection == "Training":
        try:
            if state.task == "Regression":
                PAGES[selection][0].write(state)
            elif state.task == "Classification":
                PAGES[selection][1].write(state)
            else:
                PAGES[selection][2].write(state)
        except AttributeError:
            st.error("Please Upload Csv or Excel File first!")

    if selection == "Model Performance Analysis":
        try:
            if state.task == "Regression":
                PAGES[selection][0].write(state)
            elif state.task == "Classification":
                PAGES[selection][1].write(state)
            else:
                PAGES[selection][2].write(state)
        except AttributeError:
            st.error("Please Upload Csv or Excel File first!")
    if selection == "Prediction and Save":
        try:
            PAGES[selection].write(state)
        except AttributeError:
            st.error("Please Upload Csv or Excel File first!")

    # state.sync()


if __name__ == "__main__":
    run()
