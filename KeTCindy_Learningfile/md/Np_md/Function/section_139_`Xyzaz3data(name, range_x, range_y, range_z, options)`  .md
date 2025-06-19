# KeTCindy3D  
## `Startsurf(options)`  
### マーキング  
#### `Xyzaz3data(name, range_x, range_y, range_z, options)`  
`Xyzaz3data(name, range_x, range_y, range_z, options)`  
座標軸を描く.  
画面に座標軸を描き, プロットデータ`ax3d`を作成する.  
`name`は空文字列でよい.  
  
`options`は次の2つ.  
- 矢じり`an`: nは数字で矢じりの大きさ(nはなくてもよい).  
- 原点$$\mathrm{O}$$`Onesw`: `nesw`は微小位置. 数字も付けられる(`nesw`をつけない場合, 初期値は`sw`).  
  
【例】初期設定の座標軸.  
```js  
Xyzax3data("", "x=[-5, 5]", "y=[-5, 5]", "z=[-5, 5]");  
```  
矢じりをつける.  
```js  
Xyzax3data("", "x=[-5, 5]", "y=[-5, 5]", "z=[-5, 5]", "a");  
```  
矢じりを大きくする.  
```js  
Xyzax3data("", "x=[-5, 5]", "y=[-5, 5]", "z=[-5, 5]", ["a2"]);  
```  
原点$$\mathrm{O}$$を表示する.  
```js  
Xyzax3data("", "x=[-5, 5]", "y=[-5, 5]", "z=[-5, 5]", ["O"]);  
```  
原点$$\mathrm{O}$$の位置を調整して右上に表示する. 矢じりもつける.  
```js  
Xyzax3data("", "x=[-5, 5]", "y=[-5, 5]", "z=[-5, 5]", ["a", "Oe2n2"]);  
```
