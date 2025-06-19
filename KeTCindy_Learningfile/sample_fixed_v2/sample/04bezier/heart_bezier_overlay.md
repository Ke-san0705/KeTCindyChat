
## タイトル（画像上にBezier曲線でハートを描画）

### 想定質問

画像に合わせてBezier曲線を使って図形（ハート）を描くにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

// 背景画像の読み込みと表示
drawimage([0,0],"heart.png",scale->2,alpha->0.5);

// Bezier曲線の制御点を指定して描画
Mkbezierptcrv([A,B,C,D,A],["dr,2","Color=[0,0.5,0]"]);

// 塗りつぶしのオプション（必要に応じて）
if(Shader==1,
  Shade(["bza1",["Color=[0,0.5,0]"]]);
);

Windispg();
````

---

### 解説とラベル

このコードは、**画像上にBezier曲線を重ねることで輪郭をトレース**する応用例です。視覚的な補助線として透明度付きの背景画像（`heart.png`）を読み込み、その上に曲線を引くことで、図形の形を手動で調整できます。

* `drawimage(...)`：画像を背景として表示し、透明度（`alpha`）やスケールを調整可能
* `Mkbezierptcrv(...)`：複数制御点を指定し閉曲線を作成
* `Shade(...)`：条件付きで塗りつぶしを追加（図形の視認性を向上）

**活用例：**
ロゴトレース、図形模写、曲線モデリングの初学者練習などに最適です。

---

### ラベル（タグ）

`Bezier`, `drawimage`, `overlay`, `curve fitting`, `image tracing`, `Shade`, `visual aid`, `2D`, `geometry`, `closed curve`

```
