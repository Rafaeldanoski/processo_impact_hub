############## IMPORTS #######################
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import altair as alt
import warnings
warnings.filterwarnings("ignore")

############## DASH ##########################
st.set_page_config(page_title="Dashboard Impact HUB",layout="wide",page_icon="favicon.ico")

st.sidebar.success("Selecione uma página acima")

st.write("""
# Dashboard Impact HUB
""")

############## DATASET #######################
@st.experimental_memo
def load_data(url): 
    return pd.read_csv(url, header=1)

df = load_data('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyqdSYRLIooQ9T3AuUYPnVuBt1U1PtteQshFfcJT0GBnOb5W9tJh8P_8oFJdtz7_bE7eDnXPCIs7cv/pub?output=csv')

############ Seletores ######################
col1, col2, col3, col4 = st.columns(4)

with col1:
   metodo = st.multiselect("MÉTODO",(list(df['Método'].unique())), key='metodo')
if st.session_state['metodo']==[]:
    metodo = df['Método'].unique()

with col2:
   turma = st.multiselect("TURMA",(list(df['Qual a sua turma?'].unique())), key='turma')
if st.session_state['turma']==[]:
    turma = df['Qual a sua turma?'].unique()

with col3:
   fase = st.multiselect("FASE",(list(df['Em que fase está a sua empresa após o programa?'].unique())), key='fase')
if st.session_state['fase']==[]:
    fase = df['Em que fase está a sua empresa após o programa?'].unique()

with col4:
   escolaridade = st.multiselect("ESCOLARIDADE",(list(df['Grau de escolaridade'].unique())), key='escolaridade')
if st.session_state['escolaridade']==[]:
    escolaridade = df['Grau de escolaridade'].unique()

col5, col6, col7, col8 = st.columns(4)

with col5:
   etnia = st.multiselect("ETNIA",(list(df['Como você se auto declara'].unique())), key='etnia')
if st.session_state['etnia']==[]:
    etnia = df['Como você se auto declara'].unique()

with col6:
   genero = st.multiselect("GÊNERO",(list(df['Qual seu gênero'].unique())), key='genero')
if st.session_state['genero']==[]:
    genero = df['Qual seu gênero'].unique()

with col7:
   ramo = st.multiselect("RAMO",(list(df['Qual o ramo do seu negócio?'].unique())), key='ramo')
if st.session_state['ramo']==[]:
    ramo = df['Qual o ramo do seu negócio?'].unique()
   

df_filter = df[(df['Método'].isin(metodo)) 
                & (df['Qual a sua turma?'].isin(turma)) 
                & df['Em que fase está a sua empresa após o programa?'].isin(fase)
                & (df['Grau de escolaridade'].isin(escolaridade)) 
                & df['Como você se auto declara'].isin(etnia)
                & (df['Qual seu gênero'].isin(genero)) 
                & df['Qual o ramo do seu negócio?'].isin(ramo)
                ]
            

agg_full = df_filter.groupby(['Nome Completo']).agg({'Faturamento antes do programa':'first','Faturamento após o programa':'first','Você gerou quantos empregos durante/após a participação no Inovativa?':'first',
                                                     'Você fez conexões relevantes graças ao programa Inovativa?':'first', 'Para você acelerar o seu negócio, o quanto participar do Inovativa foi importante?':'first',
                                                     'Para você crescer a sua renda, o quanto participar do Inovativa foi importante?':'first', 'Para você aumentar a sua motivação e comprometimento, o quanto participar do Inovativa foi importante?':'first',
                                                     'Para você encontrar novas ideias e soluções para o seu negócio, o quanto participar do Inovativa foi importante?':'first','Para você ter acesso a novos clientes, o quanto participar do Inovativa foi importante?':'first',
                                                     'Para você fazer conexões relevantes, o quanto participar do Inovativa foi importante?':'first','Para você melhorar a sua competitividade no seu mercado de atuação, o quanto participar do Inovativa foi importante?':'first',
                                                     'Para você ganhar visibilidade, reconhecimento e credibilidade, o quanto participar do Inovativa foi importante?':'first', 'Em geral, qual o seu nível de satisfação com a metodologia adotada pelo programa?':'first'})

agg_full['Retorno'] = agg_full['Faturamento após o programa'] -  agg_full['Faturamento antes do programa']
agg_full['% Retorno'] = round(((agg_full['Retorno'] / agg_full['Faturamento antes do programa']) - 1) * 100, 2)

agg_full = agg_full[['Faturamento antes do programa','Faturamento após o programa','Retorno','% Retorno','Você gerou quantos empregos durante/após a participação no Inovativa?','Você fez conexões relevantes graças ao programa Inovativa?',
                     'Para você acelerar o seu negócio, o quanto participar do Inovativa foi importante?','Para você crescer a sua renda, o quanto participar do Inovativa foi importante?','Para você aumentar a sua motivação e comprometimento, o quanto participar do Inovativa foi importante?',
                     'Para você encontrar novas ideias e soluções para o seu negócio, o quanto participar do Inovativa foi importante?','Para você ter acesso a novos clientes, o quanto participar do Inovativa foi importante?','Para você fazer conexões relevantes, o quanto participar do Inovativa foi importante?',
                     'Para você melhorar a sua competitividade no seu mercado de atuação, o quanto participar do Inovativa foi importante?','Para você ganhar visibilidade, reconhecimento e credibilidade, o quanto participar do Inovativa foi importante?','Em geral, qual o seu nível de satisfação com a metodologia adotada pelo programa?']]


agg_full.sort_values(by='Retorno', ascending=False)
st.dataframe(agg_full, use_container_width=True)