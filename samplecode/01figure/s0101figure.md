### 想定質問

三点A, B, Cを通る円と、それらを結んだ三角形ABCを描くKeTCindyのコード例を教えてください。

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Addax(0);
Listplot("1",[A,B,C,A],[]);
Circledata("1",[A,B,C]);
Letter([A,"sw","A",B,"se","B",C,"n2","C"]);

Windispg();
```

### 解説

このコードは、三角形ABCと、それを通る外接円を描画する例です。各点にはラベルが付けられ、座標軸も表示されています。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Listplot`, `Circledata`, `Letter`, `Windispg`

### 関数(CindySqript)

なし

### その他

`triangle`, `circle`, `geometry`, `2D`, `label`
