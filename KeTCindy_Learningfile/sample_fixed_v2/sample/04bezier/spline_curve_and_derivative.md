## タイトル（スプライン曲線とその導関数の可視化）

### 想定質問

KeTCindyでスプライン補間曲線を描き、その導関数を表示したいです。どうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");

Qspline("1",[A,B,C,D]);  // スプライン補間曲線
Putoncurve("P","bz01");  // 曲線上に点Pを置く
Derivative("bz01","*P.x");  // bz01の導関数を定義

Lineplot("1",[P,[1,1]],[]);  // P点から導関数の接線（方向）を描く

Plotdata("1","*m*x^n","x",[Num=1]);  // 近似式の描画
//Plotdata("1","fun","x",[Num=1]);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、**点列からスプライン補間曲線を作成し、さらにその導関数を視覚化**する例です。

* `Qspline(...)`：与えられた点列を滑らかにつなぐスプライン曲線を生成（ベジェ曲線ベース）
* `Putoncurve(...)`：指定した曲線上に動点Pを配置し、微分可能な対象にする
* `Derivative(...)`：曲線に沿って変化する点Pの導関数（接線方向）を取得
* `Lineplot(...)`：導関数方向ベクトルを補助的に可視化
* `Plotdata(...)`：導関数や補間式のプロット

**ラベル（タグ）**
`Qspline`, `Putoncurve`, `Derivative`, `Lineplot`, `Plotdata`, `curve`, `spline`, `tangent`, `2D`, `visualization`, `differentiation`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
