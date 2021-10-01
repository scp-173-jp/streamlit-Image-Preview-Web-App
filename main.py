import streamlit as st
from PIL import Image

st.title('画像プレビューWebアプリ')

# extension = st.radio('拡張子', ('psd', 'svg', 'bmp', 'tiff', 'png', 'jpg', 'gif'))
extension = st.multiselect('ファイル拡張子固定', ['psd', 'svg', 'bmp', 'tiff', 'png', 'jpg', 'gif'])

upload_file = st.file_uploader('画像ファイルをドラッグ、または選択してください。:))',type=extension)
if upload_file is not None:
    img = Image.open(upload_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
