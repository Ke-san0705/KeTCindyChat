# 平面の図形とグラフ  
## 描画  
### 関数のグラフ  
#### `Paramplot(name , 式 , 変数と定義域,options)`  
`Paramplot(name , 式 , 変数と定義域,options)`  
媒介変数表示の曲線を描く。  
式は""でくくった媒介変数表示のリストで与える。  
定義域も " " でくくって文字列とし，`t=`に続いてリストで指定する。  
options は線種が有効  
  
【例】リサージュ図形を描く。(リサージュ図形は[cos(a*t),sin(b*t)]で表される。)  
```  
Ketinit();  
  
Paramplot("1","[cos(5*t),sin(7*t)]","t=[0,2*pi]",["Num=2000"]);//[cos(a*t),sin(b*t)]で表される媒介変数表示のグラフを0<t<2piの範囲で描く。式を変えるなら2番目の引数(数式が書いてあるリスト)、範囲を変えるなら"t="を変える。媒介変数はtでなくてもいい。そのときは、範囲をその変数で定義すること。(媒介変数がsなら範囲は"s=[-1,1]"などとする。)  
  
Windispg();  
```  
  
【例】太線にする。  
```  
Paramplot("2","[2*cos(t),sin(t)]","t=[0,2*pi]",["dr,2"]);//2*cos(t),sin(t)で表されるグラフを0<t<2piの範囲で太さ2の実線で描く。  
```
