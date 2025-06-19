# 平面の図形とグラフ  
## 描画  
### マーキング  
#### `Segmark(name, リスト,options)`  
`Segmark(name, リスト,options)`  
線分に印をつける  
リストで与えられた 2 点を端点とする線分に印をつける。  
  
オプション  
Type=印の種類 `"seg(,n)","cir","poly(,n)" `   
`Width`：線の幅，`Size`：大きさ  
  
【例】  
```  
Ketinit();  
addax(0);  
  
Putpoint("A",[-1.5,-0.5],[A.x,A.y]);  
Putpoint("B",[0,2.5],[B.x,B.y]);  
Putpoint("C",[1.5,-0.5],[C.x,C.y]);  
Putpoint("D",[2,0],[D.x,D.y]);  
  
Listplot([A,B,C,D,A]);  
Segmark("1",[A,B],["Type=seg,1"]);//線が1本の印  
Segmark("2",[B,C],["Type=seg,2","Width=1.2"]);//線が2本で太さ1.2の印  
Segmark("3",[C,D],["Type=cir"]);//丸印  
Segmark("4",[D,A],["Type=poly,4","Size=1.5"]);//四角形の印で、大きさが1.5  
  
Windispg();  
```  
  
【例】多角形の印の頂点の数を変更する  
```  
Segmark("1",[D,A],["Type=poly,6","Size=1.5"]);//六角形の印を付ける。  
Segmark("2",[A,B],["Type=poly,3","Size=1.5"]);//三角形の印を付ける。  
```
