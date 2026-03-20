# 🩺 Medical RAG Based on LLMs

Medical RAG is a local, privacy-respecting AI assistant that answers medical questions based on the content of a PDF textbook. 
It is designed for offline use, requiring no internet and no API keys, making it ideal for educational, private, or restricted environments.

## 🚀 Features
- 📘 **PDF-Based Knowledge**: Load a medical textbook and answer questions using its content.
- 💡 **Context-Aware Answers**: Relevant content is retrieved via FAISS vector search before generating responses.
- 🤖 **Local LLM**: Uses HuggingFace's `flan-t5-base` to generate answers — 100% local, no OpenAI.
- 🧠 **Semantic Search with Embeddings**: Powered by `all-MiniLM-L6-v2`.
- ⚡ **No Internet Needed**: After first-time setup, it runs entirely offline.
- 🖥️ **Streamlit Interface**: Clean, interactive, and easy to use.

All answers are generated using only the context retrieved from the medical PDF, ensuring responses remain grounded and trustworthy.

---

🎯 Use Cases
- ✅ Medical students and educators needing quick, contextual answers
- ✅ Environments with no internet access or privacy concerns
- ✅ Developers building Retrieval-Augmented Generation (RAG) apps
- ✅ Anyone interested in combining LLMs with vector search and document understanding

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

## 📦 Tech Stack
- Layer	Tool
- UI	Streamlit
- PDF Loader	LangChain PyPDFLoader
- Text Splitter	LangChain RecursiveCharacterTextSplitter
- Embeddings	sentence-transformers/all-MiniLM-L6-v2
- Vector DB	FAISS
- LLM	google/flan-t5-base
- Pipeline	HuggingFace text2text-generation

 ---
 
## 📬 Get in Touch
- aakashpawar496@gmail.com
- Made by AAKASH PAWAR

⚠️ This chatbot is for educational and demonstration purposes only. It is not a replacement for professional medical advice. Always consult a qualified healthcare provider for medical concerns.

---
