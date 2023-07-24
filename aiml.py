import streamlit as st

st.title("Titanic Dataset")

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

X,y = make_blobs(n_samples=500,n_features=2,centers=3,random_state=3)



st.write("the random datasts")
st.line_chart(X)
st.line_chart(y)



st.write(y.shape)
st.write(X.shape)



data= data.drop( columns= (['Name','Ticket','Fare','Embarked', 'Parch', 'SibSp', 'Cabin' ] ))

st.write("after making some changes like dropping some of the not very useful rows")
st.line_chart(data)


plt.scatter(X[:,0], X[:, 1])
plt.show()
