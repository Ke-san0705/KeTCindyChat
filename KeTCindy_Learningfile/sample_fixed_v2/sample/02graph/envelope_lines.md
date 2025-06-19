## タイトル（複数直線によるエンベロープの可視化）

### 想定質問

KeTCindyで複数の直線を使ってエンベロープ（包絡線）を表現するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

Slider("C",[-5,-6],[5,-6]);

n=50;
forall((-n)..n,
  t=XMIN+#/n*(XMAX-XMIN);
  if(t<C.x,
    tmp=Assign("-t*x+t^2","t",t);
    Plotdata(text(# + n), tmp, "x", ["Num=1"]);
  );
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、たくさんの直線（または放物線状関数）を描いて、エンベロープ（包絡線）構造を視覚的に浮かび上がらせるものです。

* `Slider("C",...)`：描画範囲の可変条件を導入
* `forall((-n)..n)`：点列を走査して関数群を生成
* `Assign("-t*x+t^2","t",t)`：動的に変化するパラメータ t を代入し、各関数式を生成
* `Plotdata(...)`：1本ずつ直線（または曲線）を描画

この手法は、数学における包絡線や変化するパラメトリック関数の構造を捉える教材として適しています。

**ラベル（タグ）**
`Plotdata`, `Assign`, `forall`, `Slider`, `envelope`, `parametric`, `curve_family`, `geometry`, `2D`, `visualization`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
