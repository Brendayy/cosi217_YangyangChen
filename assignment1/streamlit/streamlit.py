import streamlit as st
from ner import SpacyDocument
import spacy_streamlit
from spacy_streamlit import visualize_tokens

st.markdown("## Yangyang's Spacy NER Display")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>{ner.get_entities_with_markup()}', unsafe_allow_html=True)


txt = st.text_area('Change the text here...', 
    "Marc Verhagen teaches at Brandeis in 2022. Yangyang has been doing NLP homework until 3pm.")
ner = SpacyDocument(txt)
models = ["en_core_web_sm"]
if st.button('submit'):
    local_css("static/css/main.css")
    # st.markdown(ner.pos())
    spacy_streamlit.visualize(models,txt)
    # visualize_tokens(ner.text, attrs=["text", "pos_", "dep_", "ent_type_"])
'---'

