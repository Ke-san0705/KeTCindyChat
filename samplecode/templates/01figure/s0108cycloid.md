### 想定質問

円が直線上を転がるときに描くサイクロイド曲線をKeTCindyで描画するにはどうすればよいですか？

### コード（CindyScript）

```cindy
Ketinit();

Putpoint("A",[0,0],A.xy);
Putpoint("C",[0,1]);

Circledata("1",[C,C+[1,0]],["nodisp"]);
Pointdata("1",[A],["nodisp"]);

Addgraph("0",["pt1","cr1"],["nodisp"],
  [["Color=red","Size=3"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  Rotatedataadd(text(#)+"r","ad0",-t,["nodisp",C,""]);
  Translatedataadd(text(#)+"t","ad"+text(#)+"r",[t,0],[]);
);

Windispg();
```

### 解説

このコードは、円が直線上を滑らずに転がる運動の軌跡、すなわちサイクロイドをシミュレートしたものです。`Rotatedataadd`と`Translatedataadd`を用いて、接点が移動しながら円が回転する様子を段階的に再現しています。

### 関数(KeTCindy)

`Ketinit`, `Circledata`, `Pointdata`, `Addgraph`, `Rotatedataadd`, `Translatedataadd`, `Windispg`,`Putpoint`

### 関数(CindySqript)

`forall`

### その他

`cycloid`, `curve`, `rolling_circle`, `parametric_motion`, `2D`, `visualization`, `animation_like`
