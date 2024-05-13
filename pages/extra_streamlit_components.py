import streamlit as st

# https://github.com/Mohamed-512/Extra-Streamlit-Components
import extra_streamlit_components as stx


name = 'extra_streamlit_components'


def get_cookie_controller():
    return stx.CookieManager()


controller = get_cookie_controller()

if st.button("Get All"):
    st.write(controller.get_all())
    st.write(st.session_state)

if st.button("Set"):
    controller.set(name, 'test')
    st.write(st.session_state)

if st.button("Get"):
    st.write(controller.get(name))
    st.write(st.session_state)

if st.button("Remove"):
    controller.delete(name)
    st.write(st.session_state)