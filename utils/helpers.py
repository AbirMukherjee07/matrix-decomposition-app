import streamlit as st
import numpy as np
import pandas as pd
def display_matrix(matrix, name):
    st.write(f"**Matrix {name}:**")
    real = np.real(matrix) if np.iscomplexobj(matrix) else matrix
    st.dataframe(pd.DataFrame(np.round(real, 4)), use_container_width=False)