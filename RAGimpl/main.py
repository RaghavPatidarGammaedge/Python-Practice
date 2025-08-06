from sentence_transformers import SentenceTransformer
import faiss
import requests
import pandas as pd
import nltk
nltk.download('punkt')


def load_csv(file_path):
    df = pd.read_csv(file_path)
    docs = []
    for _, row in df.iterrows():
        content = f"""Index: {row['Index']}
        Organization Id: {row['Organization Id']}
        Name: {row['Name']}
        Website: {row['Website']}
        Country: {row['Country']}
        Description: {row['Description']}
        Founded: {row['Founded']}
        Industry: {row['Industry']}
        Number of Employees: {row['Number of employees']}"""
        docs.append(content)
    return docs

def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_chunks(chunks, model):
    return model.encode(chunks)

def create_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index

def search_top_k(query, model, chunks, index, k=3):
    query_vec = model.encode([query])
    scores, indices = index.search(query_vec, k)
    return [chunks[i] for i in indices[0]]

def generate_response_with_llama(query, top_chunks):
    context = "\n".join(top_chunks)
    prompt = f"""Use the following information to answer the user's question.

Context:
{context}

Question:
{query}

Answer:"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]

def main():
    docs = load_csv("organizations.csv")  # ✅ use your actual CSV file here
    print("✅ Documents loaded from CSV")

    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc))
    print("✅ Documents chunked")

    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_vectors = embed_chunks(all_chunks, embed_model)
    print("✅ Embeddings created")

    index = create_faiss_index(chunk_vectors)
    print("✅ FAISS index created")

    while True:
        query = input("\n🔍 Ask a question (or type 'exit'): ")
        if query.lower() == 'exit':
            break

        top_chunks = search_top_k(query, embed_model, all_chunks, index)
        answer = generate_response_with_llama(query, top_chunks)

        print("\n🤖 Answer:\n", answer)

if __name__ == "__main__":
    main()
