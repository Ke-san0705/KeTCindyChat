## タイトル（エピトロコイド曲線の生成）

### 想定質問

KeTCindyでエピトロコイド曲線を描くにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Putpoint("A",[0,0],A.xy);
Putpoint("C",[0,1]);

r=3;

// 円の中心と接点を定義
Putpoint("C",[0,0]);
Putpoint("B",[C+[r+1,0]]);
Putpoint("A",B+[1,0],A.xy);

Circledata("O",[C,r]);          // 大きな円
Circledata("1",[B,1],["nodisp"]);  // 回転する小円
Pointdata("1",[A],["nodisp"]);
Addgraph("O",["pt1","cr1"],[""], [["Size=5","Color=red"],["dr,0.5"]]);

nn=36;
forall(1..nn,
  t=2*pi/nn*#;
  tmp=r*#(cos(t),sin(t));  // 小円中心の軌道
  nst=text(#);
  Rotatedataadd(nst+"r","ad0",radx+t,[B,"nodisp"]);
  Translatedataadd(nst+"t","ad"+nst+"r",tmp-[rad,0],["nodisp"]);
  Rotatedataadd(nst,"ad"+nst+"t",t,[tmp]);
);

Windispg();
````

---

### 解説とラベル

このコードは、\*\*エピトロコイド曲線（外円に内接する小円上の点の軌跡）\*\*を構築します。

* `Circledata("O",[C,r])`：固定された大円を定義します。
* `Rotatedataadd`, `Translatedataadd`：回転と並進により、小円の軌道と追跡点を生成
* `Addgraph`：点Aの軌跡を可視化
* `forall`ループ：時間的ステップでサンプル点を多数配置

この処理により、歯車運動や幾何学的アートとして知られるエピトロコイドが描画されます。

**ラベル（タグ）**
`Circledata`, `Putpoint`, `Rotatedataadd`, `Translatedataadd`, `epitrochoid`, `curve`, `parametric`, `2D`, `geometry`, `motion`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
