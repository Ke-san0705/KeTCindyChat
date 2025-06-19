# 平面の図形とグラフ  
## 設定・定義  
### 環境設定  
#### `Usegraphics("tpic"/"pict2e"/"tikz")`  
`Usegraphics("tpic"/"pict2e"/"tikz")`  
TeXのグラフィクスパッケージを変更する。  
なお、これはInitializationスロットに追記する形で記述するため注意すること。  
【例】TeX出力時に使うグラフィックスパッケージをtikzに変更する。  
```  
Usegraphics("tikz")  
```  
引数は文字列であるが、許されているのは"tpic"/"pict2e"/"tikz"の3つである。  
  
### 描画設定・定義
