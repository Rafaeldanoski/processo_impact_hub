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

st.markdown("<h1 style='text-align: center;'>GRÁFICOS</h1>", unsafe_allow_html=True)

############## DATASET #######################
@st.experimental_memo
def load_data(url):
    return pd.read_csv(url, header=1)

df = load_data('https://docs.google.com/spreadsheets/d/e/2PACX-1vQyqdSYRLIooQ9T3AuUYPnVuBt1U1PtteQshFfcJT0GBnOb5W9tJh8P_8oFJdtz7_bE7eDnXPCIs7cv/pub?output=csv')

###################### KPI por anúncio #######################

tab_graphs, tab_research, tab_coesao = st.tabs(["VARIÁVEIS", "PESQUISA", "COESÃO"])

with tab_graphs:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("""
        TURMA
        """)

        turma = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Qual a sua turma?',
            y=alt.Y(field='Qual a sua turma?', aggregate='count')
        )

        text = turma.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(turma.interactive() + text, use_container_width=True)

    with col2:
        st.write("""
        FASE
        """)

        fase = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Em que fase está a sua empresa após o programa?',
            y=alt.Y(field='Em que fase está a sua empresa após o programa?', aggregate='count')
        )

        text = fase.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(fase.interactive() + text, use_container_width=True)

    with col3:
        st.write("""
        FEZ NOVAS CONEXÕES
        """)

        conexoes = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Você fez conexões relevantes graças ao programa Inovativa?',
            y=alt.Y(field='Você fez conexões relevantes graças ao programa Inovativa?', aggregate='count')
        )

        text = conexoes.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(conexoes.interactive() + text, use_container_width=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.write("""
        ESCOLARIDADE
        """)

        escolaridade = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Grau de escolaridade',
            y=alt.Y(field='Grau de escolaridade', aggregate='count')
        )

        text = escolaridade.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(escolaridade.interactive() + text, use_container_width=True)

    with col5:
        st.write("""
        ETNIA
        """)

        etnia = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Como você se auto declara',
            y=alt.Y(field='Como você se auto declara', aggregate='count')
        )

        text = etnia.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(etnia.interactive() + text, use_container_width=True)

    with col6:
        st.write("""
        RAMO
        """)

        ramo = alt.Chart(df).mark_bar(point=alt.OverlayMarkDef(color="blue")).encode(
            x='Qual o ramo do seu negócio?',
            y=alt.Y(field='Qual o ramo do seu negócio?', aggregate='count')
        )

        text = ramo.mark_text(
        align='center',
        baseline='middle',
        dx=3,
        color='white'
        ).encode(
        text=alt.Y(field='TURMA', aggregate='count')
        )

        st.altair_chart(ramo.interactive() + text, use_container_width=True)

with tab_research:

    data = [['Muito Importante', 260], ['Importante', 131], ['Razoavelmente Importante', 39], ['Pouco Importante', 15], ['Sem Importância', 4]]

    df_research = pd.DataFrame(data, columns=['resultado', 'quantidade'])
    
    research = alt.Chart(df_research).mark_arc(innerRadius=50).encode(
    theta="quantidade",
    color="resultado:N",
    )   

    text = research.mark_text(radius=140, size=20).encode(text="resultado:N")

    st.altair_chart(research.interactive(), use_container_width=True)

with tab_coesao:

    col1, col2, col3 = st.columns(3)

    with col1:
        df['Retorno'] = df['Faturamento após o programa'] -  df['Faturamento antes do programa']

        box_scholar = alt.Chart(df).mark_boxplot(extent='min-max').encode(
            x='Grau de escolaridade:O',
            y='Retorno:Q'
        ).properties(
        width=500,
        height=400)

        st.altair_chart(box_scholar.interactive())

    with col2:
        box_et = alt.Chart(df).mark_boxplot(extent='min-max').encode(
            x='Como você se auto declara:O',
            y='Retorno:Q'
        ).properties(
        width=400,
        height=400)

        st.altair_chart(box_et.interactive())

    with col3:
        box_job = alt.Chart(df).mark_boxplot(extent='min-max').encode(
            x='Qual o ramo do seu negócio?:O',
            y='Retorno:Q'
        ).properties(
        width=400,
        height=400)

        st.altair_chart(box_job.interactive())