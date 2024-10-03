import torch
from transformers import pipeline
import streamlit as st
import pdfplumber

st.title('Table extractor for 3GPP TS documents')
st.header("Upload the document to extract the table data")
uploaded_file = st.file_uploader(label='Upload the PDF file', type=['pdf'])

if uploaded_file:
    # Extract text from the uploaded PDF file
    with pdfplumber.open(uploaded_file) as pdf:
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text()

    last_prompt = f"""
    Extract the table captions from the following text extracted from the PDF file:
    {extracted_text[:1000]}  # Limiting to the first 1000 characters for prompt efficiency
    """

    messages = [
        {"role": "user", "content": f"{last_prompt}"},
    ]

    button = st.button('Generate')

    if button:
        pipe = pipeline(
            "text-generation",
            model="google/gemma-2-2b-it",
            model_kwargs={"torch_dtype": torch.bfloat16},
            device="cpu",  # replace with "mps" to run on a Mac device
        )
        outputs = pipe(messages, max_new_tokens=512)
        assistant_response = outputs[0]["generated_text"][-1]["content"].strip()

        st.write("---")
        st.header('Caption list')
        st.write(assistant_response)