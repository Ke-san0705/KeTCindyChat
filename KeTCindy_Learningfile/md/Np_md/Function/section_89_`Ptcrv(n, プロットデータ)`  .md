# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Ptcrv(n, プロットデータ)`  
`Ptcrv(n, プロットデータ)`  
曲線プロットデータの n 番目の節点を返す  
Cindyscript の `PD_n` と同じ  
  
【例】六角形の一部の辺だけ太くする  
```  
Ketinit();  
addax(0);  
  
Circledata("1",[[0,0],[2,0]],["Num=6","dr,1"]);//正六角形を太さ1の実線で描く  
a=Ptcrv(2,cr1);//aをcr1の2番目の節点の座標とする  
b=Ptcrv(4,cr1);//bをcr1の4番目の節点の座標とする  
Partcrv("1",a,b,"cr1",["dr,3"]);//cr1のa-b間を太さ3の実線で描く。  
  
Windispg();  
```
