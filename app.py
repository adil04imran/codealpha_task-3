from transformers import MarianMTModel, MarianTokenizer
import streamlit as st

# Load the pre-trained MarianMT model and tokenizer
def load_model(src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer

# Function to translate text locally
def translate_text(text, src_lang='en', tgt_lang='fr'):
    model, tokenizer = load_model(src_lang, tgt_lang)
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Streamlit UI for local translation
st.title("Language Translation Tool")

# Input text
text_to_translate = st.text_area("Enter the text you want to translate")

# Extended language options
language_options = {
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Italian': 'it',
    'Dutch': 'nl',
    'Russian': 'ru',
    'Chinese': 'zh',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Portuguese': 'pt',
    'Arabic': 'ar',
    'Hindi': 'hi',
    'Bengali': 'bn'
}

# Language selection
source_lang = st.selectbox("Select source language", options=language_options.keys())
target_lang = st.selectbox("Select target language", options=language_options.keys())

# Translate button
if st.button("Translate"):
    if text_to_translate:
        src_lang_code = language_options[source_lang]
        tgt_lang_code = language_options[target_lang]
        translated_text = translate_text(text_to_translate, src_lang=src_lang_code, tgt_lang=tgt_lang_code)
        st.success(f"Translated Text: {translated_text}")
    else:
        st.error("Please enter text to translate")
