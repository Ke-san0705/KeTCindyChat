# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Nearestptcrv(座標, プロットデータ)`  
`Nearestptcrv(座標, プロットデータ)`  
点に最も近いプロットデータの点を求める  
第1引数の座標に最も近い曲線プロットデータ上の点の座標を返す。  
【例】  
```  
Ketinit();  
Setketcindyjs(["Figure=y"]);  
Putpoint("A",[1,1],[A.x,A.y]);  
  
Plotdata("1","x^2","x",["Num=200","dr"]);//y=x^2のグラフを描く  
  
nrst=Nearestptcrv(A,"gr1");//点Aとgr1の距離が最も近いgr1上の点の座標を取得する  
Pointdata("1",nrst,["Size=4"]);nrstの座標に点を打つ  
Listplot("1",[A,nrst],["da"]);点A-nrst間に線を引く  
  
  
Windispg();  
```
