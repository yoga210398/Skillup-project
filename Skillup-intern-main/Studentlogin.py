import streamlit as st
from db import get_connection
import datetime
import pandas as pd

def app():
    st.title("🎓 Student Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE email=? AND password=?",
            (email, password)
        )
        student = cursor.fetchone()

        if not student:
            st.error("Invalid email or password")
            return

        cursor.execute(
            "UPDATE students SET last_login=? WHERE student_id=?",
            (datetime.date.today(), student["student_id"])
        )
        conn.commit()

        st.success(f"Welcome {student['name']}")

        cursor.execute("""
            SELECT b.title, bi.issue_date
            FROM book_issues bi
            JOIN books b ON b.book_id = bi.book_id
            WHERE bi.student_id=?
        """, (student["student_id"],))

        data = cursor.fetchall()

        if data:
            df = pd.DataFrame(data, columns=["Book", "Issue Date"])
            df["Issue Date"] = pd.to_datetime(df["Issue Date"])

            st.subheader("📖 Borrowed Books")
            st.table(df)

            st.subheader("📊 Reading Activity")
            st.line_chart(df.groupby("Issue Date").count())
        else:
            st.info("No books borrowed")

        conn.close()
