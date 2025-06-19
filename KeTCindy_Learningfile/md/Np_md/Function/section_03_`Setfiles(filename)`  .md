# 平面の図形とグラフ  
## 設定・定義  
### 環境設定  
#### `Setfiles(filename)`  
`Setfiles(filename)`  
出力するファイル名の設定  
出力する Tex のファイル名を指定する。  
出力するファイル名は 初期設定では，作図している Cinderella のファイル名。  
たとえば，triangle.cdy で作図して出力すると，triangle.tex ができる。  
これに対し，triangle.cdy で作図しているときに，grav.tex で出力したい場合は  
```  
Setfiles("grav");  
```  
とすると，grav.tex ができる。
