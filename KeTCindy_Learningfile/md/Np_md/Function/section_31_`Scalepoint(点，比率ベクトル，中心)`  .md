# 平面の図形とグラフ  
## 描画  
### 点・線分・直線  
#### `Scalepoint(点，比率ベクトル，中心)`  
`Scalepoint(点，比率ベクトル，中心)`  
点の位置の拡大・縮小を行う  
点を，指定された中心を原点とする座標系で，比率ベクトルの分だけ拡大・縮小した位置の座標を返す。  
【例】点 A～F は作図ツールで適当な位置にとっておく。  
点 D を，点 A を原点を中心に横に 3 倍，縦に 2 倍した位置に置く。  
点 E を，点 A を点 B を中心に横に 3 倍，縦に 2 倍した位置に置く。  
点 F を，点 A を原点を中心にベクトル −−→OC で示された比率の位置に置く。  
```  
D.xy=Scalepoint(A,[3,2],[0,0]);  
E.xy=Scalepoint(A,[3,2],B);  
F.xy=Scalepoint(A,C.xy,[0,0]);  
Arrowdata("1",[[0,0],C]);  
Pointdata("1",[A,B,C,D,E,F],["size=2"]);  
Letter([A,"e2","A("+A.x+","+A.y+")"]);  
Letter([B,"e2","B("+B.x+","+B.y+")"]);  
Letter([C,"e2","C("+C.x+","+C.y+")"]);  
Letter([D,"e2","D("+D.x+","+D.y+")"]);  
Letter([E,"e2","E("+E.x+","+E.y+")"]);  
Letter([F,"e2","F("+F.x+","+F.y+")"]);  
```  
点 A,B,C をドラッグすると，インタラクティブに D,E,F の位置が変わる。
