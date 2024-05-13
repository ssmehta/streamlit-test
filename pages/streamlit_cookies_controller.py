import streamlit as st

# https://github.com/NathanChen198/streamlit-cookies-controller
from streamlit_cookies_controller import CookieController


name = 'streamlit_cookies_controller'


def get_cookie_controller():
    return CookieController()


controller = get_cookie_controller()

if st.button("Get All"):
    st.write(controller.getAll())
    st.write(st.session_state)

if st.button("Set"):
    controller.set(name, 'test')
    st.write(st.session_state)

if st.button("Get"):
    st.write(controller.get(name))
    st.write(st.session_state)

if st.button("Remove"):
    controller.remove(name)
    st.write(st.session_state)