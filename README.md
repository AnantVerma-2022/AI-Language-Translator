## Multilingual AI Translator (50 Languages)
An interactive AI-powered translator built with Streamlit and Facebook’s MBART-50 model. This app supports translation across 50 languages, making it a versatile tool for multilingual communication.

## Features
- Translate text between 50 languages using MBART-50.
- Simple and intuitive Streamlit UI.
- Cached model loading for faster performance.
- Clean, minimal design with a light sky-blue background.
- Error handling for empty input and identical source/target languages.

## Tech Stack
- Streamlit – for interactive web UI.
- PyTorch – deep learning framework.
- Transformers (huggingface.co in Bing) – Hugging Face library for MBART-50.
- MBART-50 (huggingface.co in Bing) – multilingual translation model.

## Installation
Clone the repository and install dependencies:
git clone https://github.com/your-username/ai-translator.git
cd ai-translator
pip install -r requirements.txt



##  Usage
Run the Streamlit app:
streamlit run app.py


Then open the local URL (usually http://localhost:8501) in your browser.

## Supported Languages
The app supports 50 languages, including:
- English, French, Spanish, German, Hindi, Chinese (Simplified), Japanese, Arabic, Russian, Portuguese, Turkish, Swahili, and many more.

## How It Works
- Select source and target languages.
- Enter text in the input box.
- Click Translate.
- The MBART-50 model generates the translation and displays it in the output box.

## Future Improvements
- Add swap button for quick language switching.
- Enable speech-to-text and text-to-speech.
- Save translation history.
- Deploy on Streamlit Cloud or Docker.

##  Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## Deployed
**Streamlit Deployement** --> https://ai-language-translator-iwqsebhhm4azrhcn2w6tj7.streamlit.app/
