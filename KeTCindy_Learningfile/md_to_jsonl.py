import os
import json
import re

# 入力と出力のパス
input_dir = "md./Learning_md"
output_dir = "jsonl./Learning_jsonl"
os.makedirs(output_dir, exist_ok=True)

# ファイルとジャンルの対応
genre_map = {
    "overview": ["About_KeTCindyandCindy.md"],
    "KeTCindyreference2019": ["KeTCindyReference2019.md"],
    "KeTCindyreference2021": ["KeTCindyReference2021.md"],
    "CindySqriptreference": ["CindyReference.md"],
    "howto": ["how_to_ket.md"],
    "installation": ["Installation.md"],
    "latex": ["WritingLATEX.md"]
}

# テキストクリーニング関数
def clean(text):
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip()

# MarkdownをJSONL形式に変換
for genre, files in genre_map.items():
    jsonl_path = os.path.join(output_dir, f"{genre}.jsonl")
    with open(jsonl_path, 'w', encoding='utf-8') as out_file:
        for fname in files:
            path = os.path.join(input_dir, fname)
            if not os.path.exists(path):
                continue
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()

            current_prompt = None
            current_content = []

            for line in lines:
                # 見出しを「質問」と見なす（##以上の階層）
                if re.match(r'^#{2,3} ', line):
                    if current_prompt and current_content:
                        item = {
                            "prompt": clean(current_prompt),
                            "completion": clean('\n'.join(current_content))
                        }
                        out_file.write(json.dumps(item, ensure_ascii=False) + '\n')
                    current_prompt = re.sub(r'^#+ ', '', line)
                    current_content = []
                else:
                    current_content.append(line)

            # 最後のセクションも保存
            if current_prompt and current_content:
                item = {
                    "prompt": clean(current_prompt),
                    "completion": clean('\n'.join(current_content))
                }
                out_file.write(json.dumps(item, ensure_ascii=False) + '\n')

print("✅ 変換が完了しました！output_jsonl/ を確認してください。")
