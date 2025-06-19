## タイトル（テンキー入力で関数を動的に描画）

### 想定質問

KeTCindyでテンキーのようなUIから関数式を入力し、その関数をプロットしたいです。どうすればできますか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");

aPLB=[7,0];
PLB=Tenkeybrd(aPLB,["ShadeY"]);

Plotdata("1","x^2","x",["Color=blue"]);
Lineplot("1",[[0,1],[1,2]],["dr,0.5"]);

if(textKey!=1,
  End=IsKeyaction(key);
  drawtext(PLB,[0.8,0.8],Tenkeys,size->16);
  textKey=1;
);

if(End!=1,
  a=parse(Tenkeys);
  fun=Assign("x^"+a,["a"]);
  Plotdata("2",fun,"x",["Colored"]);
  Tenkeys="";
  End=[s:0];
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、KeTCindyで**テンキーUIを用いて関数の式を入力**し、その入力値に基づいたグラフを描画する機構を示しています。

* `Tenkeybrd(...)`：テンキーの作成（文字入力UI）
* `textKey`/`End`：入力の確定と判定の制御
* `parse(...)`：文字列としての入力を `Assign()` により関数に変換
* `Plotdata(...)`：入力関数を動的に描画

このように、KeTCindyをインタラクティブな**計算・描画ツール**として活用できます。

**ラベル（タグ）**
`Tenkeybrd`, `Plotdata`, `Assign`, `parse`, `dynamic_input`, `interactive_plot`, `calculator`, `function_input`, `2D`, `geometry`, `UI`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
