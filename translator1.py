import streamlit as st
import torch
from transformers import MBartForConditionalGeneration, MBart50Tokenizer

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #e6f7ff;  /* light sky blue */
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.set_page_config(page_title="AI Translator", page_icon="🌍")
st.title("🌍 Multilingual AI Translator (50 Languages)")
st.write("Powered by MBART-50")

# The @st.cache_resource decorator in Streamlit is used to cache global resources that are expensive to create, such as machine learning models, database connections, or other objects that are not easily serializable

@st.cache_resource
def load_model():
    tokenizer = MBart50Tokenizer.from_pretrained(
        "facebook/mbart-large-50-many-to-many-mmt"
    )
    model = MBartForConditionalGeneration.from_pretrained(
        "facebook/mbart-large-50-many-to-many-mmt"
    )
    return tokenizer, model

tokenizer, model = load_model()

# All MBART-50 languages
LANGUAGES = {
    "Arabic": "ar_AR",
    "Czech": "cs_CZ",
    "German": "de_DE",
    "English": "en_XX",
    "Spanish": "es_XX",
    "Estonian": "et_EE",
    "Finnish": "fi_FI",
    "French": "fr_XX",
    "Gujarati": "gu_IN",
    "Hindi": "hi_IN",
    "Italian": "it_IT",
    "Japanese": "ja_XX",
    "Kazakh": "kk_KZ",
    "Korean": "ko_KR",
    "Lithuanian": "lt_LT",
    "Latvian": "lv_LV",
    "Burmese": "my_MM",
    "Nepali": "ne_NP",
    "Dutch": "nl_XX",
    "Romanian": "ro_RO",
    "Russian": "ru_RU",
    "Sinhala": "si_LK",
    "Turkish": "tr_TR",
    "Vietnamese": "vi_VN",
    "Chinese (Simplified)": "zh_CN",
    "Afrikaans": "af_ZA",
    "Azerbaijani": "az_AZ",
    "Bengali": "bn_IN",
    "Persian": "fa_IR",
    "Hebrew": "he_IL",
    "Croatian": "hr_HR",
    "Indonesian": "id_ID",
    "Georgian": "ka_GE",
    "Khmer": "km_KH",
    "Macedonian": "mk_MK",
    "Malayalam": "ml_IN",
    "Mongolian": "mn_MN",
    "Marathi": "mr_IN",
    "Polish": "pl_PL",
    "Pashto": "ps_AF",
    "Portuguese": "pt_XX",
    "Swedish": "sv_SE",
    "Swahili": "sw_KE",
    "Tamil": "ta_IN",
    "Telugu": "te_IN",
    "Thai": "th_TH",
    "Tagalog": "tl_XX",
    "Ukrainian": "uk_UA",
    "Urdu": "ur_PK",
    "Xhosa": "xh_ZA",
    "Galician": "gl_ES",
    "Slovenian": "sl_SI"
}

# UI Layout
col1, col2 = st.columns(2)

with col1:
    src_language = st.selectbox("Source Language", list(LANGUAGES.keys()))

with col2:
    tgt_language = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1)

# Swap button
#if st.button("🔁 Swap Languages"):
#    src_language, tgt_language = tgt_language, src_language

text = st.text_area("Enter text:", height=150)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    elif src_language == tgt_language:
        st.warning("Source and target languages must be different.")
    else:
        with st.spinner("Translating..."):
            tokenizer.src_lang = LANGUAGES[src_language]
            inputs = tokenizer(text, return_tensors="pt")

            translated_tokens = model.generate(
                **inputs,
                forced_bos_token_id=tokenizer.lang_code_to_id[LANGUAGES[tgt_language]]
            )

            translation = tokenizer.batch_decode(
                translated_tokens,
                skip_special_tokens=True
            )[0]

        st.success("Translation")
        st.text_area("Output:", translation, height=150)