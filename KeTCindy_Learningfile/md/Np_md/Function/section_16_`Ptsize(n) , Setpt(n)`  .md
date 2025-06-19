# 平面の図形とグラフ  
## `Defvar(文字列)`  
### 描画設定・定義  
#### `Ptsize(n) , Setpt(n)`  
`Ptsize(n) , Setpt(n)`  
表示する点の大きさを設定する。  
`Ptsize()` と `Setpt()` は同じである。 初期設定は１  
全体の点の大きさを設定する。  
【例】  
```  
Ptsize(4);//点のサイズを4に変更。次実行するまで有効  
```  
  
点の大きさを個々に変えたい場合は，以下のようにsize オプションを用いる。  
【例】１から 4 までの点の大きさ  
```  
Pointdata("1",A,["Size=1"]);  
Pointdata("2",B,["Size=2"]);  
Pointdata("3",C,["Size=3"]);  
Pointdata("4",D,["Size=4"]);  
```
