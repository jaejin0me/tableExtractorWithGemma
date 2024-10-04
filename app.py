import torch
from transformers import pipeline
import streamlit as st
import pdfplumber
from datetime import datetime
from jarowinkler import jarowinkler_similarity
import time
import re

torch.cuda.empty_cache()
st.title('Table extractor')
st.header("Upload pdf file")
table_name_format = st.text_input("Table name format e.g. Table [0-9.-]+:", value="Table [0-9.-]+:")
uploaded_file = st.file_uploader(label='Upload the PDF file', type=['pdf'])

if uploaded_file:
    button = st.button('Generate')

    if button:
        st.write("-----------------------------------")
        st.write("Extracting text...")
        now = datetime.now()
        st.write(f"Current time: {now}")

        extracted_text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            find_flag = False
            prev_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if find_flag:
                    score = jarowinkler_similarity(prev_text, text)
                    ##print(score)
                    if score > 0.5:
                        extracted_text += text
                        prev_text = text
                        ##print(text)
                    else:
                        prev_text = ""
                        find_flag = False
                elif re.search(r"Table [0-9.-]+:", text):
                    find_flag = True
                    result = re.search(r"Table [0-9.-]+:", text)
                    prev_text = text[result.start():]
                    extracted_text += prev_text
                    ##print(text_partial)
                st.write(f"read page {page.page_number}")

        st.write(extracted_text[0:1000])

        #last_prompt = f"""
        #The following text is extracted from a PDF document. Summarize the text:
        #extracted_text: {extracted_text[:1000]}
        #"""

        last_prompt = f"""
        The following text is extracted from a PDF document. Convert the extracted content into CSV format:
        extracted_text: {extracted_text[:1000]}
        """

        messages = [
            {"role": "user", "content": f"{last_prompt}"},
        ]

        now = datetime.now()
        st.write(f"Current time: {now}")
        st.write("Generating...")
        pipe = pipeline(
            "text-generation",
            model="google/gemma-2-2b-it",
            model_kwargs={"torch_dtype": torch.bfloat16},
            device="cpu"
        )
        outputs = pipe(messages, max_new_tokens=512)
        assistant_response = outputs[0]["generated_text"][-1]["content"].strip()

        st.write("-----------------------------------")
        st.header('Table data')
        st.write(assistant_response)
        now = datetime.now()
        st.write(f"Current time: {now}")