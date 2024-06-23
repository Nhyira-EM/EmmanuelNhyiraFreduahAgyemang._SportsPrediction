
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="Nhyira/FIFA-Model", filename="fifa_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)


# Main program for Streamlit to use
def main():
    st.title("FIFA Player Rating Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Sports Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)


    potential = st.number_input('Player Potential out of 100',1, 100, 1)
    value_eur = st.number_input('Player Value in Euros')
    wage_eur = st.number_input('Player Wage in Euros')
    movement_reactions = st.number_input('Player Movement reactions out of 100'1, 100, 1)
    passing = st.number_input('Passing out of 100')
    dribbling = st.number_input('Dribbling out of 100'1, 100, 1)


    if st.button('Predict'):
        data = {
            'potential': [potential],
            'value_eur': [value_eur],
            'wage_eur': [wage_eur],
            'movement_reactions': [movement_reactions],
            'passing': [passing],
            'dribbling': [dribbling]
        }

        # Making into a DataFrame
        df = pd.DataFrame(data)
        
        # Ensure the DataFrame has the same columns as the model expects
        expected_features = model.feature_names_in_
        for feature in expected_features:
            if feature not in df.columns:
                df[feature] = 0  # or some default value

        df = df[expected_features]  # Reorder columns to match model's expectation
        
        prediction = model.predict(df)
        st.write("The predicted overall for your player is ", prediction[0])

if __name__ == '__main__':
    main()
