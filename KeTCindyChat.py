import os
import json
import numpy as np
import faiss
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

# --- 環境変数の読み込み ---
load_dotenv()
client = OpenAI()

# --- 設定 ---
EMBED_MODEL = "text-embedding-3-small"
DATA_DIRS = [
    "./KeTCindy_Learningfile/jsonl/Learning_jsonl",
    "./KeTCindy_Learningfile/jsonl/Np_jsonl",
    "./KeTCindy_Learningfile/jsonl/Samplecode_jsonl"
]
TOP_K = 3
REJECT_PATTERNS = ["import ", "def ", "matplotlib", "plt.", "print(", "Python"]

# --- JSONLデータ読み込み ---
entries = []
for data_dir in DATA_DIRS:
    for fname in os.listdir(data_dir):
        if fname.endswith(".jsonl"):
            full_path = os.path.join(data_dir, fname)
            with open(full_path, "r", encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line)
                    entries.append(obj)

# --- Embedding生成 ---
print("🔄 ベクトルを生成中...")
# 埋め込み用テキストの抽出とフィルタリング
texts = [entry.get("content") or entry.get("completion") for entry in entries]
texts = [t for t in texts if t and t.strip()]  # ← これを追加（空・Noneを除外）

embeddings = []

for i in tqdm(range(0, len(texts), 100)):
    batch = texts[i:i + 100]
    res = client.embeddings.create(model=EMBED_MODEL, input=batch)
    batch_embeddings = [d.embedding for d in res.data]
    embeddings.extend(batch_embeddings)

embedding_matrix = np.array(embeddings).astype("float32")

# --- FAISSインデックス構築 ---
index = faiss.IndexFlatL2(len(embedding_matrix[0]))
index.add(embedding_matrix)

# --- 応答生成関数 ---
def search_and_respond(query):
    query_vec = client.embeddings.create(
        model=EMBED_MODEL,
        input=[query]
    ).data[0].embedding

    D, I = index.search(np.array([query_vec]).astype("float32"), TOP_K)
    results = [entries[i] for i in I[0]]
    context = "\n\n".join(
        [f"【{r.get('title') or r.get('prompt')}】\n{r.get('content') or r.get('completion')}" for r in results]
    )

    # --- システムプロンプト読み込み ---
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    for attempt in range(2):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"{context}\n\n質問：{query}"}
            ],
            temperature=0.2
        )
        content = response.choices[0].message.content
        if not any(pat in content for pat in REJECT_PATTERNS):
            return content
    return "⚠️ KeTCindy形式での出力ができませんでした。質問をもう少し具体的にして再度お試しください。"

# --- 実行セクション ---
if __name__ == "__main__":
    print("KeTCindy ChatBot へようこそ")
    while True:
        user_input = input("質問をどうぞ（終了=exit）：")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            answer = search_and_respond(user_input)
            print("💡 回答:", answer, "\n")
        except Exception as e:
            print("⚠️ エラー:", str(e))
