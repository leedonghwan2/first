import streamlit as st

menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.subheader('로그인')
    st.sidebar.write('로그인')
if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.write('회원목록')
