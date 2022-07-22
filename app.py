import streamlit as st
import sqlite3
import pandas as pd
import os.path

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT * "
                f"FROM users "
                f"WHERE id='{id}' and pwd = '{pw}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록','게임'])

if menu == '로그인':
    st.subheader('로그인')
    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.text_input('비밀번호',
                             placeholder='비밀번호를 입력하세요',
                             type='password')
    login_btn = st.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        file_name = './img/'+user_info[0]+'.png'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.write(user_info[4], '님 환영합니다.')
        else:
            st.write(user_info[4], '님 환영합니다.')
    st.sidebar.subheader('로그인')

if menu == '회원가입':
    st.subheader('회원가입')
    st.info('다음 양식을 모두 입력후 회원가입 버튼을 클릭하세요')
    uid = st.text_input('아이디', max_chars=10)
    uname = st.text_input('이름', max_chars=10)
    upw = st.text_input('비밀번호', type='password')
    upw_chk = st.text_input('비밀번호 확인', type='password')
    uage = st.text_input('나이')
    ugender = st.radio('성별', options=['여','남','트랜스 젠더'], horizontal=True)

    ubtn = st.button('회원가입')
    if ubtn:
        if upw != upw_chk:
            st.warning('비밀번호가 일치하지 않습니다.')
            st.stop()

        cur.execute(f"INSERT INTO users(id, pwd, gender, age, name) "
                    f"VALUES('{uid}','{upw}', '{ugender}', {uage}, '{uname}')")
        st.success('회원가입에 성공했습니다.')
        con.commit()
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT name,age,gender FROM users', con)
    st.dataframe(df)
    st.sidebar.write('회원목록')
    st.video('https://youtu.be/ESWiIyhibpY')

if menu == '게임':

    a = st.text_input('숫자1')
    b = st.text_input('숫자2')

    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        login_btn1 = st.button('더하기')
    with col2:
        login_btn2 = st.button('빼기')
    with col3:
        login_btn3 = st.button('곱하기')
    with col4:
        login_btn4 = st.button('나누기')



    if login_btn1:
        st.write(str(int(a)+int(b)))
    if login_btn2:
        st.write(str(int(a)-int(b)))
    if login_btn3:
        st.write(str(int(a)*int(b)))
    if login_btn4:
        st.write(str(int(a)/int(b)))


