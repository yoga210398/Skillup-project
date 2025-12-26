import streamlit as st
from db import get_connection

def app():
    st.title("👤 Student Account")

    student_id = st.number_input("Enter Student ID", min_value=1, step=1)

    if st.button("View Account"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )
        student = cursor.fetchone()

        if student:
            st.write(f"**Name:** {student['name']}")
            st.write(f"**Email:** {student['email']}")
            st.write(f"**Department:** {student['department']}")
            st.write(f"**Year:** {student['year']}")
            st.write(f"**Last Login:** {student['last_login']}")
        else:
            st.error("Student not found")

        conn.close()
