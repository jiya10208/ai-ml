import streamlit as st

st.title("Titanic Dataset")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

model= LinearRegression()
model1=LogisticRegression()
data=pd.read_csv("titanic.csv?dl=0")

st.write("the titanic datasts")
st.line_chart(data)

st.write("the columns having nan values")
st.line_chat(data.isna().sum())



data= data.drop( columns= (['Name','Ticket','Fare','Embarked', 'Parch', 'SibSp', 'Cabin' ] ))

st.write("after making some changes like dropping some of the not very useful rows")
st.line_chart(data)
