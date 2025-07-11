### 想定質問

ベジエ曲線（Bezier curve）をKeTCindyで描く基本コードを教えて

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");

Bezier("1",[A,B,C,D],[E,F,G,H,K,L]);

Mkbezierpctrv([M,N,O,P]);

//Figpdf();
Windispg();
```

---

### 解説

このコードは、KeTCindyでベジエ曲線を描く基本構文を示しています。
上側に4点制御のベジエ曲線（赤）、下側にベジエ曲線の構成点表示（緑）が見られます。

* `Bezier("1",[A,B,C,D],[E,F,G,H,K,L]);`
  → 2つの制御点系列（4点）によりベジエ曲線を描画します。
* `Mkbezierpctrv([M,N,O,P]);`
  → 点 M, N, O, P を使ってベジエ曲線の作図過程（分点列 `ap1`, `ap2`, `ap3`など）を視覚化。

---

### ラベル（関数KeTCindy）

`Ketinit`, `Bezier`, `Mkbezierpctrv`, `Windispg`

---

### ラベル（関数CindyScript）



---

### ラベル（その他）

`bezier`, `curve`, `geometry`, `construction`, `分割点列`, `補間`, `2D`
