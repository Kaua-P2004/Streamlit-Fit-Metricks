import streamlit as st
import math

def function_circumferences():
    col_1 = st.columns(3)  

    with col_1[0]:
        neck = st.number_input("Circunferência do Pescoço (CM):", min_value=1, key="neck")

    with col_1[1]:
        chest = st.number_input("Circunferência do Peito (CM):", min_value=1, key="chest")

    with col_1[2]:
        waist = st.number_input("Circunferência da Cintura (CM):", min_value=1, key="waist")

    col_2 = st.columns(3) 

    with col_2[0]:
        hip = st.number_input("Circunferência do Quadril (CM):", min_value=1, key="hip")

    with col_2[1]:
        thigh = st.number_input("Circunferência da Coxa (CM):", min_value=1, key="thigh")

    with col_2[2]:
        calf = st.number_input("ircunferência da Panturrilha (CM):", min_value=1, key="calf")
    
    col_3 = st.columns(4)

    with col_3[1]:
        biceps = st.number_input("Circunferência do Biceps (CM):", min_value=1, key="aa")

    with col_3[2]:
        forearm = st.number_input("Circunferência do Antebraço (CM):", min_value=1, key="thaigh")

    return neck, chest, waist, hip, thigh, calf, biceps, forearm

def function_measures():
    col = st.columns(3)

    with col[0]:
        height = st.number_input("Digite sua Altura (CM):",min_value=1)
    with col[1]:
        weight = st.number_input("Digite seu Peso (KG):",min_value=1.00)
    with col[2]:
        age = st.number_input("Digite sua idade:", min_value=0, format="%d")
    
    return height, weight, age

def function_IMC_calc(height, weight, tile, row):
    heightIMC = height / 100
    IMC = weight / (heightIMC ** 2)
    tile.write(f"<p style='text-align: center;'>IMC (Índice de Massa Corporal)</br>{IMC:.2f}</p>", unsafe_allow_html=True)
    row[0].write("##### Explicação:")

    if IMC < 18.5:
        col1, col2 = row[0].columns([1, 1])
        with col1: 
            st.write("Você está abaixo do peso:")
        with col2: 
            st.write("A recomendação é procurar um médico para avaliação do resultado.")
    
    elif 18.5 <= IMC < 24.9:
        col1, col2 = row[0].columns([1, 1])
        with col1: 
            st.write("Você está no peso ideal:")
        with col2: 
            st.write("Tudo certo, mas é importante avaliar outros fatores como circunferência abdominal.")
    
    elif 25 <= IMC < 29.9:
        col1, col2 = row[0].columns([1, 1])
        with col1: 
            st.write("Você está com sobrepeso:")
        with col2: 
            st.write("O sobrepeso pode causar doenças como diabetes e hipertensão. Procure um médico ou nutricionista.")
    else:
        col1, col2 = row[0].columns([1, 1])
        with col1: 
            st.write("Você está com obesidade:")
        with col2: 
            st.write("A obesidade pode representar riscos graves. Procure um médico imediatamente.")

    return IMC

def function_TMB_calc(sex, weight, height, age, tile, row):
    if sex == "Homem": 
        TMB = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif sex == "Mulher": 
        TMB = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    
    tile.write(f"<p style='text-align: center;'>TMB (Taxa Metabólica Basal)</br>{TMB:.2f} Kcal</p>", unsafe_allow_html=True)
    
    row[1].write("##### Gasto Calórico Diário Total (GCDT):")
    
    cols = row[1].columns([1, 5, 1]) 
    with cols[1]: 
        st.write(f"Sedentário: {TMB * 1.2:.2f} kcal")
        st.write(f"Leve (1-3 dias): {TMB * 1.375:.2f} kcal")
        st.write(f"Moderado (3-5 dias): {TMB * 1.55:.2f} kcal")
        st.write(f"Intenso (6-7 dias): {TMB * 1.725:.2f} kcal")
        st.write(f"Muito intenso (2x/dia ou trabalho físico pesado): {TMB * 1.9:.2f} kcal")

def function_water_calc(weight,tile,row):
    watter_per_kg = (weight * 35) / 1000
    tile.write(f"<p style='text-align: center;'>Ingestão de Água por KG</br>{watter_per_kg} Litros</p>", unsafe_allow_html=True)
    row[2].write("##### Quantidade:")
    cols = row[2].columns([1, 5, 1]) 
    with cols[1]: st.write(f"{(watter_per_kg * 1000) / 500:.2f} Garrafas Pequenas (500ml)")
    with cols[1]: st.write(f"{(watter_per_kg * 1000) / 1000:.2f} Garrafas Medias (1L)")
    with cols[1]: st.write(f"{(watter_per_kg * 1000) / 1500:.2f} Garrafas Grandes (1,5L)")
    with cols[1]: st.write(f"{(watter_per_kg * 1000) / 2000:.2f} Garrafas Grandes (2L)")

def function_PFC_calc(sex, age, waist, hip, neck, height, IMC, tile, row):
    if sex == "Homem": 
        try:
            PFC = 495/(1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
            tile.write(f"<p style='text-align: center;'> PFC (Percentual de Gordura Corporal)</br>{PFC:.2f}%</p>", unsafe_allow_html=True)
            row[1].write("##### Explicação:")
            cols = row[1].columns([0.5, 10, 0.5])
            with cols[1]: st.write("Calculo baseado na formula de Jackson & Pollock")
            if 18 <= age < 25:
                function_PFC_structure(PFC, row, 4, 4, 6, 8, 10, 12, 13, 14, 16, 17, 20, 20, 24, 26, 36)
            if 26 <= age < 35:
                function_PFC_structure(PFC, row, 8, 8, 11, 12, 15, 16, 18, 18, 20, 22, 24, 24, 27, 28, 36)
            if 36 <= age < 45:
                function_PFC_structure(PFC, row, 10, 10, 14, 16, 18, 19, 21, 21, 23, 24, 25, 27, 29, 30, 39)
            if 45 <= age < 55:
                function_PFC_structure(PFC, row, 12, 12, 16, 18, 20, 21, 23, 24, 25, 26, 27, 28, 30, 32, 38)
            if 56 <= age < 65:
                function_PFC_structure(PFC, row, 13, 13, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 32, 38)

        except: 
            tile.write(f"<p style='text-align: center;'> PFC (Percentual de Gordura Corporal)</br>Dados Invalidos</p>", unsafe_allow_html=True)
    
    elif sex == "Mulher": 
        try:
            PFC = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450
            tile.write(f"<p style='text-align: center;'> PFC (Percentual de Gordura Corporal)</br>{PFC:.2f}%</p>", unsafe_allow_html=True)
            row[1].write("##### Explicação:")
            cols = row[1].columns([0.5, 10, 0.5])
            with cols[1]: st.write("Calculo baseado na formula de Jackson & Pollock")
            if 18 <= age < 25:
                function_PFC_structure(PFC, row, 4, 4, 6, 8, 10, 12, 13, 14, 16, 17, 20, 20, 24, 26, 36)
        except:
            tile.write(f"<p style='text-align: center;'> PFC (Percentual de Gordura Corporal)</br>Dados Invalidos</p>", unsafe_allow_html=True)

def function_PMM_calc(IMC, tile, row):
    tile.write(f"<p style='text-align: center;'>PMM (Percentual de Massa Magra)</br>{IMC:.2f}</p>", unsafe_allow_html=True)

def function_if_structure(row, texto1, texto2):
    col1, col2 = row[1].columns([1, 1])
    with col1: 
        st.write(f"{texto1}")
    with col2: 
        st.write(f"{texto2}")
        

def function_PFC_structure(PFC, row, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15):
    if PFC < v1:
        function_if_structure(row, "Muito Baixo", "...")
    elif v2 <= PFC < v3:
        function_if_structure(row, "Exelente:", "...")

    elif v4 <= PFC < v5:
        function_if_structure(row, "Bom:", "...")
    
    elif v6 <= PFC < v7:
        function_if_structure(row, "Acima da Media", "...")
    
    elif v8 <= PFC < v9:
        function_if_structure(row, "Média", "...")
    
    elif v10 <= PFC < v11:
        function_if_structure(row, "Abaixo da Média", "...")
    
    elif v12 <= PFC < v13:
        function_if_structure(row, "Ruim", "...")
    
    elif v14 <= PFC < v15:
        function_if_structure(row, "Muito Ruim", "...")