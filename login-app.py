import streamlit as st

# Predefined user credentials (for demo purposes)
USER_CREDENTIALS = {
    "user1": "password123",
    "admin": "adminpassword"
}

# Function to check login credentials
def login(username, password):
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return True
    else:
        return False

# Main function to render the login page
def login_page():
    st.title("Login Page")

    # Create a login form
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    # If login button is clicked
    if login_button:
        if login(username, password):
            st.success(f"Welcome, {username}!")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password. Please try again.")

# Main application content (only accessible after login)
def main_page():
    st.title("Welcome to the Main Application")
    st.write("This is the main content that is only accessible after login.")

# App execution flow
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    main_page()
