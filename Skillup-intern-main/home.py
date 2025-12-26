import streamlit as st
from db import get_connection

def app():
    st.title("📚 Library Home")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, category FROM books")
    books = cursor.fetchall()

    if books:
        st.subheader("Available Books")
        st.table(books)
    else:
        st.info("No books available")

    conn.close()
