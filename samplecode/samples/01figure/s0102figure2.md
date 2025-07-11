### 想定質問

三角形ABCに補助点を加え、線分やラベルを複数組み合わせて幾何学的構造を強調するKeTCindyコード例を教えてください。

### コード（CindyScript）

```cindy
Ketinit();
Setketcindyjs(["Label=[]","Color=offwhite"]); // default

Addax(0);
Listplot("1",[A,B,C,A]);
Listplot("2",[C,D]);
Listplot("3",[A,E]);

Letter([F,"n3w5","G"]);
Letter([A,"sw","A",B,"se","B",C,"n2","C"]);
Letter([D,"s","M",E,"ne","E",F,"n","N"]);

Windispg();
```

### 解説

このコードは、三角形ABCに補助点D, E, F, Gを導入し、それらを結ぶ線分とラベルにより幾何学的構造を強調して表現するものです。各点に方向指定付きのラベルが付与され、図形の関係性が明瞭に示されています。

### 関数(KeTCindy)

`Ketinit`, `Setketcindyjs`, `Addax`, `Listplot`, `Letter`, `Windispg`

### 関数(CindySqript)

なし

### その他

`triangle`, `auxiliary_lines`, `label`, `geometry`, `2D`, `structure`
