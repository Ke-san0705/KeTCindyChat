# 操作方法など  
## 始め方  
Cinderellaを起動し、テンプレートを開く   
テンプレートは、`./doc/work/template`に入っている。  
このテンプレートをもとに、プロジェクトを作成する。  
cindyscriptは、  スクリプトタブのcindyscriptから開いて編集する。  
主にdrawスロットのコードを編集する  
## 作図したデータを出力する  
### TeXで使える形にする  
ParentボタンもしくはFigureボタン(figpdf関数を用いた場合は、Parentボタン)を押すとcdyファイルと同じディレクトリに./fig/(ファイル名).texが出力される。  
このTeXファイルを適当なテキストエディタで開けば作った図が外部で利用できる  
### pdfに出力する  
ParentボタンもしくはFigureボタン(figpdf関数を用いた場合は、Parentボタン)を押すとcdyファイルと同じディレクトリに./fig/(ファイル名).pdfが出力され Sumatra PDFが起動しプレビューが表示される。  
### HTMLに出力する  
「ファイルタブからHTML書き出す」からHTMLファイルを作成し、その上でketjsonボタンを押すと./(ファイル名)json.htmlが作成されるので、それを開く。なおjsonという名前がつくが、意味的にはjs+onであり、ファイル形式のjsonとは全く関係ない  
## 関数の使用例を調べる  
Help関数を以下のように書いて実行する  
```  
Help("Listplot");//Listplot関数に関するHelpを取得する  
```  
