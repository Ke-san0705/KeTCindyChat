## タイトル（2つの関数グラフの交点間を斜線で塗り分ける）

### 想定質問

KeTCindyで \( \sin x \) と \( \cos x \) の交差部分を斜線で塗りつぶすにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");

Setax([7,"se"]);

Plotdata("1","sin(x)","x");
Plotdata("2","cos(x)","x");

tmp1=Intersectcurves("gr1","gr2");
printLn(tmp1);
pt1=tmp1_2;
pt2=tmp1_3;

Ch=[1];

if(contains(Ch,1),
  Partcrv("1",pt1,pt2,"gr1");
  Partcrv("2",pt1,pt2,"gr2");
  Joincrvs("1",["part1","part2"],["nodisp"]);
  Hatchdata("1",["j1"],["File=y"]);
);

if(contains(Ch,2),
  Enclosing("1",["gr2","Invert(gr1)"],[pt1,"nodisp"]);
  Hatchdata("1",["en1"],["File=y"]);
);

if(contains(Ch,3),
  Setparent(Cdyname()+"figs");
  Enclosing("1",["gr2","Invert(gr1)"],[pt1,"nodisp"]);
  Shade("1",["en1"],["Color=[0,0.3,0.4]"]);
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、2つの関数（ここでは $\sin x$ と $\cos x$）の交点間の領域を検出し、ハッチングまたは塗りつぶしで視覚的に強調する例です。

* `Intersectcurves`：交点を検出し、その座標を `pt1`, `pt2` に保存
* `Partcrv`：指定関数の一部分を抽出
* `Joincrvs`：2つの部分曲線を結合し、閉じた領域を形成
* `Hatchdata`：閉じた領域に斜線（ハッチ）を適用
* `Enclosing` + `Shade`：より高度な領域指定とカラー塗りつぶしも可能

複数手法が選択可能な構成になっており、視覚化用途に応じて柔軟に応用できます。

**ラベル（タグ）**
`Plotdata`, `Intersectcurves`, `Partcrv`, `Joincrvs`, `Enclosing`, `Hatchdata`, `Shade`, `sin`, `cos`, `intersection`, `region_fill`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
