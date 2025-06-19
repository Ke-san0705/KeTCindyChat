## タイトル（sin関数の基本グラフ描画）

### 想定質問

KeTCindyで \( y = \sin x \) のグラフを描くにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

Setax(["l","x","e","y","n","O","se"]);
//Setunitlen("4mm");

Plotdata("1","sin(x)","x");

Putpoint("D",[0,2],D.xy);
Letter([D,"s","Graph of $y=\\sin x$"]);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、KeTCindyで基本的な正弦関数 $y = \sin x$ を描く方法です。

* `Setparent(Cdyname()+"fig")`：PDF出力用の親ファイル指定
* `Setax([...])`：座標軸の表示設定（方向と原点の位置を含む）
* `Plotdata("1","sin(x)","x")`：関数 $y = \sin x$ を描画
* `Putpoint`, `Letter`：注釈用の点を配置し、式の説明を加える
* `Figpdf()`, `Windispg()`：描画と出力処理

シンプルな関数の視覚化に最適なテンプレートです。

**ラベル（タグ）**
`Plotdata`, `Setax`, `Letter`, `Figpdf`, `trig_function`, `sin`, `graph`, `2D`, `function_plot`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
