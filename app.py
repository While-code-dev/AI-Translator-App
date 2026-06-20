import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Translator App",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI-Powered Translator")
st.markdown("Translate text between multiple languages instantly.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys()),
        index=0
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter text to translate",
    height=180,
    placeholder="Type or paste text here..."
)

if st.button("🔄 Translate", use_container_width=True):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation completed!")

            st.subheader("Translated Text")
            st.text_area(
                "",
                value=translated,
                height=180
            )

        except Exception as e:
            st.error(f"Translation failed: {e}")

st.markdown("---")
st.caption("Built with Streamlit and Deep Translator")