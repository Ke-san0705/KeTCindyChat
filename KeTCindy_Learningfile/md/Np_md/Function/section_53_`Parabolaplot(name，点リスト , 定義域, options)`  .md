# 平面の図形とグラフ  
## 描画  
### 曲線  
#### `Parabolaplot(name，点リスト , 定義域, options)`  
`Parabolaplot(name，点リスト , 定義域, options)`  
点リスト [A,B,C] で示された焦点，準線で決まる放物線を描く。  
焦点 A と準線 BC で決定する放物線を描く。  
実際には，2 次関数  y = x^2  のグラフを回転・平行移動して描いており，定義域は，y = x^2 での定義域と考えてよい。定義域は省略することもできる。省略したときの初期値は [-5,5]  
  
【例】点 A を焦点，直線 BC を準線とする放物線を描く  
  
```  
Ketinit();  
  
Putpoint("A",[0,0],[A.x,A.y]);  
Putpoint("B",[3,0],[B.x,B.y]);  
Putpoint("C",[4,2],[C.x,C.y]);  
Parabolaplot("1",[A,B,C],["Num=200"]);//焦点A,準線が直線BCである放物線を描画する。  
Pointdata("1",[A,B,C],["Size=2"]);  
Letter([A,"e2","A",B,"s2","B",C,"s2","C"]);  
Windispg();  
```
