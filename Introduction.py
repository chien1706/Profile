import streamlit as st
import cv2
st.markdown("# About Me 🎈")
# st.sidebar.markdown("# Main page 🎈")
image_path = "D:\Certificate\image.jpg"
image = cv2.imread(image_path)
st.image(image, caption='TrinhChien')


st.markdown(
    """
    <style>
    .horizontal-bar {
        border-top: 1px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# from streamlit.components.v1 import HtmlComponent

# Nhúng biểu tượng Facebook bằng cách sử dụng thẻ <i> trong HTML
# facebook_icon = HtmlComponent("""
# <i class="fab fa-facebook-square fa-2x"></i>
# """)
# Sử dụng class 'horizontal-bar' để tạo đường kẻ ngang
# st.markdown('<div class="horizontal-bar"></div>', unsafe_allow_html=True)
st.write('# Education')
st.markdown('## 1.University:')
st.markdown('### Name: Ha Noi University of Science and Technology (HUST)')
st.markdown('### Major: Computer Science - Talented Program - 3rd Student')
st.markdown('### CPA: 3.81')

st.markdown('## 2.Primary School:')
st.markdown('### Name: Tứ Kỳ Primary School')
st.markdown('### Major: Math')
st.markdown('### CPA: 8.8')

st.markdown('## 3.Secondary School')
st.markdown('### Name: Phan Bội Châu Secondary School')
st.markdown('### Major: Math')
st.markdown('### CPA: 8.9')
# st.markdown('### 1.University')

st.write('# Experience')
st.write('## 1.AI Engineer ')
st.write('### AI Engineer at Nautilus Company from 8 Octobal 2022')
st.write('### Contribute: Research and Develop product about Human activities Recognition ')
st.write('## 2.AI Researcher at AIoT Lab')
st.write('### AIoT is a laboratory in BK.AI in HaNoi University of Science and Technology')
st.write('### Research and Develop about OCR, Key Information Extraction')
st.write('# Contact')
# st.write("\uF09A")
st.markdown('### Phone number: 0373317176')
st.markdown('### Facebook: https://www.facebook.com/chien.trinhvan.1706 ')
st.markdown('### github: https://github.com/chien1706')
# st.markdown('## Facebook: https://www.facebook.com/chien.trinhvan.1706 ')
