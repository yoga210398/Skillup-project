import streamlit as st
from db import get_connection
import datetime

def app():
    st.title("👩‍🏫 Staff Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM staff WHERE email=? AND password=?",
            (email, password)
        )
        staff = cursor.fetchone()

        if not staff:
            st.error("Invalid email or password")
            return

        cursor.execute(
            "UPDATE staff SET last_login=? WHERE staff_id=?",
            (datetime.date.today(), staff["staff_id"])
        )
        conn.commit()

        st.success(f"Welcome {staff['name']} ({staff['role']})")

        st.subheader("📚 Issued Books")

        cursor.execute("""
            SELECT s.name AS student, b.title AS book, bi.issue_date, bi.return_date
            FROM book_issues bi
            JOIN students s ON s.student_id = bi.student_id
            JOIN books b ON b.book_id = bi.book_id
        """)

        rows = cursor.fetchall()

        for r in rows:
            st.write(f"👤 {r['student']} | 📖 {r['book']} | 📅 {r['issue_date']}")

        conn.close()
