import streamlit as st

st.title("👋🏻 미술실놀러와")
st.subheader("저의 페이지에 오신 것을 환영합니다.")
st.write("미술교사 최유나입니다.")

st.link_button("키티쌤블로그 바로가기!", "https://blog.naver.com/kittyontop")

st.success("미술작품을 검색해보세요")
# st.error("빨간색 창")
# st.info("파란색 창")
# st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/nR4L10XlJcSeQ/giphy.gif?cid=790b76112wig0ccffy14fb764lc4qt9eohzzipq7tmzx2a41&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="Welcome to ")
st.video("https://youtu.be/hAAixJ8lux8?si=aZgKRkppa3yEzGtC") 