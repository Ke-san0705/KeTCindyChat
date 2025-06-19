# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Intersectcrvs(プロットデータ 1, プロットデータ 2)`  
`Intersectcrvs(プロットデータ 1, プロットデータ 2)`  
2 曲線の交点リストを取得する。  
オプションとして，共有点があるかどうかを判断するための限界値があるが，通常は使わない。  
【例】  
```  
Ketinit();  
  
Plotdata("1","x^2","x",["Num=200","dr"]);//y=x^2のグラフを描く  
Plotdata("2","x+2","x",["Num=200","dr"]);//y=x+2のグラフを描く  
intscs = Intersectcrvs("gr1", "gr2");//gr1とgr2の交点をすべて求め、リストで格納  
Pointdata("1",intscs_1,["Size=4"]);//gr1とgr2の交点のうち1番目を大きさ4でプロット  
Pointdata("2",intscs_2,["Size=4"]);//gr1とgr2の交点のうち2番目を大きさ4でプロット  
  
Windispg();  
```
