### 想定質問

KeTCindyで定積分や不定積分の計算結果を表示するコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
Texparent="";

Ch=[];

if(contains(Ch,1),
  fun="((1-cos(t))/(1/2-cos(t)))^(1/2)";
  Frifun("1","integrate",[fun,"t"],[""]);
);

if(contains(Ch,2),
  Mxtex("1",fri1,["Disp=n"]);
  Expr(A,"e",tx1);
);

Windispg();
```

---

### 解説

このコードは KeTCindy で不定積分を求め、その結果を式として表示する例です。

* `Frifun("1", "integrate", [...])`: 式 `((1 - cos(t)) / (1/2 - cos(t)))^(1/2)` の不定積分を計算
* `Mxtex` と `Expr` を用いて、結果を数式表示

---

### ラベル（関数KeTCindy）

`Ketinit`, `Frifun`, `Mxtex`, `Expr`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`

---

### ラベル（その他）

`integration`, `calculus`, `symbolic`, `expression`, `2D`, `不定積分`, `表示`
