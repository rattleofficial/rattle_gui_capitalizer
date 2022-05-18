import streamlit as sl
sl.title('Rattle capitalizer')
inp=sl.text_area('Enter the text to capitalize:')
if sl.button('Capitalize!'):
    sl.header(inp.upper())