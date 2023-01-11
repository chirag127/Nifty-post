import streamlit as st
from pdf2docx import Converter
from docx2pdf import convert

def convert_pdf_to_docx():
    st.set_page_config(page_title="PDF to Docx Converter", page_icon=":guardsman:", layout="wide")
    st.title("PDF to Docx Converter")

    pdf_file = st.file_uploader("Upload a pdf file", type=["pdf"])
    if pdf_file is None:
        st.warning("Please upload a pdf file")
        return
    else:
        cv = Converter(pdf_file)
        docx_file = cv.convert()
        cv.close()
        st.success("File Converted Successfully")
        st.markdown("Press `Download File` button to download docx file")
        if st.button("Download File"):
            st.download(docx_file)

def convert_docx_to_pdf():
    st.set_page_config(page_title="Docx to PDF Converter", page_icon=":guardsman:", layout="wide")
    st.title("Docx to PDF Converter")

    docx_file = st.file_uploader("Upload a docx file", type=["docx"])
    if docx_file is None:
        st.warning("Please upload a docx file")
        return
    else:
        pdf_file = convert(docx_file)
        st.success("File Converted Successfully")
        st.markdown("Press `Download File` button to download pdf file")
        if st.button("Download File"):
            st.download(pdf_file)

def main():
    st.set_page_config(page_title="File Converter", page_icon=":guardsman:", layout="wide")
    st.title("File Converter")
    st.markdown("Select an option below to convert your file")
    option = st.selectbox("Select the file type you want to convert", ["PDF to Docx", "Docx to PDF"])
    if option == "PDF to Docx":
        convert_pdf_to_docx()
    elif option == "Docx to PDF":
        convert_docx_to_pdf()

if __name__ == '__main__':
    main()
