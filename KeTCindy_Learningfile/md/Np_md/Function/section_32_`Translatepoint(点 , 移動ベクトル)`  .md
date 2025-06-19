# 平面の図形とグラフ  
## 描画  
### 点・線分・直線  
#### `Translatepoint(点 , 移動ベクトル)`  
`Translatepoint(点 , 移動ベクトル)`  
点を平行移動する  
点を移動ベクトルで示された分だけ平行移動した点の座標を返す  
【例】点 A～D は作図しておく。  
点 C を点 A を x 軸方向に 2 , y 軸方向に 3 だけ平行移動した点にする。  
点 D を点 A をベクトル OB だけ平行移動した点にする。  
```  
C.xy=Translatepoint(A,[2,3]);  
D.xy=Translatepoint(A,B.xy);  
```
