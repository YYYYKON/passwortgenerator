import streamlit as st
import random
from streamlit_copy_button import copy_button

st.title("🔐 Passwort Generator")

laenge = st.slider("Länge", 4, 30, 12)

sonderzeichen = st.checkbox("Sonderzeichen benutzen")

if st.button("Generieren"):
    zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    if sonderzeichen:
        zeichen += "€&@?!$£¥#%"

    passwort = ""

    for i in range(laenge):
        passwort += random.choice(zeichen)

    st.success(passwort)

    copy_button(
        passwort,
        "📋 Passwort kopieren"
    )
