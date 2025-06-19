````markdown
## ファイル名: second_order_diff_eq_slider.md

## タイトル（2階線形微分方程式のスライダー制御と可視化）

### 想定質問

KeTCindyで \( \frac{d^2y}{dx^2} + a \frac{dy}{dx} + by = 0 \) のような2階線形微分方程式の係数をスライダーで操作しながら解の形を確認するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["Nolabel=all","Color=white"]);

Slider("C",[0,YMAX],[0,YMIN]);
Slider("G",[0,YMIN-1],[XMAX,YMIN-1]);
Slider("L",[0,YMIN-2],[XMAX,YMIN-2]);

// 解のグラフ描画
// Deqplot("1","y=y","x",0,1);
Deqplot("2","y''=-L.x*y'-G.x*y","x=[0,XMAX]",0,[C.y,0],["Num=200"]);
// 初期値ベクトルの可視化
// Deqplot("3","[x,y]=[x*(1-y),0.3*y*(x-1)]","t=[0,20]",0,A,["Num=200"]);

// 数式の表示
Expr(M,"e","\\displaystyle\\frac{d^2 y}{dx^2}+"+L.x+"\\frac{dy}{dx}+"+G.x+"y=0");

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、2階線形常微分方程式

$$
\frac{d^2y}{dx^2} + a \frac{dy}{dx} + b y = 0
$$

の解曲線をスライダーでパラメータ $a$, $b$ を変更しながら可視化するものです。

* `Slider("L",...)`：係数 $a$ を制御（1階微分項の係数）
* `Slider("G",...)`：係数 $b$ を制御（定数項の係数）
* `Deqplot("2",...)`：数値的に解を描画
* `Expr(...)`：現在の係数値に基づいた方程式を数式表示

減衰振動・振動解・発散の様子を視覚的に観察でき、教育用や解析の初学に適したモデルです。

**ラベル（タグ）**
`Slider`, `Deqplot`, `Expr`, `differential_equation`, `second_order`, `visualization`, `interactive`, `2D`, `graph`, `math_education`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
