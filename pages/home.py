
import streamlit as st
from utils.components import *
from utils.functions import *

st.set_page_config(
    page_title="FitMetricks",
    page_icon="./assets/imgs/Fit_icon.ico",
    layout="wide",
)
def render():
    user = st.session_state['user_name']
    col1, col2, col3 = st.columns([0.2, 0.1, 1])

    col1.write(f"## Olá, {user}")
    col2.image("./assets/imgs/Fit_logo.png")

    component_effect_underline()
    st.write('## Bem Vindo ao Fit Metricks!')
    st.markdown('<div class="full-width-line-white"></div>', unsafe_allow_html=True)
    st.markdown('<div class="full-width-line-black"></div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,3,1])  # Cria uma coluna estreita e outra mais larga
    with col2:
        st.markdown(
            """
            #### O que é o Fit Metricks?
            Ele foi criado com o objetivo de calcular de forma fácil e gratuita métricas relacionadas ao seu treino.
            """,
            unsafe_allow_html=True,
        )

    tab1, = st.tabs(["Metricas"])

    with tab1:    
        st.write("Informe suas Metricas:")
        sex = st.radio(
        "Qual seu sexo?",
        ("Homem", "Mulher")
        )
        
        col1, col2 = st.columns([0.2, 1])  # Proporção para a imagem e inputs

        with col1:
            if sex == "Homem":
                st.image("./assets/imgs/Men_Measurements.png", use_column_width=True) 
            else:
                st.image("./assets/imgs/Woman_Measurements.png", use_column_width=True)

        with col2:
            neck, chest, waist, hip, thigh, calf, biceps, forearm = function_circumferences()

        height, weight, age = function_measures()

        if st.button("Calcular"):
            st.session_state.show_more = True

        if 'show_more' in st.session_state and st.session_state.show_more:
            row = st.columns(3) 
            tile1 = row[0].container(border=True)
            tile2 = row[1].container(border=True)
            tile3 = row[2].container(border=True)

            IMC = function_IMC_calc(height, weight, tile1, row)
            function_TMB_calc(sex, weight, height, age, tile2, row)
            function_water_calc(weight,tile3,row)

            row1 = st.columns([0.5,1,1,0.5])
            tile4 = row1[1].container(border=True)
            tile5 = row1[2].container(border=True)
            
            function_PFC_calc(sex, age, waist, hip, neck, height, IMC, weight, tile4, row1)
            function_PMM_calc(IMC, tile5, row1)

if __name__ == "__main__":
    component_hide_sidebar()
    component_fix_tab_echarts()

    if 'user_name' in st.session_state:
        render()