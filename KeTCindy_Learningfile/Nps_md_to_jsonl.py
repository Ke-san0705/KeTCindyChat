import os
import json
import re

input_root = "md./Np_md"
output_dir = "jsonl./Np_jsonl"
os.makedirs(output_dir, exist_ok=True)

# Function用出力ファイル
function_jsonl_path = os.path.join(output_dir, "function.jsonl")
function_outfile = open(function_jsonl_path, 'w', encoding='utf-8')

# テキスト整形
def clean(text):
    return re.sub(r'\s+', ' ', text).strip()

# Function系：1行ずつ変換
def convert_function_md(md_path, filename, jsonl_writer):
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = clean(line)
            if line:
                item = {
                    "prompt": filename,
                    "completion": line
                }
                jsonl_writer.write(json.dumps(item, ensure_ascii=False) + '\n')

# 一般ドキュメント：見出し単位で変換
def convert_general_md(md_path, jsonl_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    current_prompt = None
    current_content = []

    with open(jsonl_path, 'w', encoding='utf-8') as out_file:
        for line in lines:
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

        if current_prompt and current_content:
            item = {
                "prompt": clean(current_prompt),
                "completion": clean('\n'.join(current_content))
            }
            out_file.write(json.dumps(item, ensure_ascii=False) + '\n')

# 全体を走査
for root, _, files in os.walk(input_root):
    for file in files:
        if file.endswith(".md"):
            md_path = os.path.join(root, file)
            if "Function" in md_path:
                convert_function_md(md_path, os.path.splitext(file)[0], function_outfile)
            else:
                jsonl_name = os.path.splitext(file)[0] + ".jsonl"
                jsonl_path = os.path.join(output_dir, jsonl_name)
                convert_general_md(md_path, jsonl_path)

function_outfile.close()
print("✅ 変換が完了しました（Functionは1行1項目）。")
