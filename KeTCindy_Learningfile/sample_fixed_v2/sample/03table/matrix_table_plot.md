## タイトル（行列表現の描画と記号入力）

### 想定質問

KeTCindyで表（マトリクス）を描画し、数式や記号を含んだ行列演算の図を作るにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

xLst=[10,10,12,10,12,10];
yLst=[10,10,10,10,10];
rmvL=[];
rmvL=["r2c1c2"];

Tabledata(xLst,yLst,rmvL);

Ch=[1,2];

if(contains(Ch,1),
  Tlistplot(["c1r1","c2r3"]);
  Tlistplot(["c1r3","c2r1"]);
);

if(contains(Ch,2),
  Putrowexpr(1,"c",["x","0","%cdots","1","%cdots","2"]);
  Putrowexpr(2,"c",["x","=","+","0","=",""]);
  Putrowexpr(3,"c",["y","=","%nearrow","","%searrow",""]);
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、行列・表形式の構造をKeTCindy上に可視的に表現する方法を示しています。

* `Tabledata(xLst,yLst,rmvL)`：各セルサイズを定義し、任意のセルを非表示（rmv）に設定
* `Tlistplot`：セルの間に線を描画する（矢印や強調線など）
* `Putrowexpr`：行に数式や記号を挿入（LaTeXスタイル記法をサポート）

記号の例：

* `%cdots`：中央のドット「⋯」
* `%nearrow`：↗
* `%searrow`：↘

このようにして、行列の演算過程や変形の可視化が可能になります。

**ラベル（タグ）**
`Tabledata`, `Putrowexpr`, `Tlistplot`, `matrix`, `grid`, `math_table`, `expression_input`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
