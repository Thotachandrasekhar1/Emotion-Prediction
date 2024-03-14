import streamlit as st
import pickle

st.title("Emotion Detection Using ML")
text = st.text_input("Enter the Text")
import os
script_path = os.path.abspath(__file__)

os.chdir(os.path.dirname(script_path))

model_folder = "model"

model_file_path = os.path.join(model_folder, 'chandu_linked.pkl')

with open(model_file_path, 'rb') as model_file:

    model = pickle.load(model_file)

# Construct the file path using os.path.join()




btn = st.button("Submit")

resul = model.predict([text])
result = resul[0]

if btn == True:

    if result == 'anger':
        st.image(r'https://freepngimg.com/thumb/angry_emoji/36886-1-angry-emoji-photo-thumb.png')
    elif result == 'love':
        st.image(r'https://freepngimg.com/thumb/emoji/64989-emoticon-heart-love-emoji-png-free-photo-thumb.png')
    elif result == 'joy':
        st.image(r'https://static.vecteezy.com/system/resources/thumbnails/029/138/681/small/happy-emoji-happy-emoji-happy-emoji-transparent-background-ai-generative-free-png.png')
    elif result == 'sad':
        st.image(r'https://freepngimg.com/thumb/sad_emoji/36860-2-sad-emoji-transparent-image-thumb.png')
    elif result == 'surprise':
        st.image(r'https://static.vecteezy.com/system/resources/thumbnails/009/665/371/small/emoticon-shocked-face-png.png')
    elif result == 'fear':
        st.image(r'https://static.vecteezy.com/system/resources/thumbnails/009/885/115/small/fearful-face-emoji-3d-illustration-png.png')
    st.subheader(f'Prediction: {result}')