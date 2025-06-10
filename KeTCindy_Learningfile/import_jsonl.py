import os
import re
import json

# 入力と出力ディレクトリのパス（必要に応じて変更）
input_dir = "./KeTCindy_Learningfile/output_md"
output_jsonl_path = "./tagged_chatbot_data.jsonl"

# タグ付けルール：キーワード → タグ
tag_rules = [
    (r"インストール|セットアップ|環境", ["インストール", "初心者向け", "環境構築"]),
    (r"Plotdata|Drawline|Circle|Draw", ["図形描画", "関数", "中級者向け"]),
    (r"LaTeX|数式|Text\(", ["数式描画", "LaTeX", "中級者向け"]),
    (r"スライダー|アニメーション|動的", ["アニメーション", "上級者向け"]),
    (r"KeTCindy|CindyScript|CindyJS", ["KeTCindy", "構文"]),
    (r"ファイル|保存|読み込み|書き出し", ["外部連携", "中級者向け"]),
    (r"基本|操作|使い方", ["初心者向け", "基本操作"]),
]

# 結果格納
tagged_entries = []

# 各Markdownファイルを処理
for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
            text = f.read()

        # セクション単位に分割
        sections = re.split(r"(?m)^##+\s+", text)
        for section in sections:
            if section.strip():
                lines = section.strip().splitlines()
                title = lines[0] if lines else "Untitled"
                content = "\n".join(lines[1:]) if len(lines) > 1 else ""

                if len(content.strip()) < 30:
                    continue

                # タグ推定
                matched_tags = set()
                for pattern, tags in tag_rules:
                    if re.search(pattern, content, re.IGNORECASE):
                        matched_tags.update(tags)

                tagged_entries.append({
                    "title": title.strip(),
                    "content": content.strip(),
                    "tags": sorted(matched_tags)
                })

# JSONL形式で書き出し
with open(output_jsonl_path, "w", encoding="utf-8") as f:
    for entry in tagged_entries:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"✅ 完了：{output_jsonl_path} に {len(tagged_entries)} 件のエントリを書き出しました。")
