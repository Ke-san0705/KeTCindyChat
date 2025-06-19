
## タイトル（sin関数への接線の描画）

### 想定質問

KeTCindyで \( y = \sin x \) に対する任意点での接線を引くにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");
Setketcindyjs(["Nolabel=all","Color=white"]);
Setax([7,"se"]);

Plotdata("1","sin(x)","x",["Num=200"]);
Putoncurve("A","gr1");

coeff=Derivative("sin(x)",x,A.x);
funstr=Assign("coeff*(x-A.x)+A.y",["coeff",coeff]);
Plotdata("2",funstr,"x",["Color=red","Num=1"]);

Pointdata("1",A,["Size=3"]);

Putpoint("B",[3,0.5],B.xy);
Putpoint("C",[-6,2],C.xy);
Letter([A,"n2","A"]);
Expr([B,"e","y=\\sin x"]);
Letter([C,"e","\\Large The graph of $y=\\sin x$"]);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、関数 \$y = \sin x\$ における任意の点Aにおいて接線を描く処理です。

* `Putoncurve("A","gr1")`：点Aを関数グラフ上に置く
* `Derivative(...)`：A.x における接線の傾きを計算
* `Assign(...)`：傾きとAの座標から接線の関数式を生成
* `Plotdata("2",...)`：接線を赤色で1本だけ描画

さらに、ラベルや注釈も追加されており、グラフ全体の理解がしやすくなっています。

---

### ラベル（タグ）

`Plotdata`, `Derivative`, `Putoncurve`, `Expr`, `tangent`, `sin`, `function`, `geometry`, `2D`, `graph`, `calculus`

```

