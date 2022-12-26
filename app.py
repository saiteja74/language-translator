import streamlit as st
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

api_key = '7ch_BLkmCjplNEosb_w2oJyJjYCJN0-J-OSbJutwhDkn'
url = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/97de7be0-bf1f-40fc-a025-7cd7eab59266'

authenticator = IAMAuthenticator(apikey=api_key)

langtranslator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

langtranslator.set_service_url(url)

st.title("Language-Translator")

option = st.selectbox(
    'Select Language Here',
    ('English', 'Telugu', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean', 'Kannada', 'Japanese',
     'French', 'Italian', 'Urdu', 'Gujarati')
)

option1 = st.selectbox(
    'Select Language To Translate',
    ('English', 'Telugu', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean', 'Kannada', 'Japanese',
     'French', 'Italian', 'Urdu', 'Gujarati')
)

sent = "Enter the text in "+option+" and click translate button"

language_lib = {'English': 'en', 'German': 'de', 'Spanish': 'es', 'Korean': 'ko', 'Telugu': 'te', 'Hindi': 'hi', 'Arabic': 'ar'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):

    try:

        if option == option1:
            st.write("Please Select Different Language😥")

        else:

            translate_code = language_lib[option]+'-'+language_lib[option1]

            translation = langtranslator.translate(text=sentence, model_id=translate_code)

            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+'😁'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write("Please Type Selected Language😣")






