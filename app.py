import streamlit as st
from PyPDF2 import PdfReader
from anthropic import Anthropic
import os
from dotenv import load_dotenv

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF:{str(e)}")
        return None

def generate_summary(text):
    """Generate summary using Claude"""
    try:
          
        load_dotenv()

        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

        prompt = f"""Please provide a comprehensive summary of the following research paper.
        Include:
        - Main research objectives
        - Methodology
        - Key findings
        - Important conclusions

        Research paper text:
        {text}"""

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content":prompt}]
        )

        # Extract the content from the message response
        if hasattr(message,'content') and isinstance(message.content, list):
            # if content is a list, join all the text blocks 
            summary_text = '\n'.join(
                block.text for block in message.content
                if hasattr(block,'text')
            )
        else:
            # if content is already a string
            summary_text = str(message.content)
          
        return summary_text
    except Exception as e:
        st.error(f"Error generating summary:{str(e)}")
        return None

def main():
    st.title("Research Paper PDF Summarizer")
    st.write("Upload a research paper to get a comprehensive summary")

    #File uploader
    pdf_file = st.file_uploader("Upload your research paper (PDF)", type=['pdf'])

    if pdf_file is not None:
        with st.spinner("Processing PDF..."):
            #Extract text from PDF 
            text = extract_text_from_pdf(pdf_file)

        if text:
            st.success("PDF processed successfully!")

            if st.button("Generate Summary"):
                with st.spinner("Generating summary using Claude.."):
                    summary = generate_summary(text)

                    if summary:
                        st.subheader("Summary")
                        st.write(summary)

                        #Add download button for summary 
                        st.download_button(
                            label="Download Summary",
                            data = summary,
                            file_name = "research_summary.txt",
                            mime="text/plain"
                        )

if __name__ == "__main__":
    main()
