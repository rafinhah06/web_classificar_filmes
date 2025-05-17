import streamlit as st
import dados

st.title("Filmes")

nome = st.text_input("Nome do filme:")
ano = st.number_input("Ano do filme:", min_value=1990, max_value=2025)
nota = st.number_input("Nota do filme:", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    dados.insere_dados(nome, ano, nota)
    st.sucess("Filme Cadastrado")

    filmes = dados.obter_dados()
    st.header("Lista de Filmes")
    st.table(filmes)