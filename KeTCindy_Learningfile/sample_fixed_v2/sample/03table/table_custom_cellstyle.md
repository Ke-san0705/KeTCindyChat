## タイトル（セルのスタイル変更と文字列挿入を含む表の作成）

### 想定質問

KeTCindyで特定のセルの境界線やスタイルをカスタマイズした表を作成するにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

xLst=[16,16,16,16,16,16];
yLst=[10,10];
rmvL=["c1r2","c2r1r2","c3r1r2","c4r1r2","c5r1r2"];

Tabledata(xLst,yLst,rmvL);

// セルへの文字列挿入
Putcell("<c0r0","c6r1","lt","Ans");
Putcell("<c0r0","c6r1","rb2","cm");

// 特定セルの罫線スタイル変更（点線で表示）
ChangeTablestyle(["r1c0c6"],["da"]);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、以下のような目的で表をカスタム描画する方法を示しています：

* `Tabledata(xLst,yLst,rmvL)`：セルサイズと非表示マスを設定
* `Putcell(...,"lt",...)`：左上揃えで文字列「Ans」を挿入
* `Putcell(...,"rb2",...)`：右下揃えで文字列「cm」を挿入
* `ChangeTablestyle(...)`：特定のセルの罫線（ここでは破線 `"da"`）に変更

これにより、表内のレイアウトや強調、罫線構成が柔軟に制御できます。

**ラベル（タグ）**
`Tabledata`, `Putcell`, `ChangeTablestyle`, `table`, `grid`, `labeling`, `style`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
