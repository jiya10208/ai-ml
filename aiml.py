import streamlit as st

st.title("Titanic Dataset")

# import numpy as np
# from matplotlib import pyplot as plt
# from sklearn.datasets import make_blobs

X = np.arange(1,9,5)



st.write("the random datasts")
st.line_chart(X)
