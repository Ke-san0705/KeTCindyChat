# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Mkbezierptcrv( ptlist，[オプション] )`  
`Mkbezierptcrv( ptlist，[オプション] )`  
ベジェ曲線を描く  
**制御点は，自動的に配置される。**  
ptlistには節点を記載する。  
複数の場合は` [ ptlist1, ptlist2.... ]`  
名前は，a から順に自動的につける。  (プロットデータ名はbza,bzb,bzc...となる)  
オプション  
"Deg=..." 次数指定ができる。（初期設定は 3 次）  
"Num=..." 各区間の区間数（分点数 −1）を指定できる。（初期設定は 10）  
  
【例】  
```  
Ketinit();  
Putpoint("A",[-5,0],[A.x,A.y]);  
Putpoint("B",[5,0],[B.x,B.y]);  
Putpoint("C",[2,3],[C.x,C.y]);  
Mkbezierptcrv([A,B,C]);//A-B,B-C間を3次のベジェ曲線で結ぶ。制御点は自動生成。  
  
Windispg();  
```  
  
その他の例  
【例】制御点の数を1つにする  
```  
Mkbezierptcrv([A,B,C],["Deg=2"]);//A-B,B-C間を2次のベジェ曲線で結ぶ。制御点は自動生成。次元数に応じてDeg=の値を書き換える。3次元なら3でよい。  
```  
【例】節点の数を増やす  
```  
Mkbezierptcrv([A,B,C,D,E,F,X]);//点の数に応じてptlistのリストの長さを変化させる。  
```  
【例】複数の場合  
```  
Mkbezierptcrv([[A,B,C],[D,E,F,G]]);//A-B,B-C間とD-E,E-F,F-G間をそれぞれ3次のベジェ曲線で結ぶ。  
```
