## タイトル（サイクロイド曲線の生成と描画）

### 想定質問

KeTCindyでサイクロイド曲線を生成するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Putpoint("A",[0,0],A.xy);
Putpoint("C",[0,1]);

Circledata("1",[C,C+[1,0]],["nodisp"]);
Pointdata("1",[A],["nodisp"]);
Addgraph("0",["pt1","cr1"],["nodisp"],[["Color=red","Size=3"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  Rotatedataadd(text(#)+"r","ad0", -t,[ "nodisp", C,""]);
  Translatedataadd(text(#)+"t","ad"+text(#)+"r",[t,0],[]);
);

Windispg();
```

### 解説とラベル

このコードは、円の回転によって生成される**サイクロイド曲線**を描く一連の処理です。

* `Putpoint`：基準点Aと円の接点Cを設定
* `Circledata`：回転する円のベース
* `Addgraph`：接点を赤点で示し、円周上の点追跡を準備
* `forall(1..nn)`：`nn`等分して、円を回転・平行移動
* `Rotatedataadd`, `Translatedataadd`：円の回転とx方向への平行移動を繰り返すことで、円の転がり運動を模倣

これにより、点Cの軌跡として美しいサイクロイドカーブが得られます。

### ラベル
`Circledata`, `Putpoint`, `Addgraph`, `Rotatedataadd`, `Translatedataadd`, `cycloid`, `curve`, `animation`, `2D`, `geometry`, `rolling_motion`


