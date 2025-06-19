# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Mkbeziercrv(名前, [節点リスト, 制御点リスト] のリスト,options )`  
`Mkbeziercrv(名前, [節点リスト, 制御点リスト] のリスト,options )`  
複数のベジェ曲線を描く  
 [節点リスト, 制御点リスト] が１つの場合は，Bezier() と同じ。  
【例】  
```  
Ketinit();  
addax(0);  
  
Mkbeziercrv("5",[[[A,B,C],[[D],[E,F]]],[[G,H,K,L],[[M],[N,O],[P]]]],["Num=200"]);//A-B間を点Dで制御、B-C間を点E,Fで制御するベジェ曲線、G-H間を点Mで制御、H-K間を点N,Oで制御、K-L間を点Pで制御するベジェ曲線をそれぞれ描く(PD名は前者がbz51、後者がbz52となる。bz+name+指定した順番となる。)  
Letter([A,"s2","A"]);  
Letter([B,"s2","B"]);  
Letter([C,"s2","C"]);  
Letter([D,"n2","D"]);  
Letter([E,"n2","E"]);  
Letter([F,"n2","F"]);  
Letter([G,"s2","G"]);  
Letter([H,"s2","H"]);  
Letter([K,"s2","K"]);  
Letter([L,"s2","L"]);  
Letter([M,"n2","M"]);  
Letter([N,"n2","N"]);  
Letter([O,"n2","O"]);  
Letter([P,"n2","P"]);  
Pointdata("1",[A,B,C,D,E,F,G,H,K,L,M,N,O,P],["Size=2"]);  
Windispg();  
```
