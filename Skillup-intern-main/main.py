import streamlit as st
from streamlit_option_menu import option_menu

import home, Studentlogin, Stafflogin, account, about

st.set_page_config(page_title="Library Management System", layout="wide")

class MultiApp:
    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Library Management System",
                options=["Home", "Student Login", "Staff Login", "Account", "About"],
                icons=["house", "person", "person-check", "person-circle", "info-circle"],
                default_index=0
            )

        if app == "Home":
            home.app()
        elif app == "Student Login":
            Studentlogin.app()
        elif app == "Staff Login":
            Stafflogin.app()
        elif app == "Account":
            account.app()
        elif app == "About":
            about.app()

app = MultiApp()
app.run()
