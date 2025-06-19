## タイトル（三角形と円のPDF出力用図の作成）

### 想定質問

KeTCindyで三点を通る円と三角形を描いて、PDF出力用の図を作りたいのですが、どうすれば良いですか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"p");

Addax(0);  // 座標軸の表示
Listplot("1",[A,B,C,A],[]);  // 三角形の描画
Circledata("2",[A,B,C]);     // ABCを通る円の描画
Letter([A,"sw","A"],B,"se","B",C,"n2","C");  // 頂点ラベル

Figpdf();  // PDF出力用の設定
Windispg();
````

---

### 解説とラベル

このコードは、三点 A・B・C を通る円と三角形 ABC を描き、PDFとして正しいサイズで出力できるように設定したものです。

* `Setparent(Cdyname()+"p")`：PDFサイズの親ファイルを指定（ボタン「Parent」を押して設定）
* `Figpdf()`：PDF用描画の開始。`Windispg()`の前に置くことで正確なサイズでのPDF生成を可能にします
* `Circledata`, `Listplot`：それぞれ円と三角形の描画
* `Letter`：各点のラベル表示（位置も指定）

**ラベル（タグ）**
`Setparent`, `Figpdf`, `Addax`, `Listplot`, `Circledata`, `Letter`, `PDF_output`, `geometry`, `triangle`, `circle`, `2D`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
