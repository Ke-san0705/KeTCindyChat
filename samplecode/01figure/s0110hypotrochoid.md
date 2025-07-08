### 想定質問

円の内側を転がる点が描くハイポトロコイド曲線をKeTCindyで描画するにはどうすればよいですか？

### コード（CindyScript）

```cindy
Ketinit();

rad=5;
Putpoint("C",[0,0]);
Putpoint("B",C+[rad-1,0]);
Putpoint("A",B+[1,0],A.xy);

Circledatac("0",[C,C+[rad,0]]);
Circledata("1",[B,B+[1,0]],["nodisp"]);
Pointdata("1",[A]);
Addgraph("0",["pt1","cr1"],[],[["Size=3","Color=red"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  tmp=rad*[cos(t),sin(t)];
  nst=text(#);
  Rotatedataadd(nst+"r","ad0",-rad*t,[B,"nodisp"]);
  Translatedataadd(nst+"t","ad"+nst+"r",tmp-[rad,0],["nodisp"]);
  Rotatedataadd(nst,"ad"+nst+"t",t,[tmp]);
);

Windispg();
```

### 解説

このコードは、固定円の内側を滑らずに転がる小円の外周上の点が描くハイポトロコイド曲線をシミュレートしています。回転と並進の組合せで、各時点における点の位置を描写しています。

### 関数(KeTCindy)

`Ketinit`, `Putpoint`, `Circledatac`, `Circledata`, `Pointdata`, `Addgraph`, `Rotatedataadd`, `Translatedataadd`, `Windispg`

### 関数(CindySqript)

`forall`

### その他

`hypotrochoid`, `curve`, `rolling_circle`, `parametric_curve`, `2D`, `geometry`, `visualization`, `animation_like`
