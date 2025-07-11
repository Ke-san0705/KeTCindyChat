### 想定質問

KeTCindyで方程式の解や常微分方程式をWolframを用いて解くコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Ch=[1];

if(contains(Ch,1),
  cmdL=[
    "ans=Solve","x^2+4x+1=0","x",
    "ans1=x/.ans[[1]]", [],
    "ans2=x/.ans[[2]]", [],
    "ans1::ans2", []
  ];
  CalcbyW("ans",cmdL,["~"]);
  // Wltex("1",ans_1);
  // Wltex("2",ans_2);
);

if(contains(Ch,2),
  Wlfun("1","DSolve",["y'[x]+y[x]==a Sin[x]","y[x]","x"]);
  Wlfun("2","DSolve",["y'[x]+y[x]==a Sin[x], y[0]==0","y[x]","x"]);
  Wltex("1",w1);
  Wltex("2",w2);
);

Windispg();
```

---

### 解説

このコードは、KeTCindyからWolframを呼び出して以下の処理を行います：

* `Solve`: 方程式 `x^2+4x+1=0` の解を求め、解1と解2を抽出
* `DSolve`: 常微分方程式 `y'[x] + y[x] = a sin(x)` の一般解と初期値付き解を計算
* `CalcbyW`: 複数のWolfram式を順次計算するための関数
* `Wlfun`, `Wltex`: Wolfram呼び出しと結果のTeX出力表示を行う関数

---

### ラベル（関数KeTCindy）

`Ketinit`, `Addax`, `CalcbyW`, `Wlfun`, `Wltex`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`

---

### ラベル（その他）

`algebra`, `equation`, `solve`, `ODE`, `differential`, `Wolfram`, `symbolic`, `2D`
