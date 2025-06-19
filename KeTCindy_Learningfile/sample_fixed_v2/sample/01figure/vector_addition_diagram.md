## タイトル（ベクトルの加法を示す図）

### 想定質問

KeTCindyでベクトルの加法（a + b）を図示したいです。どのように表現すればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Arrowdata("1",[A,B]);  // ベクトル a
Arrowdata("2",[A,C]);  // ベクトル b
Arrowdata("3",[A,D]);  // 合成ベクトル a + b

Listplot("1",[C,D,B],["da"]);  // 補助線（平行四辺形）

Expr([(A+B)/2,"se","\\vec{a}",(A+C)/2,"nw","\\vec{b}"]);
Expr([(A+D)/2,"se","\\vec{a}+\\vec{b}"]);

Windispg();
````

---

### 解説とラベル

このコードは、ベクトルの加法を視覚的に示すためのものです。

* `Arrowdata`：ベクトルの描画。始点と終点を指定
* `Expr`：ベクトルラベルを任意の位置にTeX形式で表示
* `Listplot("1",[C,D,B],["da"])`：補助的に平行四辺形を描画し、ベクトルの加法の幾何的意味を補完

ベクトルの始点を共通にした場合や、平行四辺形法則での説明に適した図になります。

**ラベル（タグ）**
`Arrowdata`, `Expr`, `Listplot`, `vector`, `addition`, `parallelogram`, `2D`, `geometry`, `visualization`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
