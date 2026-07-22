import streamlit as st
import random

st.title("🔐 Passwort Generator")

laenge = st.slider("Länge", 4, 30, 12)

sonderzeichen = st.checkbox("Sonderzeichen benutzen")
zahlen = st.checkbox("Zahlen benutzen")

if st.button("Generieren"):
    zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    if sonderzeichen:
        zeichen += "€&@?!$£¥#%"
    if zahlen:
        zeichen += "0123456789"

    passwort = ""

    for i in range(laenge):
        passwort += random.choice(zeichen)

    st.code(passwort)


    
