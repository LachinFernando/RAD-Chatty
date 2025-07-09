import streamlit as st

# Home page
st.title("Chatty 🤖")
st.subheader("Your personal assistant")
st.write("Chatty is a personal assistant that can help you with a variety of tasks.")

# Add a coral reef image
st.image("https://www.kommunicate.io/blog/wp-content/uploads/2023/07/Personalization-at-Scale-How-Chatbots-Drive-Customized-Customer-Experiences-1.png", caption="Chatty")

if not st.experimental_user.is_logged_in:
    if st.sidebar.button("Log in with Google", type="primary", icon=":material/login:"):
        st.login()
else:
    if st.sidebar.button("Log out", type="secondary", icon=":material/logout:"):
        st.logout()
        st.stop()