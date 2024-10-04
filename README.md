# PDF Table Extractor

This project is a **PDF Table Extractor** application built using **Streamlit**, **Transformers**, and **PDFPlumber**. The app extracts tables from uploaded PDF documents, processes the extracted text, and attempts to convert it into CSV format.

## Features

- Upload a PDF file and extract text containing tables.
- Use regex to identify tables based on a format (e.g., `Table [0-9.-]+:`).
- The extracted text can be converted into a CSV format using a text generation model.
- The tool leverages the **Jaro-Winkler similarity** algorithm to ensure consistency between pages and extracted content.

## Demo

The application allows you to:
1. Upload a PDF file.
2. Define a table name format (regex) to detect tables (default: `Table [0-9.-]+:`).
3. Extract and view text from the PDF.
4. Convert the extracted content into CSV format.

## Tech Stack

The project uses the following major dependencies:

- **Streamlit**: Provides an easy-to-use web interface for the app.
- **Transformers**: Used to process the text and generate a CSV format from the extracted content.
- **PDFPlumber**: To handle PDF reading and text extraction.
- **Jaro-Winkler Similarity**: To check for similarity between consecutive pages when extracting tables.

## Requirements

Here are the key packages used in this project. Make sure to install them before running the application:

```bash
addict==2.4.0
aiofiles==22.1.0
altair==5.4.1
argon2-cffi==23.1.0
beautifulsoup4==4.12.3
black==24.8.0
certifi==2024.8.30
charset-normalizer==3.3.2
click==8.1.7
cryptography==43.0.1
decorator==5.1.1
fsspec==2024.9.0
huggingface-hub==0.25.1
jinja2==3.1.4
joblib==1.4.2
jsonschema==4.23.0
markdown-it-py==3.0.0
matplotlib==3.7.5
nbconvert==7.16.4
nbformat==5.10.4
numpy==1.24.4
pdfminer.six==20231228
pdfplumber==0.11.4
pillow==10.4.0
pandas==2.0.3
protobuf==5.28.2
pytorch-lightning==2.4.0
regex==2024.9.11
requests==2.32.3
scikit-learn==1.3.2
scipy==1.10.1
streamlit==1.39.0
torch==2.4.1
transformers==4.45.1
```

To install all dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository and navigate into the project directory.

   ```bash
   git clone https://github.com/yourusername/pdf-table-extractor.git
   cd pdf-table-extractor
   ```

2. Install the required packages using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application.

   ```bash
   streamlit run app.py
   ```

4. Open your web browser and go to `http://localhost:8501`.

5. Upload a PDF, specify the table name format, and click **Generate** to extract the table content.

## How It Works

### PDF Table Extraction

- **PDFPlumber** is used to open and read each page of the PDF document. Text is extracted, and a regular expression is used to identify table sections.
  
- **Jaro-Winkler Similarity** ensures the continuity of table text across multiple pages by comparing the extracted text between pages.

### Text-to-CSV Conversion

- The extracted text is passed to a **Transformers** pipeline using the Hugging Face library. The model generates CSV-like output based on the text provided. A simpler text generation model like `gpt-2` is used.

## Future Enhancements

- **Improved Table Extraction**: Incorporating advanced table detection algorithms to accurately extract tabular data.
- **Better CSV Generation**: Using more robust approaches for converting text to structured CSV data.
- **Model Optimization**: Experimenting with specialized models for better text-to-CSV conversion.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)
- [PDFPlumber](https://github.com/jsvine/pdfplumber)