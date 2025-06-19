# 平面の図形とグラフ  
## 設定・定義  
### 環境設定  
#### `Addpackage(パッケージ名)`  
`Addpackage(パッケージ名)`  
TeX のパッケージを追加する  
パッケージ名は1つの時文字列で、1つ以上の時リスト形式で記述する。  
なお、これはInitializationスロットに追記する形で記述するため注意すること。  
  
【例】emathパッケージを追加する。  
```  
//以下のどちらか  
Addpackage("emath");  
Addpackage(["emath"]);  
```
