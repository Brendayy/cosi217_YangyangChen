import streamlit as st
from ner import SpacyDocument

from model import graph

# st.sidebar.markdown('# Letters')
# letter = st.sidebar.radio('Pick a letter', ['a', 'b', 'c'])
# st.sidebar.info(f'Selected: {letter}')

st.markdown("## Yangyang's Spacy NER Display")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>{ner.get_entities_with_markup()}', unsafe_allow_html=True)


txt = st.text_area('Type something here...')
ner = SpacyDocument(txt)
if st.button('submit'):
    local_css("static/css/main.css")
'---'



# result = st.text_area('ner',ner.get_entities_with_markup())

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>{ner.get_entities_with_markup()}', unsafe_allow_html=True)

# local_css("static/css/main.css")


# if st.button('Show Animals'):
#     left, _spacer, right = st.columns([10,1,10])
#     left.write('Here is what we have in the zoo')
#     table_data = pd.DataFrame(['koalas','ole','dingos', 'rabbits'],[14,5,6,22])
#     left.table(table_data)
#     left.write('... with an unrelated chart')
#     chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
#     left.area_chart(chart_data)
#     right.write('And here is an unrelated graph')
#     right.graphviz_chart(graph)

