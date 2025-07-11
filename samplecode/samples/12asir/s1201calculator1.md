### 想定質問

KeTCindyで四則演算・式の展開・因数分解などの電卓的な使い方をしたい場合のコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
Texparent="";

Ch=[];

if(contains(Ch,1),
  Asirfun("1","2*(3+(5*4))",[],[""]);
);

if(contains(Ch,2),
  Asirfun("2","(2*x-1)*(2*x+1)",[],[""]);
);

if(contains(Ch,3),
  Asirfun("3","fctr",["x^10-1"],[""]);
);

if(contains(Ch,4),
  Asirfun("4","deval",["3^(1/2)"],[""]);
);

Windispg();
```

---

### 解説

このコードは、KeTCindyを用いて Asir による電卓的な計算を行う基本例です：

* `Asirfun("1", "2*(3+(5*4))")`: 通常の四則演算の評価
* `Asirfun("2", "(2*x-1)*(2*x+1)")`: 式の展開（省略形でも結果が表示される）
* `Asirfun("3", "fctr", ["x^10-1"])`: 多項式の因数分解
* `Asirfun("4", "deval", ["3^(1/2)"])`: 数値評価

---

### ラベル（関数KeTCindy）

`Ketinit`, `Asirfun`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`

---

### ラベル（その他）

`calculator`, `evaluation`, `symbolic`, `factor`, `expand`, `2D`, `Asir`, `expression`
