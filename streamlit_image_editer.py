import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style= 'text-align: center;'> Image Editor </h1>", unsafe_allow_html=True)
st.write("---------------")
image_1 = st.file_uploader("Upload your File", type=["png", "jpg", "jpng"])

if image_1:
    #------------------------------------
    but = st.checkbox("See Origanl-Image")
    st.write("\n\n")
    info = st.empty()
    size = st.empty()
    format = st.empty()
    model = st.empty()
    if but:
        st.image(image_1)
    #----------------------------------
    img = Image.open(image_1)
    info.markdown("<h2 style= 'text-align: center;'> Information </h2>", unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>",unsafe_allow_html=True)
    format.markdown(f"<h6>Format: {img.format}</h6>",unsafe_allow_html=True)
    model.markdown(f"<h6>Model: {img.mode}</h6>",unsafe_allow_html=True)
    #-----------------------------------------------
    st.markdown("<h2 style= 'text-align: center;'> Resizing </h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    #----------------------------------------------
    st.markdown("<h2 style= 'text-align: center;'> Rotation </h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")
    #-------------------------------------------------------
    st.markdown("<h2 style= 'text-align: center;'> Filter </h2>", unsafe_allow_html=True)
    selectnox = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss","Smooth"))
    #------------------------------------------------------
    st.write("\n\n\n\n")
    st.write("\n\n")
    st.write("\n\n")
    st.write("\n\n")
    s_but = st.button("Submit")
    if s_but:
        edte = img.resize((width, height)).rotate(degree)
        if filter == "None":
            st.image(edte)
        elif filter == "Blur":
            a = edte.filter(BLUR)
            st.image(a)
        elif filter=="Detail":
            a = edte.filter(DETAIL)
            st.image(a)
        elif filter=="Emboss":
            a= edte.filter(EMBOSS)
            st.image(a)
        else:
            a= edte.filter(SMOOTH)
            st.image(a)
    
        















