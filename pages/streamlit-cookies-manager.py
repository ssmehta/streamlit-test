import streamlit as st

# https://github.com/ktosiek/streamlit-cookies-manager
from streamlit_cookies_manager import CookieManager


name = 'streamlit-cookies-manager'


def get_cookie_controller():
    return CookieManager()


controller = get_cookie_controller()

if not controller.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

if st.button("Get All"):
    st.write(controller._get_cookies())
    st.write(st.session_state)

if st.button("Set"):
    controller[name] = 'test'
    controller.save()
    st.write(st.session_state)

if st.button("Get"):
    st.write(controller[name])
    st.write(st.session_state)

if st.button("Remove"):
    del controller[name]
    controller.save()
    st.write(st.session_state)