# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Shade(("名前"), プロットデータのリスト , options)`  
`Shade(("名前"), プロットデータのリスト , options)`  
閉曲線で囲まれた領域を塗りつぶす。  
第１引数には，閉曲線を与える曲線分のプロットデータ名を並べる。  
デフォルトでは，Joincrvs を使って閉曲線を作っている。ただし，プロットデータのリストに"Invert()"が入っていれば，Enclosing を使う。  
option の Color は，Cinderella の画面上での描画色をリストで与える。濃さを指定したい場合は色名や RGBではなく CMYK にする。  
options には，他に，次のものがある。  
・Enclosing を使うかどうか："Enc=y/n"（初期値は n）  
　　　"Enc=y" のとき，複数の Shade を使うときは，名前をつける。  
・Enclosing のときの開始点，描画色  
・描画領域のトリミング："Trim=y/n" （初期値は n ）  
・TeX への書き出しで，先頭に配置するか："First=y/n" （初期値は n ）  
　　　"First=n" のときは，使われている Gdata の書き出しの直前におく．  
  
【例】 y=x+2 とy=x^2のグラフの内側を塗りつぶす。  
```  
Ketinit();  
  
Plotdata("1","x^2","x",["Num=200"]);//y=x^2のグラフを描く  
Plotdata("2","x+2","x",["Num=200"]);//y=x+2のグラフを描く  
  
Enclosing("1",["gr1","gr2"],["nodisp"]);//y=x^2のグラフとy=x+2のグラフから閉曲線を作る  
Shade(["en1"],["Color=red"]);//en1の内部を赤色(red)で塗る  
  
Windispg();  
```  
  
【例】描画範囲外は塗りつぶさない  
```  
Ketinit();  
addax(0);  
  
Circledata("1",[[0,0],[2,0]],["dr,2"]);  
Shade("1",["cr1"],["color=red","Trim=y"]);//描画範囲以外は塗りつぶさない("Trim=y")  
  
Windispg();  
  
```
