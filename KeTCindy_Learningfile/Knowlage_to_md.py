import pdfplumber
import os
import re

def clean_text(text):
    # 制御文字や不可視文字を除去
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)
    # 無意味な繰り返し（例: あああああ）を一定回数以上で制限
    text = re.sub(r'([ぁ-んァ-ヶ一-龯])\1{4,}', r'\1\1\1', text)
    # 空白の繰り返しを整理
    text = re.sub(r'[ 　]{2,}', ' ', text)
    return text.strip()

# --- カテゴリごとのPDFファイル名 ---
categorized_files = {
    "KeTCindyReference2021": ["KeTCindyReferenceJ.pdf"],
    "KeTCindyReference2019": ["0.pdf"],
    "Installation": ["install-ketcindy.pdf"],
    "WritingLATEX": ["LATEX.pdf", "図形描画.pdf"],
    "CindyReference": ["CindyJSReference2024.pdf"],
}

# --- PDFの格納ディレクトリと出力先 ---
input_dir = "./Knowlage"
output_dir = "md./Learning_md"
os.makedirs(output_dir, exist_ok=True)

# --- PDFをMarkdownに変換 ---
for category, files in categorized_files.items():
    md_path = os.path.join(output_dir, f"{category}.md")
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# {category} ドキュメント\n\n")
        for filename in files:
            pdf_path = os.path.join(input_dir, filename)
            if not os.path.exists(pdf_path):
                md_file.write(f"## {filename}（見つかりませんでした）\n\n")
                continue
            with pdfplumber.open(pdf_path) as pdf:
                md_file.write(f"## {filename}\n\n")
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        cleaned_text = clean_text(text)
                        md_file.write(f"### Page {i+1}\n\n{cleaned_text}\n\n")
                    else:
                        md_file.write(f"### Page {i+1}（テキストなし）\n\n")

print(f"変換が完了しました！ → {output_dir} フォルダをご確認ください")
