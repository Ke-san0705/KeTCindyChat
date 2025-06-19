import os
import json
import re

# --- 変数設定 ---
root_dir = "sample"               # ルートフォルダ名（例: sample）
output_jsonl = "output.jsonl"     # 出力ファイル名

# --- JSONLに格納するリスト ---
jsonl_data = []

# --- 再帰的に.mdファイルを探索して処理 ---
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(subdir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 必要なセクションを抽出
            q = re.search(r"### 想定質問\s*\n+(.+?)\n+---", content, re.DOTALL)
            code = re.search(r"### コード.*?```cindy\n(.+?)```", content, re.DOTALL)
            exp = re.search(r"### 解説とラベル\s*\n+(.+?)\n+---", content, re.DOTALL)
            tags = re.search(r"### ラベル.*?\n+`(.+?)`", content, re.DOTALL)

            if q and code and exp and tags:
                jsonl_data.append({
                    "filename": file,
                    "question": q.group(1).strip(),
                    "code": code.group(1).strip(),
                    "explanation": exp.group(1).strip(),
                    "tags": [tag.strip() for tag in tags.group(1).split("`, `")]
                })
            else:
                print(f"⚠️ Skipped: {file_path}（一部のセクションが見つかりません）")

# --- JSONL形式で保存 ---
with open(output_jsonl, "w", encoding="utf-8") as f_out:
    for entry in jsonl_data:
        f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"✅ {len(jsonl_data)} entries written to {output_jsonl}")
