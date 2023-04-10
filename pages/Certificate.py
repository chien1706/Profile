import streamlit as st
from PIL import Image
image = Image.open("D:\Code\\upwork\\multiple\\certi\\Algorithm_Toolbox.jpg")
image2 = Image.open("D:\Code\\upwork\\multiple\\certi\\SQL_DataScience.jpg")
image3 = Image.open("D:\Code\\upwork\\multiple\\certi\\Deep_learning(ImprovingDNN).jpg")
image4 = Image.open("D:\Code\\upwork\\multiple\\certi\\bootcamp_techainer.jpg")

# Show the image in Streamlit
st.markdown('# 1.Algorithm Toolbox Certificate')
st.image(image, caption="Algorithm Toolbox", use_column_width=True)

st.markdown('# 2.SQL for Data Science')
st.image(image2, caption="SQL for Data Science", use_column_width=True)

st.markdown('# 3.Deep learning')
st.image(image3, caption="Algorithm Toolbox", use_column_width=True)

st.markdown('# 4.Techainer Bootcamp')
st.image(image4, caption="Algorithm Toolbox", use_column_width=True)
