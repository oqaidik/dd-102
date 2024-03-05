import streamlit as st
with st.sidebar:
    st.sidebar.title('Title')
    st.sidebar.subheader('Subheader')
    x = st.radio('Pick your gender',['Media','Form'])
if x=="Media":
    st.write("Hello ,let's learn how to build a streamlit app together")
    st.image("ofppt_logo.png")
    st.video("ma_video.mp4")
if x=="Form":
    st.checkbox('yes')
    st.button('Click')
    st.radio('Pick your gender',['Male','Female'])
    st.selectbox('Pick your gender',['Male','Female'])
    st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
    st.slider('Pick a number', 0,50)
