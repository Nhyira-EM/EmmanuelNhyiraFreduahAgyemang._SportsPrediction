import streamlit as st
import pandas as pd
import numpy as np
import pickle
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(repo_id="Nhyira-EM/FIFA-Model", filename="fifa_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Main program for Streamlit to use
def main():
    st.title("FIFA Player Rating Predictor")
    html_temp = """
    <div style="background:#ADD8E6; padding:10px">
    <h2 style="color:black; text-align:center;">Sports Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    potential = st.number_input('Player Potential out of 100', 1, 100, 1)
    movement_reactions = st.number_input('Player Movement reactions out of 100', 1, 100, 1)
    passing = st.number_input('Passing out of 100',1, 100, 1)
    wage_eur = st.number_input('Player Wage in Euros')
    value_eur = st.number_input('Player Value in Euros')
    dribbling = st.number_input('Dribbling out of 100', 1, 100, 1)

    if st.button('Predict'):
        data = {
            'potential': [potential],
            'movement_reactions': [movement_reactions],
            'passing': [passing],
            'wage_eur': [wage_eur],
            'value_eur': [value_eur],
            'dribbling': [dribbling]
        }

        # Making into a DataFrame
        df = pd.DataFrame(data)

        # Ensure the DataFrame has the same columns as the model expects
        expected_features = [
            'potential', 'movement_reactions', 'passing', 'wage_eur', 'value_eur', 'dribbling'
        ]
        
        for feature in expected_features:
            if feature not in df.columns:
                df[feature] = 0  # or some default value

        df = df[expected_features]  # Reorder columns to match model's expectation

        prediction = model.predict(df)
        st.write("The predicted overall for your player is ", prediction[0])

if __name__ == '__main__':
    main()