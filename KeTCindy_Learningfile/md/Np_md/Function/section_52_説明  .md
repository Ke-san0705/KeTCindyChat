# 平面の図形とグラフ  
## 描画  
### 曲線  
#### 説明  
説明  
点リストで 2 つの焦点と通る点を与える。点は Cinderella の幾何点が使える。  
また，通る点のかわりに，焦点からの距離の差を実数で与えることもできる。  
option として，`"Asy=線種"`を与えると，漸近線を指定した線種で表示する。 初期設定では漸近線は非表示。  
  
【例】  
```  
Ketinit();  
  
Putpoint("A",[0,0],[A.x,A.y]);  
Putpoint("B",[3,0],[B.x,B.y]);  
Putpoint("C",[4,2],[C.x,C.y]);  
Hyperbolaplot("1",[A,B,C]); //点A,Bを焦点とし、Cを通る双曲線を描く。  
Pointdata("1",[A,B,C],["Size=2"]);  
Letter([A,"s2","A",B,"s2","B",C,"s2","C"]);  
Windispg();  
```  
  
【例】  
```  
Hyperbolaplot("1",[A,B,2]);//点A,Bを焦点とし、焦点からの距離の差が 2 の双曲線を描く。  
```  
【例】  
```  
Hyperbolaplot("1",[A,B,C],["Asy=do"]);//漸近線を点線で描く。  
```
