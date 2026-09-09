import numpy as np

docs = [
    "machine learning is fun",
    "deep learning uses neural networks",
    "i love walking in the park",
    "neural networks power deep learning",
    "the dog plays in the garden",
    "learning machines can learn",
]

# ========== BƯỚC 1: XÂY TỪ ĐIỂN (vocabulary) ==========
# Gom tất cả từ duy nhất từ mọi câu, gán mỗi từ một chỉ số
all_words = "".join(docs).split()
vocab = sorted(set(all_words))
word_to_idx = {w: i for i, w in enumerate(vocab)}

print(f"Vocab ({len(vocab)} tu): ", vocab)

# ========== BƯỚC 2: CÂU → VECTOR (bag of words) ==========
# Mỗi câu = vector dài bằng vocab; đếm số lần mỗi từ xuất hiện
def text_to_vector(text):
    vec = np.zeros(len(vocab))
    for word in text.lower().split():
        if word in word_to_idx:
            vec[word_to_idx[word]] +=1
    return vec

# Vector hóa TẤT CẢ documents → ma trận (6 câu × N từ)
doc_vectors = np.array([text_to_vector(d) for d in docs])
print("Shape cua ma tran docs:", doc_vectors.shape)

# ========== BƯỚC 3: COSINE SIMILARITY ==========
def cosine_militarity(u, v):
    return np.dot(u, v)/(np.linalg.norm(u) * np.linalg.norm(v))

# ========== BƯỚC 4: SEARCH ==========
def search(query, top_k = 2):
    q = text_to_vector(query)
    # Tính điểm similarity của query với từng document
    scores = np.array([cosine_militarity(q, d) for d in doc_vectors])
    # argsort: sắp xếp theo index, từ nhỏ → lớn; [::-1] đảo ngược thành lớn → nhỏ
    top_idx = np.argsort(scores)[::-1][:top_k]

    print(f'\n🔍 Query: "{query}"')
    for i in top_idx:
        print(f"  {scores[i]:.3f} | {docs[i]}")

# ========== CHẠY THỬ ==========
search("learning neural networks")
search("dog in the park")
search("machines that learn")