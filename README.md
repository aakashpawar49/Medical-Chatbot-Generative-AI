# 🩺 Medical Chatbot – PDF-Based Q&A with Local LLMs

Welcome to **Medical Chatbot**, a locally-running AI assistant that answers medical questions based on the content of a medical textbook. 
It uses **LangChain**, **FAISS**, and **HuggingFace Transformers**, all running offline — no API keys required.


## 🚀 Features

- 📘 **PDF-Based Knowledge**: Load a medical textbook and answer questions using its content.
- 💡 **Context-Aware Answers**: Relevant content is retrieved via FAISS vector search before generating responses.
- 🤖 **Local LLM**: Uses HuggingFace's `flan-t5-base` to generate answers — 100% local, no OpenAI.
- 🧠 **Semantic Search with Embeddings**: Powered by `all-MiniLM-L6-v2`.
- ⚡ **No Internet Needed**: After first-time setup, it runs entirely offline.
- 🖥️ **Streamlit Interface**: Clean, interactive, and easy to use.

---

## 🧠 How It Works (Behind the Scenes)

- Document Loading: Loads a PDF using PyPDFLoader.
- Chunking: Splits the book into ~500-character chunks with overlap.
- Embeddings: Each chunk is turned into a vector using all-MiniLM-L6-v2.
- Vector Search: On every question, FAISS retrieves the most similar chunks.
- Prompting: The chunks + question are sent to the flan-t5-base model.
- Answer: The model generates a human-like answer using only the provided context.
  
---

## 📸 Screenshots

| Ask a medical question and Answer generated using FAISS + Flan-T5 |
|-------------------------------------------------------------------|
| ![image](https://github.com/user-attachments/assets/3625e487-67e0-48fc-ac80-c22a40b234c3) |

---

## 🛡 Disclaimer
This chatbot is intended for educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## 📬 Contact

- aakashpawar496@gmail.com
- Built by Aakash Pawar
