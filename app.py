import streamlit as st
from main import run_pharma_assistant
import os
from dotenv import load_dotenv

load_dotenv()

st.title("🔎 Pharma AI Assistant")
st.write(
    "Essa IA te ajuda com **dúvidas sobre remédios** baseado em suas bulas"
)

# Sidebar for user selection
with st.sidebar:
    task_type = (
        "Answer Pharma Question"  # Since we have only one task, it's pre-selected
    )

    # Input field for user question
    user_input = st.text_area("Escreva sua pergunta:")

# Run the AI Pharma Assistant when the user clicks the button
if st.button("Processar pergunta 🚀"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, envie uma pergunta.")
    else:
        st.write("⏳ Processando sua pergunta... Por favor, espere.")

        pdf_dir = "knowledge"  # sua pasta local com os PDFs
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

        files_mds = []

        for file_name in pdf_files:
            file_path = f"{pdf_dir}/{file_name}"
            file_url = f"/{file_path}"  # assume que a pasta 'docs' está na raiz do projeto Streamlit
            files_mds.append(f'📄 [{file_name}](/{file_path})')

        st.markdown(" | ".join(files_mds), unsafe_allow_html=True)
    
        # ✅ Call the function from main.py
        result = run_pharma_assistant(user_input)

        # Display the AI response
        st.subheader("✅  Resposta da IA:")
        st.write(result.raw)