import os
import json
import re

# --- 変数設定 ---
root_dir = "sample"  # ルートフォルダ（変更可）

# --- サブフォルダごとに処理 ---
for subdir, dirs, files in os.walk(root_dir):
    # .md ファイルがなければスキップ
    md_files = [f for f in files if f.endswith(".md")]
    if not md_files:
        continue

    # 出力ファイル名（ルートからの相対パスでサブフォルダ名を取得）
    rel_folder = os.path.relpath(subdir, root_dir)
    folder_name = rel_folder.replace(os.sep, "_") if rel_folder != "." else "root"
    output_jsonl = f"{folder_name}.jsonl"
    jsonl_data = []

    for file in md_files:
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

    # 出力（対象データがある場合のみ）
    if jsonl_data:
        with open(output_jsonl, "w", encoding="utf-8") as f_out:
            for entry in jsonl_data:
                f_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"✅ {len(jsonl_data)} entries written to {output_jsonl}")
