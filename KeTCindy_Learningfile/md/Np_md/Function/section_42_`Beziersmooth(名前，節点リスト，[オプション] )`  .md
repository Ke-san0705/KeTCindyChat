# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Beziersmooth(名前，節点リスト，[オプション] )`  
`Beziersmooth(名前，節点リスト，[オプション] )`  
節点間を3次ベジェ曲線でスムーズに結んだ曲線を描く  
節点をはさむ制御点は１直線上にとる（したがって，１つは半自由点で，直線上しか動けない）。制御点は自動的に配置される。その後，節点や制御点を動かして，描きたいものにする。  
  
```  
Ketinit();  
  
Setketcindyjs(["Figure=y"]);  
//点A,B,C,Dをそれぞれ定義  
Putpoint("A",[-5,0],[A.x,A.y]);  
Putpoint("B",[5,0],[B.x,B.y]);  
Putpoint("C",[2,3],[C.x,C.y]);  
Putpoint("D",[2,-2],[D.x,D.y]);  
Beziersmooth("1",[A,B,C,D],["num=2000"]);//A-B,B-C,C-D間を3次ベジェ曲線でスムーズに結んだ曲線を描く(節点を挟む制御点は一直線上)  
Pointdata("1",[A,B,C,D],["Size=2"]);  
Letter([A,"n2","A",B,"n2","B",C,"n2","C",D,"n2","D"]);  
  
Windispg();  
```
