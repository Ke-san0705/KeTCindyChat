# 平面の図形とグラフ  
## 描画  
### マーキング  
#### `Anglemark(name, 点リスト , options)`  
`Anglemark(name, 点リスト , options)`  
点リストで示された角に弧の形状の角の印をつける。  
`Listplot()` などと同様，点リストが点名の場合は name は省略できる。弧を描かず文字だけを入れる場合はoptions に "nodisp" を指定する。  
options は次の通り。  
数値角の印の大きさ。 初期設定は１  
線種`"dr, n", "da,m,n" , "do,m,n"  `  
`"Expr=文字"` または`"Letter=文字"` : 文字を入れる  
`"Expr=位置 , 文字"`: 位置を指定して文字を入れる。位置は頂点からの距離。  
  
【例】\angle ABC に印をつけて、文字を書き込む  
```  
Ketinit();  
Addax(0);  
Putpoint("A",[-2,-1],[A.x,A.y]);  
Putpoint("B",[1,3],[B.x,B.y]);  
Putpoint("C",[2,-1],[C.x,C.y]);  
Listplot("1",[A,B,C],["dr,2"]);  
Anglemark([A,B,C],[2,"dr,2","Expr=1.2,\theta"]);  
Letter(A,"e2","A");  
Letter(B,"w2","B");  
Letter(C,"n2","C");  
Windispg();  
```
