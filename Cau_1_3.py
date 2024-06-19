import streamlit as st

st.title('Random Words Generator')
st.header('Random Word')

st.markdown('### -')
st.text('Meaning: -')
st.write('Click the <span style="color: green;">Generate</span> button to generate new word', unsafe_allow_html=True)
st.button('Generate')

# Link web: https://21522120-cau1-3.streamlit.app/