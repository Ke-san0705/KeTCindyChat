## タイトル（aⁿ型指数関数とその接線の可視化）

### 想定質問

KeTCindyで \( y = a^x \) 型の指数関数を描いて、その点における接線を表示するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["Nolabel=all","Color=white"]);

Slider("C",[-1,5.5],[5,5.5]);

funstr=Assign("a^x",["a",Sprintf(C.x,3)]);
Plotdata("1",funstr,"x=[-5,5]");

Putpoint("D",[0,1]);

coeff=Derivative(funstr,"x",D.x);
Lineplot("1",[D,[D.x+1,D.y+coeff]]);
Lineplot("2",[D,[D.x+1,D.y+1]],["da"]);

Expr([F,"w","y=x+1",E,"e","y="+funstr]);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、一般的な指数関数 $y = a^x$ を描き、点 $D(0,1)$ における接線と比較線 $y = x + 1$ を表示します。

* `Slider("C",...)`：底 $a$ を動かすスライダーで指数関数の形を変化
* `Assign` と `Sprintf`：関数式にスライダーの値を反映し文字列で代入
* `Derivative(...)`：点Dにおける接線の傾きを取得
* `Lineplot`：実際の接線と比較線を描画
* `Expr`：式を図上に表記

これにより、さまざまな指数関数の形とその微分の視覚的理解が可能になります。

**ラベル（タグ）**
`Slider`, `Plotdata`, `Lineplot`, `Derivative`, `Assign`, `Expr`, `exponential_function`, `differentiation`, `tangent`, `interactive`, `2D`, `graph`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
