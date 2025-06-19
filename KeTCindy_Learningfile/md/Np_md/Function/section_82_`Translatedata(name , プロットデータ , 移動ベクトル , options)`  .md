# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Translatedata(name , プロットデータ , 移動ベクトル , options)`  
`Translatedata(name , プロットデータ , 移動ベクトル , options)`  
プロットデータを平行移動する  
プロットデータを移動ベクトルで示された分だけ平行移動する。  
  
【例】y=x^2とそれをx軸方向に2,y軸方向に3移動させたものを描く。  
```  
Ketinit();  
  
Plotdata("1","x^2","x",["Num=200","dr"]);//y=x^2のグラフを描く。  
  
Translatedata("1","gr1",[2,3],["da"]);//gr1をx軸方向に2,y軸方向に3ずらす  
  
Windispg();  
```
