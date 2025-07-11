### 想定質問

CindyScriptで表（行列や記号を含む）を描画するコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");
Setparent(Cdyname()+"fig");

xLst=[[10,10,12,10,12,10]];
yLst=[[10,10,10]];
rawL=[r"r2c1o2"];

Tabledata(xLst,yLst,rmvL);

Ch=[1,2];

if(contains(Ch,1),
  Tlistplot([["o1r1","c2r3"]]);
  Tlistplot([["o1r3","c2r1"]]);
);

if(contains(Ch,2),
  Putrowexpr(1,"c",["x","O","$\cdots$","1","$\cdots$","2"]);
  Putrowexpr(2,"c",["y","","x","O","x","",""]);
  Putrowexpr(3,"c",["y","x","$\nearrow$","x","$\searrow$","",""]);
);

Figpdf();
Windispg();
//Help("Table");
```

---

### 解説

このコードは、KeTCindyを使って表（テーブル）を描画するものです。以下のような構造を持ちます：

* `Tabledata(...)` で表の構成を指定します。セルの幅や高さは `xLst`, `yLst`、削除セルは `rmvL` にて設定します。
* `Tlistplot(...)` でセルの位置に線を引く（例：斜線やセル間接続）。
* `Putrowexpr(...)` を使って各行に数式や記号などを挿入します。
* 数式には LaTeX のような `\cdots`, `\nearrow`, `\searrow` などの表現も可能です。

---

### ラベル（関数KeTCindy）

`Ketinit`, `Setparent`, `Tabledata`, `Tlistplot`, `Putrowexpr`, `Figpdf`, `Windispg`

---

### ラベル（関数CindyScript）

`contains`

---

### ラベル（その他）

`table`, `matrix`, `symbolic`, `notation`, `expression`, `2D`, `grid`, `math表記`, `記号表現`, `構造描画`
