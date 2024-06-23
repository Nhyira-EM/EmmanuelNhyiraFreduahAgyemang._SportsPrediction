import streamlit as st
from streamlit import runtime
import pandas as pd
import numpy as np
import pickle

st.title('Sports Prediction Group 27')

model = "C:/Users/Ato/OneDrive - Ashesi University/ASHESI/CS MAJOR/INTRO TO AI/Labs/AI Project/model.pkl"

md = pickle.load(open(model, 'rb'))

potential = st.number_input('Player Potential out of 100')
value_eur = st.number_input('Player Value in Euros')
wage_eur = st.number_input('Player Wage in Euros')
movement_reactions = st.number_input('Player Movement reactions')
shot_power = st.number_input('Shot Power out of 100')
passing = st.number_input('Passing out of 100')
dribbling = st.number_input('Dribbling out of 100')
movement = st.number_input('Movement out of 100')
mentality = st.number_input('Mentality out of 100')

prediction = md.predict([[potential,
value_eur,
wage_eur,
release_clause,
shot_power,
passing,
dribbling,
movement,
mentality]])


if st.button('Predict'):
    st.write("The predicted overall for your player is ", prediction[0])



