## タイトル（2つの表を並列に描画し、値の比較やスタイル調整を行う）

### 想定質問

KeTCindyで、2つの表を横に並べて描きたいです。また、一部の枠線だけを表示・非表示にして、比較しやすくしたいのですが、どうすれば良いですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

Putpoint("C",[4,0],[C.x,0]);  // 右側表の基準点

xLst=[10,10,10];
yLst=[10,10];

Tabledatalight(xLst,yLst,[],["Setwindow=sn"]);
Putrowexpr(1,"c",["x","20","30"]);
Putrowexpr(2,"c",["y","60","40"]);

Tabledatalight(xLst,yLst,[],["Move=C.xy"]);
Putrowexpr(1,"c",["x","30","20"]);
Putrowexpr(2,"c",["y","60","50"]);

Changetablestyle(["r1c0c3","r2c0c3"],["da"]);  // 枠線非表示設定

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードでは、KeTCindyで以下の構成を実現しています：

* `Tabledatalight(...)`：余計な外枠のないテーブルを描画
* `Putrowexpr(...)`：行ごとにテキストや数値を配置
* `Putpoint("C",...)`：第2表の位置基準点を明示的に設定
* `Changetablestyle(...,["da"])`：r1〜r2行・c0〜c3列の枠線を非表示に

このようにして、**2つの表の数値比較やスタイルの比較**が可能になります。

**ラベル（タグ）**
`Tabledatalight`, `Putrowexpr`, `Putpoint`, `Changetablestyle`, `multiple_tables`, `side_by_side`, `table_comparison`, `styling`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
