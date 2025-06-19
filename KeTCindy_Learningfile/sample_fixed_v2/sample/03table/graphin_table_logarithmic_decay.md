## タイトル（表の中にグラフを挿入し対数減衰の構造を視覚化）

### 想定質問

KeTCindyで、表の一部にグラフを埋め込みたいです。また、対数減衰に関連した式や記号、定数 \( e \) や \( \sqrt{e} \) などを含めて表現したいです。

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Ch=[2];

if(contains(Ch,1),
  Setfiles("graph");
  Setwindow([-0.5,7.5],[0,2.4]);
  Plotdata("1","10*log(10/x)","x=[0,XMAX]",["Exe=0","Num=100"]);
);

if(contains(Ch,2),
  xLst=[15,15,15,15,15,15,15];
  yLst=[10,10,10,10,40];
  rmvL=["r1c1r2","c3r4r5","c4r5","c5r4r5","c6r4r5"];
  Tabledata(xLst,yLst,rmvL);

  Tlistplot(["r1","c1r0r4"]);
  Tlistplot(["c2r1","c2r2r5"]);
  Tlistplot(["c1r2","c1r3"]);
  Tlistplot(["r3","c2r3r4"]);
  Tlistplot(["c3r2","c3r3"]);
  Tlistplot(["c4r2","c4r3"]);
  Tlistplot(["c5r2","c5r3"]);
  Tlistplot(["c6r2","c6r3"]);

  Putrowexpr(1,"c",["x","0","%cdots","%sqrt{e}","%cdots"]);
  Putrowexpr(2,"c",["y","","+","0","=",""]);
  Putrowexpr(3,"c",["y","","-",""]);
  Putrowexpr(4,"c",["y","=","%nearrow","%dfrac{10}{e}","%searrow","%dfrac{15}{e^{\sqrt{e}}}","%searrow"]);
  Putcell("c0r4","r5r5","0","\\input{graph}");
);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、KeTCindyで次のような複合的な構成を可能にします：

* `Plotdata`：10倍対数の減衰グラフを生成（例：$y = 10 \log(10/x)$）
* `Tabledata`：表の構造を構成。複数の `rmvL` 指定で一部のセルを消去
* `Putrowexpr`：指数関数・記号・分数を含む表記を1行に自動配置
* `\input{graph}`：表の下部セルにグラフを挿入（TikZ的構成に適用）

この構成は、関数と表を同時に視覚的に表したい教材に非常に有効です。

**ラベル（タグ）**
`Tabledata`, `Plotdata`, `Putrowexpr`, `Putcell`, `input_graph`, `log_decay`, `math_table`, `e`, `sqrt`, `2D`, `geometry`, `plot_in_table`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
