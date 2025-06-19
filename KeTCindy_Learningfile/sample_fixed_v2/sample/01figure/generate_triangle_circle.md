
## タイトル（三点を通る円と三角形の描画）

### 想定質問

三点を通る円を描くKeTCindyのコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Addax(0);  // 座標軸の表示
Listplot("1",[A,B,C,A],[]);  // 三角形ABC
Circledata("1",[A,B,C]);    // ABCを通る円
Letter([A,"sw","A"],B,"se","B",C,"n2","C");

Windispg();
````

---

### 解説とラベル

このコードは、KeTCindyを使って特定の幾何・グラフを描画するものです。

---

### ラベル

`Addax`, `Listplot`, `Circledata`, `Letter`, `triangle`, `circle`, `geometry`, `2D`

```


