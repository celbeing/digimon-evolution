import streamlit as st
st.title("streamlit 연습🤷‍♂️")
name = st.text_input("이름을 입력해주세요.")
menu = st.selectbox("좋아하는 음식을 선택해주세요.", ["떡볶이", "치킨", "피자", "라면"])
if st.button("인삿말 생성하기"):
  st.write(name + "님, 당신이 좋아하는 음식은", menu + "이군요!")
