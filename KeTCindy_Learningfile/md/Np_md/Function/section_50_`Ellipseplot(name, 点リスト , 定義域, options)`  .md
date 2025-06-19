# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Ellipseplot(name, 点リスト , 定義域, options)`  
`Ellipseplot(name, 点リスト , 定義域, options)`  
焦点と通る点を与えて楕円を描く。  
点リストで 2 つの焦点と通る点を与える。点は Cinderella の幾何点が使える。  
また，通る点のかわりに，焦点からの距離の和を実数で与えることもできる。  
  
【例】点 A,B を焦点とする楕円を描く。  
```  
Ketinit();  
addax(0);  
Putpoint("A",[0,0],[A.x,A.y]);  
Putpoint("B",[3,0],[B.x,B.y]);  
Putpoint("C",[4,2],[C.x,C.y]);  
Ellipseplot("1",[A,B,C],["do,2,2"]);// 点 C を通る楕円を描く。(点線)  
Ellipseplot("2",[A,B,4],["da,2"]); //焦点からの距離の和が 4 である楕円を描く。  
Ellipseplot("3",[A,B,C],"[0,pi]",["dr,1"]); //楕円の半分を描く。(角度が0からpiまでを描いている。)  
  
Pointdata("1",[A,B,C],["Size=2"]);  
Letter([A,"s2","A",B,"s2","B",C,"s2","C"]);  
  
Windispg();  
```
