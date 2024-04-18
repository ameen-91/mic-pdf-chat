import streamlit as st
from PyPDF2 import PdfReader

def read_pdf(docs):
    text = ""
    for pdf in docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



def main():
    st.set_page_config(page_title="MIC PDF Chat", page_icon=":books:")
    st.header("PDF Chat")








if __name__ == '__main__':
    main()