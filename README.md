# Language Translation Tool

## Overview
The Language Translation Tool is a web application built with Streamlit that leverages the MarianMT model for translating text between different languages. Users can input text and select source and target languages to get real-time translations.

## Features
- Supports multiple languages including English, French, Spanish, German, and more.
- User-friendly interface for easy interaction.
- Utilizes the Hugging Face Transformers library for translation.

## How It Works
1. Users input the text they wish to translate.
2. The user selects the source and target languages from dropdown menus.
3. Upon clicking the "Translate" button, the application uses the MarianMT model to provide translations.
4. The translated text is displayed below the input area.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd translation_tool

Install the required packages:
pip install streamlit transformers

Run the application:
streamlit run translation_tool.py

Usage

Enter the text you want to translate in the text area.
Select the source language and target language.
Click the "Translate" button to see the translated text.
