import streamlit as st
from pdf2docx import Converter

def convert_pdf_to_docx():
    st.set_page_config(page_title="PDF to Docx Converter", page_icon=":guardsman:", layout="wide")
    st.title("PDF to Docx Converter")

    pdf_file = st.file_uploader("Upload a pdf file", type=["pdf"])
    if pdf_file is None:
        st.warning("Please upload a pdf file")
        return
    else:
        cv = Converter(pdf_file)
        cv.convert()
        cv.close()
        st.success("File Converted Successfully")
        st.markdown("Press `Download File` button to download docx file")
        if st.button("Download File"):
            st.download(docx_file)

if __name__ == '__main__':
    convert_pdf_to_docx()
