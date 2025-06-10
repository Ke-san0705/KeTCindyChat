# import os
# import json
# import numpy as np
# import faiss
# from dotenv import load_dotenv
# from openai import OpenAI
# from tqdm import tqdm

# # --- 環境変数からAPIキーを読み込み ---
# load_dotenv()
# client = OpenAI()

# # --- 設定 ---
# EMBED_MODEL = "text-embedding-3-small"
# JSONL_PATH = "tagged_chatbot_data.jsonl"
# TOP_K = 3

# # --- JSONLファイル読み込み ---
# entries = []
# with open(JSONL_PATH, "r", encoding="utf-8") as f:
#     for line in f:
#         entries.append(json.loads(line))

# # --- Embedding生成 ---
# print("🔄 ベクトルを生成中...")
# texts = [entry["content"] for entry in entries]
# embeddings = []

# for i in tqdm(range(0, len(texts), 100)):
#     batch = texts[i:i + 100]
#     res = client.embeddings.create(model=EMBED_MODEL, input=batch)
#     batch_embeddings = [d.embedding for d in res.data]
#     embeddings.extend(batch_embeddings)

# embedding_matrix = np.array(embeddings).astype("float32")

# # --- FAISSインデックス構築 ---
# index = faiss.IndexFlatL2(len(embedding_matrix[0]))
# index.add(embedding_matrix)

# # --- 応答生成関数 ---
# def search_and_respond(query):
#     query_vec = client.embeddings.create(
#         model=EMBED_MODEL,
#         input=[query]
#     ).data[0].embedding

#     D, I = index.search(np.array([query_vec]).astype("float32"), TOP_K)
#     results = [entries[i] for i in I[0]]

#     context = "\n\n".join([f"【{r['title']}】\n{r['content']}" for r in results])

#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "あなたはKeTCindyという数学ソフトに詳しい専門アシスタントです。"},
#             {"role": "user", "content": f"{context}\n\n質問：{query}"}
#         ],
#         temperature=0.2
#     )
#     return response.choices[0].message.content

# # --- 実行 ---
# if __name__ == "__main__":
#     print("KeTCindy ChatBot へようこそ")
#     while True:
#         user_input = input("質問をどうぞ（終了=exit）：")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         try:
#             answer = search_and_respond(user_input)
#             print("💡 回答:", answer, "\n")
#         except Exception as e:
#             print("⚠️ エラー:", str(e))


import os
import json
import numpy as np
import faiss
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

# --- 環境変数からAPIキーを読み込み ---
load_dotenv()
client = OpenAI()

# --- 設定 ---
EMBED_MODEL = "text-embedding-3-small"
JSONL_PATH = "tagged_chatbot_data.jsonl"
TOP_K = 3
REJECT_PATTERNS = ["import ", "def ", "matplotlib", "plt.", "print(", "Python"]

# --- JSONLファイル読み込み ---
entries = []
with open(JSONL_PATH, "r", encoding="utf-8") as f:
    for line in f:
        entries.append(json.loads(line))

# --- Embedding生成 ---
print("🔄 ベクトルを生成中...")
texts = [entry["content"] for entry in entries]
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
    context = "\n\n".join([f"【{r['title']}】\n{r['content']}" for r in results])

    system_prompt = (
        "あなたはKeTCindyという数学ソフトに詳しい専門アシスタントです。"
        "出力するコードは必ずKeTCindy（CindyScriptやKeTCindyJS）の構文を使用してください。"
        "Pythonや他のプログラミング言語で出力しないでください。"
        "KeTCindyでの表現が難しい場合は、その理由と近い構文を説明してください。"
    )

    for attempt in range(2):  # フィルター付き再生成を1回まで許容
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

# --- 実行 ---
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

