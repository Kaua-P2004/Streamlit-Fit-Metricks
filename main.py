import streamlit as st
from utils.components import component_hide_sidebar

def show_login_page():
    col1, col2 = st.columns([4, 1])
    col1.write("## FitMetrics")
    col2.image("./assets/imgs/Fit_logo.png", width=50)

    # Captura o nome do usuário
    user = st.text_input("Digite seu Nome:")

    if st.button("Entrar"):
        if user:  # Verifica se o usuário digitou algo
            st.session_state['user_name'] = user  # Armazena na sessão
            st.switch_page("pages/home.py")
        else:
            st.warning("Por favor, digite seu nome.")


if __name__ == "__main__":
    st.set_page_config(
        page_title="FitMetricks",
        page_icon="./assets/imgs/Fit_icon.ico",
        layout="centered",
    )

    component_hide_sidebar()
    if 'user_name' not in st.session_state:
        show_login_page()
    else:
        st.success(f"Bem-vindo de volta, {st.session_state['user_name']}!")