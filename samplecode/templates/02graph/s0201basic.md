### 想定質問

関数 $y = \sin x$ のグラフをKeTCindyで描画するにはどうすればよいですか？

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");
Setparent(Cdyname()+"fig");

Setax(["1","x","e","y","n","O","se"]);
//Setunitlen("4mm");

Plotdata("1","sin(x)","x");

//Plotdata("2","sin(5*x)","x",["Num=200"]);
//Paramplot("1",["cos(5*t),sin(6*t)"],"t=[0,2*pi]",["Num=500"]);

Putpoint("D",[0,2],D.xy);
Letter([D,"s","Graph of y=¥sin x$"]);

Figpdf();
Windispg();
```

### 解説

このコードは、関数 $y = \sin x$ のグラフを描画し、座標軸設定・関数名のラベル表示・PDF出力まで一貫して行う例です。

### 関数(KeTCindy)

`Ketinit`, `Setparent`, `Setax`, `Plotdata`, `Letter`, `Figpdf`, `Windispg`,`Putpoint`

### 関数(CindySqript)
なし

### その他

`2D`, `graph`, `function`, `label`, `pdf_output`
