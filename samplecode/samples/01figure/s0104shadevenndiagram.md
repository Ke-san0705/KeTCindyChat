### 想定質問

2つの円の共通部分をベン図のように塗りつぶして表現するKeTCindyコード例を教えてください。

### コード（CindyScript）

```cindy
Ketinit();
//import("enclosing.txt");

Addax(0);

Circledata("1",[A,3]);
Circledata("2",[B,3]);
Putoncurve("C","cr2");
Putoncurve("D","cr1");

Circledata("1c",[C,0.3],["nodisp"]);
Circledata("2d",[D,0.3],["nodisp"]);
Shade(["cr1c"],["Color=white"]);
Shade(["cr2d"],["Color=white"]);

Letter([C,"c","1",D,"c","2"]);

Enclosing("1",["cr2","cr1"],[[1,2],"nodisp"]);
Shade("en1",["Color=0.6*[1,1,1]"]);

Framedata();

Windispg();
```

### 解説

このコードは、2つの円の交差部分（ベン図のような図形）を描画し、共通領域を灰色で塗りつぶすものです。補助的に白塗りの円を使って輪郭部分を調整し、`Enclosing`関数と`Shade`を組み合わせることで、重なりの可視化を実現しています。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Circledata`, `Putoncurve`, `Shade`, `Letter`, `Enclosing`, `Framedata`, `Windispg`

### 関数(CindySqript)

なし

### その他

`venn`, `circle`, `intersection`, `color_fill`, `geometry`, `2D`, `shading`, `visualization`
