# 平面の図形とグラフ  
## 描画  
### 関数のグラフ  
#### `Tangentplot(name , PD , 位置 , options)`  
`Tangentplot(name , PD , 位置 , options)`  
接線を描く。プロットデータの名前は，`lntn`  
曲線 PD の指定した位置での接線を描く。位置は `"x=n"` で指定する。  
  
【例】y=sin xのx=1での接線を描く。  
```  
Ketinit();  
  
Plotdata("1","sin(x)","x",["Num=200"]);//y=sin (x) のグラフを描くプロットデータ名はgr1となる。  
Tangentplot("1","gr1","x=1");//y=sin xのグラフ(gr1と定義した)のx=1での接線を描く。プロットデータ名はlntn1となる。  
  
Windispg();  
```  
  
### 文字
