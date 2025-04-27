import pickle
import pandas as pd
import gradio as gr

# Load the model from the .pkl file
model = pickle.load(open('best_inflation_model.pkl', 'rb'))

# Function to make predictions
def make_prediction(input_data):
    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)
    return prediction

