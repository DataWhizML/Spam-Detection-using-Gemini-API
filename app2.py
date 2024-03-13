import google.generativeai as genai
import streamlit as st
import PIL.Image
from io import BytesIO

model = genai.GenerativeModel('gemini-pro-vision')
genai.configure(api_key="API-KEY")

def image_to_text(image):
    img = PIL.Image.open(BytesIO(image))
    response = model.generate_content(img)
    return response.text.strip()

def main():
    st.title("Gemini-Pro-Vision")
    image = st.file_uploader("Upload an Image", type=['jpg','jpeg','png'])
    if image is not None:
        st.image(image)
    if st.button("Get Response"):
        result = image_to_text(image.read())
        st.success(result)

if __name__ == '__main__':
    main()

