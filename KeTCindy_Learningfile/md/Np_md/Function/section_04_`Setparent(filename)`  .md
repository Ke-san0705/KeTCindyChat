# 平面の図形とグラフ  
## 設定・定義  
### 環境設定  
#### `Setparent(filename)`  
`Setparent(filename)`  
Parent ボタンで出力するファイル名の設定  
Figpdf() を使って Parent ボタンで出力する Tex のファイル名を指定する。  
Parent ボタンで出力するファイル名は 初期設定がないので，指定する必要がある。  
たとえば，triangle.cdy で作図しているときに，図サイズの grav.pdf を作る場合，  
```  
Setparent("grav");  
```  
とすると，図の TeX ファイル triangle.tex と PDF を作る grav.tex ができ，ここから grav.pdf ができる。
