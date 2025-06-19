# KeTCindyとCindyScriptの概要まとめ

##  KeTCindyとは
**KeTCindy**は、動的幾何ソフトウェア **Cinderella 2** 上で動作する**プラグイン型のスクリプトライブラリ**です。  
主に **LaTeX / TikZ** などTeX系文書に挿入するための**高品質な図版を生成**することを目的としています。

- GUI操作 + スクリプトによる図作成が可能  
- TeXやPDF、HTML教材の出力に対応  
- 外部の数式処理ソフトとも連携可能（R, Maximaなど）

---

##  CindyScriptとは
**CindyScript**は、Cinderellaに組み込まれている**組み込み型プログラミング言語**です。

- 点や線などの**幾何オブジェクトの制御**  
- **アニメーションや数式処理**  
- KeTCindyのコマンドもこのCindyScriptで記述・実行可能  

---

##  両者の関係性

| 項目 | 内容 |
|------|------|
| KeTCindy | CindyScriptを拡張したライブラリ群 |
| 利用方法 | Cinderella上でCindyScriptとしてKeTCindyの関数・コマンドを記述 |
| 出力 | LaTeX, TikZ, PDF, HTML, 外部数式ソフト用データ など |

---

##  KeTCindyの動作の流れ

1. **Cinderellaで作図**  
   点や線、多角形などをGUIで配置。

2. **CindyScriptエディタで制御**  
   KeTCindyコマンドを使って図の構成や出力形式を定義。

3. **データ出力・外部連携**  
   作図データを外部ソフト（例：R, Maxima）に渡して計算や整形を行い、最終的にTeXやPDF等を生成。

---

##  KeTCindyの特徴・拡張性

-  **400以上のコマンド**が用意された豊富なライブラリ  
-  **R / Maxima ** など外部ソフトと連携可能  
-  関数グラフ、多面体、空間図形など**教材向け機能が充実**  
-  Web教材への応用：**KeTCindyJS**でHTML出力も可能  

---

##  まとめ

KeTCindyは、CinderellaのGUIとCindyScriptのスクリプト機能を統合し、**教育・研究・教材作成**の現場で活用できる強力な図版生成ツールです。  
TeX文書との親和性が非常に高く、**数学・物理の教材開発やプレゼン資料作成に最適**です。

---
