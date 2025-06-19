## タイトル（入れ子構造を用いた表と一部セルの結合・非表示処理）

### 想定質問

KeTCindyで、表の中に別の表を埋め込むような入れ子構造を作りたいです。また、特定のセルを結合したり、枠線を消す方法はありますか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

xLst=[10,10,10];
yLst=[10,10,10];

Tabledatalight(xLst,yLst,[]);  // 外枠表
Putrowexpr(0,"c",["A","B","C"]);
Putrowexpr(1,"c",["D","X","F"]);
Putrowexpr(2,"c",["G","H","I"]);

tmp=[5,5];  // 内側テーブルのセルサイズ
Tabledatalight(tmp,tmp,[],["Move="+text(tmp),"Setwindow=1"]);
Putrowexpr(0,"c",["x","y"]);
Putrowexpr(1,"c",["z","w"]);

Changetablestyle(["c0r0r2","c2r0r2","r0c0c2"],["nodisp"]);  // 外枠削除
````

---

### 解説とラベル

このコードは、KeTCindyで\*\*入れ子構造の表（Nested Tables）\*\*を作成するための構成例です。

* `Tabledatalight(...)` を2回使用して、外側と内側の表を作成
* `Putrowexpr(...)` でそれぞれのセル内容を行ごとに配置
* `["Move="+text(tmp)]` によって内側テーブルの表示位置を調整
* `Changetablestyle(...)` で外側表の一部セル枠を非表示に（結合風の見た目に）

このような表は、**変数の階層構造や局所的な対比**に便利です。

**ラベル（タグ）**
`Tabledatalight`, `Putrowexpr`, `Changetablestyle`, `nested_table`, `merged_cells`, `multi_layer`, `table_structure`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
