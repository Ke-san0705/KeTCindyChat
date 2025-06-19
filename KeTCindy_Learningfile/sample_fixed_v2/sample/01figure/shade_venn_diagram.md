## タイトル（ベン図の重なり部分の塗りつぶし）

### 想定質問

KeTCindyで2つの円の重なり部分だけを塗りつぶしたベン図のような図を描くにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//import("enclosing.txt");

Addax(0);

// 円のデータ
Circledata("1",[A,3]);
Circledata("2",[B,3]);

// 円弧の取得（見た目には表示しない）
Putoncurve("C","cr1");
Putoncurve("D","cr2");
Circledata("1c",[C,0.3],["nodisp"]);
Circledata("2d",[D,0.3],["nodisp"]);

// 装飾とラベル
Shade(["cr1c"],["Color=white"]);
Shade(["cr2d"],["Color=white"]);
Letter([C,"c","1","D","c","2"]);

// 重なり部分の生成と塗りつぶし
Enclosing("1",["cr2","cr1"],[[1,2],"nodisp"]);
Shade(["en1"],["Color=0.6*[1,1,1]"]);

Framedata();  // 枠線の生成
Windispg();
````

---

### 解説とラベル

このコードは、2つの円の重なり部分（ベン図の交差領域）を視覚的に強調するためのものです。

* `Putoncurve`：交点候補となる円周上の点を取得
* `Enclosing`：複数の円弧で囲まれた領域（重なり）を定義
* `Shade(["en1"])`：その囲まれた部分をグレーで塗りつぶす
* `Framedata()`：全体を囲む枠を追加して見やすく調整

交差の強調表示や領域分割教材などに応用できます。

**ラベル（タグ）**
`Circledata`, `Putoncurve`, `Enclosing`, `Shade`, `Framedata`, `venn`, `intersection`, `region`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
