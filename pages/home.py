import streamlit as st
from utils.components import *
from utils.functions import *

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
            col2_1 = st.columns(3)  

            with col2_1[0]:
                neck = st.number_input("Circunferência do Pescoço (CM):", min_value=1, key="neck")

            with col2_1[1]:
                chest = st.number_input("Circunferência do Peito (CM):", min_value=1, key="chest")

            with col2_1[2]:
                waist = st.number_input("Circunferência da Cintura (CM):", min_value=1, key="waist")

            col2_2 = st.columns(3) 

            with col2_2[0]:
                hip = st.number_input("Circunferência do Quadril (CM):", min_value=1, key="hip")

            with col2_2[1]:
                thigh = st.number_input("Circunferência da Coxa (CM):", min_value=1, key="thigh")

            with col2_2[2]:
                calf = st.number_input("ircunferência da Panturrilha (CM):", min_value=1, key="calf")
            
            col2_3 = st.columns(4)

            with col2_3[1]:
                aa = st.number_input("Circunferência do Quadril (CM):", min_value=1, key="aa")

            with col2_3[2]:
                thaigh = st.number_input("Circunferência da Coxa (CM):", min_value=1, key="thaigh")
        
        col3 = st.columns(3)
        with col3[0]:
            height = st.number_input("Digite sua Altura (CM):",min_value=1)
        with col3[1]:
            weight = st.number_input("Digite seu Peso (KG):",min_value=1.00)
        with col3[2]:
            age = st.number_input("Digite sua idade:", min_value=0, format="%d")
        
        if st.button("Calcular"):
            st.session_state.show_more = True

        if 'show_more' in st.session_state and st.session_state.show_more:
            
            row = st.columns(3)
            tile = row[0].container(border=True)
            heightIMC = height/ 100
            IMC = weight / (heightIMC ** 2)
            tile.write(f"<p style='text-align: center;'>IMC (Índice de Massa Corporal)</br>{IMC:.2f}</p>", unsafe_allow_html=True)
            row[0].write("##### Explicação:")

            if IMC < 18.5:
                col1 , col2, = row[0].columns([1, 1])
                with col1: st.write("Você está abaixo do peso:")
                with col2: st.write("A recomendação é procurar um Medico para avaliação do Resultado")
            
            elif 18.5 <= IMC < 24.9:
                col1 , col2, = row[0].columns([1, 1])
                with col1: st.write("Você está no peso ideal:")
                with col2: st.write("Aparentemente está tudo certo, porém é muito importante avalisar outros fatores, como circunferência abdominal maior ou com uma quantidade de gordura acima do ideial")
            
            elif 25 <= IMC < 29.9:
                col1 , col2, = row[0].columns([1, 1])
                with col1: st.write("Você está com sobrepeso:")
                with col2: st.write("O sobrepeso pode calsar infermidades como diabetes e hipertensão, por isso cuidado!, Procure um Medico ou nutricionista para avaliação do Resultado")

            else:
                col1 , col2, = row[0].columns([1, 1])
                with col1: st.write("Voce está com obesidade:")
                with col2: st.write("A obesidade pode representar perigos como problemas cardiacos, diabetes tipo 2, hipertensão e problemas ortopedicos, por conta disso Procure um Medico!")

            tile = row[1].container(border=True)
            if sex == "Homem": TMB = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
            elif sex == "Mulher": TMB = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
            tile.write(f"<p style='text-align: center;'>Taxa Metabólica Basal (TMB)</br>{TMB:.2f} Kcal</p>", unsafe_allow_html=True)
            row[1].write("##### Gasto Calórico Diário Total (GCDT):")
            cols = row[1].columns([1, 5, 1]) 
            with cols[1]: st.write(f"Sedentário: {TMB * 1.2:.2f} kcal")
            with cols[1]: st.write(f"Leve (1-3 dias): {TMB * 1.375:.2f} kcal")
            with cols[1]: st.write(f"Moderado (3-5 dias): {TMB * 1.55:.2f} kcal")
            with cols[1]: st.write(f"Intenso (6-7 dias): {TMB * 1.725:.2f} kcal")
            with cols[1]: st.write(f"Muito intenso (2x/dia ou trabalho físico pesado): {TMB * 1.9:.2f} kcal")

            tile = row[2].container(border=True)
            watter_per_kg = (weight * 35) / 1000
            tile.write(f"<p style='text-align: center;'>Ingestão de Água por KG</br>{watter_per_kg} Litros</p>", unsafe_allow_html=True)
            row[2].write("##### Quantidade:")
            cols = row[2].columns([1, 5, 1]) 
            with cols[1]: st.write(f"{(watter_per_kg * 1000) / 500:.2f} Garrafas Pequenas (500ml)")
            with cols[1]: st.write(f"{(watter_per_kg * 1000) / 1000:.2f} Garrafas Medias (1L)")
            with cols[1]: st.write(f"{(watter_per_kg * 1000) / 1500:.2f} Garrafas Grandes (1,5L)")
            with cols[1]: st.write(f"{(watter_per_kg * 1000) / 2000:.2f} Garrafas Grandes (2L)")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Home | Relatorio Eshows",
        page_icon="./assets/imgs/Fit_logo.png",
        layout="wide"
    )

    component_hide_sidebar()
    component_fix_tab_echarts()

    if 'user_name' in st.session_state:
        render()