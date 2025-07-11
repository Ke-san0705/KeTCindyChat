### 想定質問

双曲線の外側の領域をハッチングで塗りつぶすには、KeTCindyでどのようなコードを書けばよいですか？

### コード（CindyScript）

```cindy
Ketinit();

Hyperbolaplot("1",[A,B,C],"[-2,2]");

Ch=[1];
if(contains(Ch,1),
  Hatchdata("1",["ii"],[["rt1hyp1","w"],["rt1hyp2","e"]],["Max=100"]);
);
if(contains(Ch,2),
  Hatchdata("1",["ii"],[["rt1hyp1","w"],["rt1hyp2","e"]],["Max=100"]);
);

Windispg();
```

### 解説

このコードは、点A・B・Cをもとに双曲線を描き、その外側の領域を条件に応じて斜線で塗りつぶすものです。`Hyperbolaplot`により双曲線が描画され、`Hatchdata`関数で左右対称の領域にハッチング処理が施されます。

### 関数(KeTCindy)

`Ketinit`, `Hyperbolaplot`, `Hatchdata`, `Windispg`

### 関数(CindySqript)

なし

### その他

`hyperbola`, `function`, `graph`, `hatch`, `2D`, `region_fill`, `visualization`, `conic`
