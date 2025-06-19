## タイトル（スライダーによるsin関数の位相移動）

### 想定質問

KeTCindyで sin関数のグラフにスライダーをつけて、位相（横のずれ）を操作するにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");
Setketcindyjs(["Nolabel=all","Color=offwhite"]);
Ketcindyjsmain("<pf1o/fp>..Graph of $y=\\sin x$",[]);

Setax([7,"se"]);
Slider("C",[-6,-3],[6,-3]);

Ch=[1,2];  // 実行するブロックを指定

if(contains(Ch,1),
  Plotdata("1","sin(x)","x",["Num=200","do"]);
);

if(contains(Ch,2),
  Plotdata("2","sin(x-C.x)","x",["Num=200"]);
);

Putpoint("D",[1,2],D.xy);
Letter([D,"s","Graph of $y=\\sin x$"]);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードでは、sin関数の基本グラフに加え、スライダー操作で位相（グラフの左右シフト）を変更できる機能を追加しています。

* `Slider("C", [...])`：点Cが左右に動くスライダーとして振る舞う
* `sin(x - C.x)`：Cのx座標に応じて位相が変化
* `Ch=[1,2]`：表示制御用のフラグ（固定グラフと可変グラフ両方を描画）

この仕組みは、位相シフトの視覚化や関数変化の学習教材として有効です。

**ラベル（タグ）**
`Plotdata`, `Slider`, `Setax`, `Ketcindyjsmain`, `sin`, `graph`, `phase_shift`, `interactive`, `function_plot`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
