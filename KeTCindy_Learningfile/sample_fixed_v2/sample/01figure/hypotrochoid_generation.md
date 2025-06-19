## タイトル（ハイポトロコイド曲線の生成）

### 想定質問

KeTCindyで内接円を使ってハイポトロコイド（内トロコイド）曲線を描くにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

rad=5;
Putpoint("C",[0,0]);
Putpoint("B",C+[rad-1,0]);
Putpoint("A",B+[1,0],A.xy);

Circledata("O",[C,C+[rad,0]]);
Circledata("1",[B,B+[1,0]],["nodisp"]);
Pointdata("1",[A]);
Addgraph("O",["pt1","cr1"],[],[["Size=3","Color=red"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  tmp=rad*(cos(t),sin(t));
  nst=text(#);
  Rotatedataadd(nst+"r","ad0",-rad*t,[B,"nodisp"]);
  Translatedataadd(nst+"t","ad"+nst+"r",tmp-[rad,0],["nodisp"]);
  Rotatedataadd(nst,"ad"+nst+"t",t,[tmp]);
);

Windispg();
````

---

### 解説とラベル

このコードは、円の内接運動によって生まれる**ハイポトロコイド曲線**を描画するものです。

* `Circledata("O",[C,C+[rad,0]])`：外側の固定円（半径 = `rad`）を設定
* `B` は小円の基準点であり、`A` はその上の軌跡点
* `Rotatedataadd` と `Translatedataadd` の組み合わせで回転と並進の合成を行い、点Aの軌跡を生成
* `Addgraph` を用いて、軌跡を赤い点列で可視化

これにより、スパイログラフのような内円運動から生成される美しい曲線を再現できます。

**ラベル（タグ）**
`Circledata`, `Putpoint`, `Rotatedataadd`, `Translatedataadd`, `hypotrochoid`, `curve`, `rolling`, `2D`, `geometry`, `motion`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
