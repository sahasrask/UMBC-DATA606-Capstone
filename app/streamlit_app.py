import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Loaded the pre-trained model
model = load_model('nmt_model.weights.h5')

with open('sanskrit_data.pkl', 'rb') as f:
    sanskrit_tokenizer = pickle.load(f)
with open('eng_data.pkl', 'rb') as f:
    english_tokenizer = pickle.load(f)

# Maximum input length for the translation
max_input_length = 50

# Streamlit App UI
st.title("Sanskrit to English Translator")
st.write("Enter Sanskrit text below to translate it into English.")

# Text input for Sanskrit
sanskrit_input = st.text_area("Sanskrit Text", placeholder="Enter Sanskrit text here...")

# Translation function
def translate(sanskrit_text):
   
    input_sequence = sanskrit_tokenizer.texts_to_sequences([sanskrit_text])
    input_sequence = tf.keras.preprocessing.sequence.pad_sequences(input_sequence, maxlen=max_input_length, padding='post')

    # Predict using the model
    prediction = model.predict(input_sequence)
    predicted_sequence = np.argmax(prediction, axis=-1)

    # Convert predicted sequence back to English
    translated_text = english_tokenizer.sequences_to_texts(predicted_sequence)[0]
    return translated_text

# Translate when the button is clicked
if st.button("Translate"):
    if sanskrit_input.strip() == "":
        st.warning("Please enter some Sanskrit text to translate.")
    else:
        english_translation = translate(sanskrit_input)
        st.subheader("English Translation:")
        st.write(english_translation)
