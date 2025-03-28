# 📄 Research Paper Summarizer

This project is a **PDF summarizer for Research papers** built using **Streamlit** and the **Anthropic Claude 3.5 Sonnet API**. Simply upload a PDF file, and the app will generate a structured summary that includes the main objectives, methodology, key findings, and conclusions.

---

## 🚀 Features

- 📥 Upload any research paper in PDF format
- 📄 Extracts and reads full text from the PDF
- 🤖 Uses **Claude 3.5 Sonnet** to generate a clear, structured summary
- 📋 Outputs:
  - Research Objectives
  - Methodology
  - Key Findings
  - Conclusions
- 💾 Download the generated summary as a text file
- 🖥️ Clean and interactive Streamlit interface

---

## 🧑‍💻 Tech Stack

- Streamlit
- Anthropic Python SDK
- Claude 3.5 Sonnet model
- PyPDF2
- python-dotenv

---

## 📁 Project Structure

research-paper-summarizer/
│
├── app.py                # Main Streamlit application
├── .env                  # Contains your API key (DO NOT share or commit this)
├── .env.example          # Example structure for .env file
├── requirements.txt      # Python dependencies
├── README.md             # You're here :)
└── venv/                 # Virtual environment (ignored)

---

## ⚙️ Setup Instructions

1. Clone the repository:
   git clone https://github.com/your-username/research-paper-summarizer.git
   cd research-paper-summarizer

2. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   venv\Scripts\activate           # On Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Set up your `.env` file:
   Create a `.env` file in the root directory and add your Anthropic API key:
   ANTHROPIC_API_KEY=your_actual_anthropic_key_here

5. Run the app:
   streamlit run app.py

---

## 📦 Requirements

If you don’t want to use `requirements.txt`, manually install:
pip install streamlit PyPDF2 anthropic python-dotenv

---

## 🔒 Security

Keep your `.env` file private.
Do NOT commit `.env` or API keys to GitHub.

Add this to your `.gitignore`:
.env
venv/
__pycache__/

---

## 💡 Future Enhancements

- Chunk large PDFs and support multi-section summarization
- Add cost/token tracker per summary
- Optional models: OpenAI GPT-4, Mistral, LLaMA
- UI improvements: highlight key terms, download as PDF
- Add citation and metadata extraction





**Sushma Niresh**  
GitHub: https://github.com/Sushmaniresh 
LinkedIn: https://linkedin.com/in/sushma-n
