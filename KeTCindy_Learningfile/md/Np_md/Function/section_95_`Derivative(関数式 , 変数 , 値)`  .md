# 平面の図形とグラフ  
## 計算  
### マーキング  
#### `Derivative(関数式 , 変数 , 値)`  
`Derivative(関数式 , 変数 , 値)`  
関数の微分係数を求める  
関数式で与えられた関数の，「変数＝値」における微分係数を求める。  
値は，点の座標を用いることができる。点 A の $$x$$ 座標であれば， `A.x` とする。  
  
【例】$$y=\sin x$$の接線を描く  
```  
Ketinit();  
  
Plotdata("1","sin(x)","x",["Num=200"]);//y=sin xのグラフを描く  
Putoncurve("P","gr1",[0,0]);//gr1上に点Pを置く  
  
D = Derivative("sin(x)","x" , P.x);//xがPのx座標におけるsin xの微分係数を求める  
  
Plotdata("2",Assign("D*(x-P)+sin(P)",["D",D,"P",P.x]),"x",["Num=200"]);//xがPのx座標におけるsin xの微分係数をもちいて接線を描く  
Windispg();  
```
