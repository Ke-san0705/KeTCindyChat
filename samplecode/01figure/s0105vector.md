### 想定質問

ベクトルの加法を視覚的に示すには、KeTCindyでどのようなコードを書けばよいですか？

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Arrowdata("1",[A,B]);
Arrowdata("2",[A,C]);
Arrowdata("3",[A,D]);
Listplot("1",[C,D,B],["da"]);

Expr([(A+B)/2,"se","#vec{a}",(A+C)/2,"nw","#vec{b}"]);
Expr([(A+D)/2,"se","#vec{a}+#vec{b}"]);

Windispg();
```

### 解説

このコードは、点Aを始点とした2つのベクトルAB, ACと、それらの和であるADを描画し、ベクトルの加法の関係を図示しています。補助線や数式表記によって、ベクトルの合成過程を視覚的に把握できます。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Arrowdata`, `Listplot`, `Expr`, `Windispg`

### 関数(CindySqript)

なし

### その他

`vector`, `addition`, `geometry`, `2D`, `visualization`, `label`, `expression`
