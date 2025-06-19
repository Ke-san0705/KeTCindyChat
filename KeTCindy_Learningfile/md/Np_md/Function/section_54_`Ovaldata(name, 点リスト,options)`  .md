# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Ovaldata(name, 点リスト,options)`  
`Ovaldata(name, 点リスト,options)`  
角を丸くした矩形を描く  
中心と対角の１点を指定し，角を丸くした矩形を描く  
options は，角の落とし具合と線種など。 数字が大きいほど丸くなる。数字で与える。  
```  
Ketinit();  
  
Putpoint("A",[-5,0],[A.x,A.y]);  
Putpoint("B",[5,0],[B.x,B.y]);  
Putpoint("C",[2,3],[C.x,C.y]);  
Putpoint("D",[2,-2],[D.x,D.y]);  
Putpoint("E",[-4,0],[E.x,E.y]);  
Putpoint("F",[2,1],[F.x,F.y]);  
Putpoint("G",[3,-3],[G.x,G.y]);  
Putpoint("H",[4,-2],[H.x,H.y]);  
Ovaldata("1", [A,B]);//角をちょっと丸めた長方形を描く  
Ovaldata("2", [C,D],[0]);//角を丸めない長方形を描く  
Ovaldata("3", [E,F],[1,"dr,3"]);//角を丸めた長方形を太さ3の実線で描く。  
Ovaldata("4", [G,H],[1.5,"da"]);//角を丸めた長方形を破線で描く。  
  
Windispg();  
```  
  
### 関数のグラフ
