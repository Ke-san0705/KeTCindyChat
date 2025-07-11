### 想定質問

エピトロコイド（円の外側を転がる点が描く曲線）をKeTCindyで描画するにはどうすればよいですか？

### コード（CindyScript）

```cindy
Ketinit();
Addax(0);

Putpoint("A",[0,0],A.xy);
Putpoint("C",[0,1]);

rad=3;
Putpoint("C0",[0,0]);
Putpoint("B",C+[rad+1,0]);
Putpoint("A",B+[1,0],A.xy);

Circledatac("0",[C,rad]);
Circledata("1",[B,1],["nodisp"]);
Pointdata("1",[A],["nodisp"]);
Addgraph("0",["pt1","cr1"],[],[["Size=5","Color=red"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  tmp=rad*[cos(t),sin(t)];
  nst=text(#);
  Rotatedataadd(nst+"r","ad0",rad*t,[B,"nodisp"]);
  Translatedataadd(nst+"t","ad"+nst+"r",tmp-[rad,0],["nodisp"]);
  Rotatedataadd(nst,"ad"+nst+"t",t,[tmp]);
);

Windispg();
```

### 解説

このコードは、固定円の外側を小円が滑らずに回転するとき、その円周上の点が描く軌跡（エピトロコイド）を可視化しています。回転と平行移動を逐次的に組み合わせて、各ステップの状態を描画しています。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Putpoint`, `Circledatac`, `Circledata`, `Pointdata`, `Addgraph`, `Rotatedataadd`, `Translatedataadd`, `Windispg`

### 関数(CindySqript)

`forall`

### その他

`epitrochoid`, `curve`, `rolling_circle`, `parametric_curve`, `2D`, `animation_like`, `geometry`
