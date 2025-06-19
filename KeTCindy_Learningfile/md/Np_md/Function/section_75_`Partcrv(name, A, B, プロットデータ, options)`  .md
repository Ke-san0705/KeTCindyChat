# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Partcrv(name, A, B, プロットデータ, options)`  
`Partcrv(name, A, B, プロットデータ, options)`  
曲線プロットデータ上の点 A, B の間の部分曲線を描く。  
 2 点 A, B の順序は曲線の向きと同一であること。曲線の向きは，y = f(x) のグラフでは x 座標が増加する向き。  
options は線種"dr, n", "da,m,n" , "do,m,n"  
```  
Ketinit();  
  
Plotdata("1","x^2","x",["Num=200","do"]);  
  
Partcrv("1", [-1,1], [2,4], "gr1",["dr,3"]);//"gr1"の[-1,1]から[2,4]までを太線にする  
  
Windispg();  
```  
  
【例】`Intersectcrvs`を使って動的に交点を求める  
```  
Ketinit();  
Setketcindyjs(["Figure=y"]);  
Putpoint("A",[-2,-1],[A.x,A.y]);  
Putpoint("B",[1,3],[B.x,B.y]);  
  
Lineplot("1",[A,B],["da"]);  
  
Circledata("1",[[0,2],[0,0]],["dr"]);  
tmp=sort(Intersectcrvs("ln1","cr1"));  
print(tmp);  
Intersects=length(tmp);  
if(Intersects>0,  
if(A.x<B.x,  
Partcrv("1",tmp_1,tmp_2,"ln1",["dr,2"]);,  
Partcrv("1",tmp_2,tmp_1,"ln1",["dr,2"]);  
);  
);  
Windispg();  
  
```
