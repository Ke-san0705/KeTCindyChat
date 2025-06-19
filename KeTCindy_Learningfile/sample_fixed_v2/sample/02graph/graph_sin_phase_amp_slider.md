## タイトル（sin関数の位相と振幅をスライダーで制御）

### 想定質問

KeTCindyで sin関数のグラフをスライダーで位相と振幅を調整するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Setparent(Cdyname()+"fig");
Setketcindyjs(["Nolabel=all","Color=white"]);

Setax([7,"se"]);

Slider("C",[-6,-3],[6,-3]);     // 位相調整スライダー
Slider("F",[-8,-3],[8,-3]);     // 振幅調整スライダー

Putpoint("G",[0,2]);            // 説明ラベル用のポイント
O.xy=[0,2];

Ch=[1,2]; // block(s) to be executed

if(contains(Ch,1),
  Plotdata("1","sin(x)","x",["Num=200","do"]);
);

if(contains(Ch,2),
  Plotdata("2","sin(x-C.x)+F.y","x",["Num=200"]);
);

Letter([G,"s","Graph of $y=\\sin x$"]);

Windispg();
````

---

### 解説とラベル

このコードは、基本の $y = \sin x$ に対して以下の操作をスライダーで動的に行う実例です：

* `Slider("C",...)`：グラフの**位相**（左右移動）を制御
* `Slider("F",...)`：グラフの**振幅**（上下伸縮）を制御
* `sin(x-C.x) + F.y`：C.xでシフト、F.yで高さを調整
* `Plotdata` によりリアルタイムで再描画され、変化を可視化可能

関数の構造理解を深めるインタラクティブな教材として適しています。

**ラベル（タグ）**
`Slider`, `Plotdata`, `Setax`, `Letter`, `sin`, `amplitude`, `phase_shift`, `interactive`, `function_plot`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
