## タイトル（二重線と位置調整を含む表構成のカスタマイズ）

### 想定質問

KeTCindyで表の一部に二重線を引いたり、行列の線や構造を細かく位置調整したいのですが、どうすれば可能ですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

xLst=[16,16,16,16,16,16];
yLst=[10,10];
rmvL=["c1r2","c2r1r2","c3r1r2","c4r1r2","c5r1r2"];

Tabledata(xLst,yLst,rmvL);

// 二重線を模した線の調整と描画
Translatedata("1","tblr1c0c6",[0,0.1]);  // 基本線を少し上に
Changetablestyle("c2r0r1",["nodisp"]);  // 中央の線を消す
Translatedata("2a","tblc2r0r1",[0.05,0]);  // 右側線をずらす
Translatedata("2b","tblc2r0r1",[-0.05,0]); // 左側線をずらす
````

---

### 解説とラベル

このコードは、KeTCindyで表構成をより詳細にカスタマイズするための方法を示しています。

* `rmvL`：削除するセルを指定してレイアウト調整
* `Translatedata(...)`：任意の罫線を座標単位でずらすことで「二重線」や「強調線」を表現
* `Changetablestyle(...,["nodisp"])`：一部の線を非表示にして、重ねて表示される線の効果を演出

視覚的なアクセントや意味づけとして、表の特定部位を強調するのに非常に有効です。

**ラベル（タグ）**
`Tabledata`, `Translatedata`, `Changetablestyle`, `table`, `grid`, `doubleline`, `adjustment`, `layout`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
