## タイトル（暗黙的曲線領域の塗りつぶしと平行移動）

### 想定質問

KeTCindyで暗黙的に定義された曲線の領域に斜線（ハッチ）を付けて、さらにそれを任意の点に移動するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setketcindyjs(["Nolabel=all"]);

fun="x^2+2*x*y+2*y^2=1";
Ch=[3];

if(contains(Ch,1),
  Implicitplot("1",fun,"x=[-3,3]","y=[-3,3]");
  Hatchdata("1",["i1"],["imp1"]);
);

if(contains(Ch,3),
  Putpoint("A",[0,0],A.xy);

  Implicitplot("0",fun,"x=[-3,3]","y=[-3,3]");  // for Ketjs off
  Hatchdata("0",["i1"],["imp0"]);

  Ketcindyjsdata(["imp0",imp0,"hao",hao]);     // no ketjs off

  // translated hatch
  Translatedata("1",["imp0","hao"],A.xy);
);

Windispg();
````

---

### 解説とラベル

このコードでは、暗黙的な方程式で定義される曲線領域を以下のように処理しています：

* `Implicitplot`：例として、楕円型の関係式 $x^2 + 2xy + 2y^2 = 1$ の領域を描画
* `Hatchdata`：その内部領域に斜線（ハッチ）を適用
* `Putpoint("A",...)`：平行移動の目的地を指定
* `Translatedata`：元の図形とそのハッチを、点Aへと移動

また、`Ketcindyjsdata` によりKeTCindyJS用データを手動でセット可能。

**ラベル（タグ）**
`Implicitplot`, `Hatchdata`, `Translatedata`, `Putpoint`, `Ketcindyjsdata`, `implicit_curve`, `region_fill`, `translation`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
