import streamlit as st
from streamlit import runtime
import pandas as pd
import numpy as np
import pickle

st.title('Sports Prediction EMFA')

model = "C:/Users/nhyir/Documents/INTRO TO AI/EmmanuelNhyiraFreduahAgyemang._SportsPrediction"

md = pickle.load(open(model, 'rb'))

potential = st.number_input('Player Potential out of 100')
value_eur = st.number_input('Player Value in Euros')
wage_eur = st.number_input('Player Wage in Euros')
movement_reactions = st.number_input('Player Movement reactions out of 100')
passing = st.number_input('Passing out of 100')
dribbling = st.number_input('Dribbling out of 100')

prediction = md.predict([[potential,
value_eur,
wage_eur,
movement_reactions,
passing,
dribbling]])


if st.button('Predict'):
    st.write("The predicted overall for your player is ", prediction[0])



