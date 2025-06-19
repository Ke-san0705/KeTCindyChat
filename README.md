# KeTCindyChat の簡単な仕組み

## ディレクトリ構成

- `KeTCindy_Learningfile./Knowlage`  
  参考にした資料を格納

- `KeTCindy_Learningfile./md`  
  KeTCindyに関するリファレンス・資料をMarkdown形式で記述

- `KeTCindy_Learningfile./jsonl`  
  KeTCindyに関するリファレンス・資料をjsonl形式で記述

- 各種変換コードは `KeTCindy_Learningfile` 内に配置

- `Nps_md_to_jsonl.py`,`Learning_md_to_jsonl.py` それぞれ対応したフォルダ内の.mdを.jsonlに変換

-  `Knowlage_to_md` Knowlage内にある.pdfを.mdに変換。 (精度が荒いため改善中)

## KeTCindyChat.py の仕組み

1. ユーザーの質問を **Embedding** でベクトル化
2. `KeTCindy_Learningfile./jsonl` から検索
3. 得られた結果を文脈として **OpenAI GPT-4** に入力し、最も適切なKeTCindyコードや解説を生成

---

# アップデート予定（願望）

- 会話内容を今後の回答のために学習・反映させる
- 現在のリファレンスと既存コード・実行結果を活用して、学習用Markdownを自動生成する
- 特定の単語入力で即座に回答が返る辞書的応答機能を実装
- GitHubへの組み込み（**済み**）