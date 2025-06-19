## タイトル（制御点からベジェ曲線を描く基本例）

### 想定質問

KeTCindyでベジェ曲線を描くにはどうすればいいですか？制御点やその軌跡も表示したいです。

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");

Bezier("1",[A,B,C,D],[E,F,G,H,K,L]);

Mkbezierptcrv([M,N,O,P]);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、**KeTCindyでベジェ曲線（Bezier曲線）を制御点から描く**ための最小構成例です。

* `Bezier(...)`：第1引数がID、第2引数が制御点（曲線を決める）、第3引数が補助点（表示）
* `Mkbezierptcrv(...)`：ベジェ曲線の構成点を `ap1`, `ap2`, `ap3` のように補助的に描画

**この構成の応用で、スプラインや補間曲線の可視化**にも展開できます。

**ラベル（タグ）**
`Bezier`, `Mkbezierptcrv`, `control_points`, `curve`, `geometry`, `2D`, `visualization`, `bezier`, `construction`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
