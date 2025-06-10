import pdfplumber
import os

# --- カテゴリごとのPDFファイル名 ---
categorized_files = {
    "Reference": [
        "KeTCindyReferenceJ.pdf",
        "CindyJSReference2024.pdf"
    ],
    "HowTo": [
        "howto_k.pdf",
        "howto_o.pdf"
    ],
    "Installation": [
        "install-ketcindy.pdf"
    ],
    "MathDraw": [
        "LATEX.pdf",
        "図形描画.pdf"
    ],
    "Unknown": [
        "0.pdf"
    ]
}

# --- PDFの格納ディレクトリと出力先 ---
input_dir = "./Knowlage"         # ← PDFをこのフォルダに入れておく
output_dir = "./output_md"       # ← Markdown出力先

# --- 出力用ディレクトリを作成 ---
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
                        md_file.write(f"### Page {i+1}\n\n")
                        md_file.write(text + "\n\n")
                    else:
                        md_file.write(f"### Page {i+1}（テキストなし）\n\n")

print(f"変換が完了しました！ → {output_dir} フォルダをご確認ください")
