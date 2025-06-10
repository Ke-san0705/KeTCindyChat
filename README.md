簡単な仕組み

output_md/*.mdにて
KeTCindyに関するリファレンス・解説をMarkdown形式で記述

内容例：インストール方法、関数の使い方、図形描画方法など

tagged_chatbot_data.jsonlにて
.mdの内容を構造化された形式（title + content）に変換して蓄積

KeTCindyChat.py
ユーザーの質問をEmbeddingして、tagged_chatbot_data.jsonl の中から意味的に近いもの（上位K件）を検索（FAISS使用）

その結果を文脈としてOpenAI GPT-4に与え、最も適切なKeTCindyコードや解説を生成

tagged_chatbot_data.jsonlの更新方法
1.output_md/ フォルダに .md ファイルを追加
2.import jsonl.py を実行（たとえばPython環境で python import\ jsonl.py）
3.tagged_chatbot_data.jsonl が再生成・更新され、KeTCindyChatが新しい知識を使えるように


アップデート予定(願望)

・会話内容を今後の回答のために学習し反映させる。
・現状のリファレンスと既にあるコードとその結果を記したファイルを使い学習、自身で学習用mdを作成する。
・特定の単語を入力すると回答が返ってくる
・Githubに組み込む



