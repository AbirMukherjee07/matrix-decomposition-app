import streamlit as st
import numpy as np
import pandas as pd

from decomposition.lu import LU_decom
from decomposition.eigen import EVD_decom
from decomposition.svd import SVD_decom
from decomposition.qr import QR_decom
from decomposition.cholesky import Cholesky_decom
from decomposition.pca import PCA_decom

from utils.helpers import display_matrix
from utils.validators import validate_cholesky
from utils.validators import validate_eva


st.set_page_config(page_title="Matrix Decomposition Visualizer", layout="wide")
st.title("Matrix Decomposition Visualizer")
st.markdown("Enter a matrix, choose a decomposition method, and view the results.")

st.sidebar.header("1. Matrix Input Section")

rows = st.sidebar.number_input("Number of Rows", min_value=1, max_value=5, value=3, step=1)
cols = st.sidebar.number_input("Number of Columns", min_value=1, max_value=5, value=3, step=1)

st.sidebar.markdown("### Enter Matrix Values")

default_df = pd.DataFrame(np.zeros((rows, cols)))

edited_df = st.sidebar.data_editor(
    default_df,
    use_container_width=True,
    num_rows="fixed",
    hide_index=True
)

A = edited_df.to_numpy(dtype=float)

st.sidebar.header("2. Select Decomposition")
method = st.sidebar.selectbox(
    "Choose a method:",
    ["LU Decomposition", "QR Decomposition", "Eigenvalue Decomposition", "Singular Value Decomposition (SVD)", "Cholesky Decomposition","PCA Decomposition"]
)
st.header("Results")
st.subheader("Original Matrix (A)")
st.dataframe(pd.DataFrame(A))

if st.sidebar.button("Compute Decomposition"):
    try:
        if method == "LU Decomposition":
            st.markdown("### LU Decomposition ($A = P L U$)")
            P, L, U = LU_decom(A)
            col1, col2, col3 = st.columns(3)
            with col1:
                display_matrix(P, "P (Permutation)")
            with col2:
                display_matrix(L, "L (Lower Triangular)")
            with col3:
                display_matrix(U, "U (Upper Triangular)")

        elif method == "QR Decomposition":
            st.markdown("### QR Decomposition ($A = Q R$)")
            Q, R = QR_decom(A)
            col1, col2 = st.columns(2)
            with col1:
                display_matrix(Q, "Q (Orthogonal)")
            with col2:
                display_matrix(R, "R (Upper Triangular)")

        elif method == "Eigenvalue Decomposition":
            st.markdown("### Eigenvalue Decomposition ($A V = V \\Lambda$)")
            valid,message=validate_eva(A)
            if valid:
                eigenvalues, eigenvectors = EVD_decom(A)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Eigenvalues:**")
                    eig_df = pd.DataFrame({
                        "Real": np.round(np.real(eigenvalues), 4),
                        "Imaginary": np.round(np.imag(eigenvalues), 4)
                    })
                    st.dataframe(eig_df)
                with col2:
                    display_matrix(eigenvectors, "V (Eigenvectors)")
            else:
                st.error(message)

        elif method == "Singular Value Decomposition (SVD)":
            st.markdown("### Singular Value Decomposition ($A = U \\Sigma V^T$)")
            U, S, VT = SVD_decom(A)
            Sigma = np.zeros((A.shape[0], A.shape[1]))
            np.fill_diagonal(Sigma, S[:min(A.shape)])
            col1, col2, col3 = st.columns(3)
            with col1:
                display_matrix(U, "U")
            with col2:
                display_matrix(Sigma, "Σ (Singular Values)")
            with col3:
                display_matrix(VT, "V^T")

        elif method == "Cholesky Decomposition":
            st.markdown("### Cholesky Decomposition ($A = L L^T$)")
            valid, message = validate_cholesky(A)
            if valid:
                L = Cholesky_decom(A)
                col1, col2 = st.columns(2)
                with col1:
                    display_matrix(L, "L (Lower Triangular)")
                with col2:
                    display_matrix(L.T, "L^T (Upper Triangular)")
            else:
                st.error(message)

        elif method == "PCA Decomposition":
            st.markdown("### Principal Component Analysis (PCA)")
            components, explained_variance, transformed_data = PCA_decom(A)
            col1, col2, col3 = st.columns(3)
            with col1:
                display_matrix(components, "Principal Components")
            with col2:
                st.write("**Explained Variance:**")
                st.dataframe(
                    pd.DataFrame(
                        np.round(explained_variance, 4),
                        columns=["Variance"]
                    ),
                    width="content"
                )
            with col3:
                display_matrix(transformed_data, "Transformed Data")

    except np.linalg.LinAlgError as e:
        st.error(f"Linear Algebra Error: {e}")
        st.info("Make sure the matrix meets the mathematical requirements for the chosen decomposition (e.g., positive definite for Cholesky).")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    