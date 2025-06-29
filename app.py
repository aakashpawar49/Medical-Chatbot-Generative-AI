import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


# Load and prepare the FAISS index (load from local if exists)
@st.cache_resource
def load_faiss_index():
    if not os.path.exists("medical_index"):
        pdf_path = os.path.abspath("Data/Medical_book.pdf")
        if not os.path.isfile(pdf_path):
            st.error(f"PDF not found at: {pdf_path}")
            return None
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        text_chunks = text_splitter.split_documents(documents)
        embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        faiss_index = FAISS.from_documents(text_chunks, embedding=embedding_model)
        faiss_index.save_local("medical_index")
    else:
        faiss_index = FAISS.load_local(
            "medical_index",
            HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
            allow_dangerous_deserialization=True    
        )
    return faiss_index

# Load the text generation model and tokenizer
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return generator

def call_local_model(generator, prompt):
    result = generator(prompt, max_new_tokens=256, temperature=0.5)[0].get("generated_text") or generator(prompt)[0]["text"]
    return result.strip()

def ask_question(faiss_index, generator, query):
    docs = faiss_index.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"""You are a helpful medical assistant. Answer ONLY using the context below.

Context:
{context}

Question: {query}
Answer:"""
    return call_local_model(generator, prompt)

def main():
    st.set_page_config(page_title="Medical Chatbot", page_icon="🩺", layout="centered")
    st.title("🩺 Medical Chatbot")
    st.markdown(
        """
        Ask any medical question and get answers based on a medical book.
        Powered by HuggingFace transformers and FAISS similarity search.
        """
    )

    faiss_index = load_faiss_index()
    generator = load_model()

    if faiss_index is None:
        st.stop()

    query = st.text_input("Enter your medical question:", "")
    if st.button("Ask"):
        if query.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                answer = ask_question(faiss_index, generator, query)
            st.markdown("### Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
