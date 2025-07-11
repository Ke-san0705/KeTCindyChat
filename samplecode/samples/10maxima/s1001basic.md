### 想定質問

様々な代数処理をKeTCindyで試すサンプルコードを教えて

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");
Ch=[3.1];
if(contains(Ch,1),
  Mxfun("1","100!",[],[""]);
);
if(contains(Ch,2),
  Mxfun("2","10!!",[],[""]);
);
if(contains(Ch,3),
  Mxfun("3","ratsimp",["x+(3*x-1)"],[""]);
);
if(contains(Ch,3.1),
  Mxfun("31","radcan",["sqrt(x)+x/(3*sqrt(x)-1)"],[""]);
);
if(contains(Ch,4),
  Mxfun("4","sum",["i","i",1,10],[""]);
);
if(contains(Ch,5),
  Mxfun("5","nusum",["i^2","i",1,"n"],[""]);
);
if(contains(Ch,6),
  Mxfun("6","ev",["x^2+5*x+3","x=3/4"]);
);
if(contains(Ch,7),
  Mxfun("6b","ev",["x^2*y+5*x+y+3","[x=1,y=2]"]);
);
if(contains(Ch,8),
  Mxfun("7","expand",["(x+y)^4"];,[""]);
);
if(contains(Ch,9),
  Mxfun("8","factor",["x^4 - 3*x^2 + 2"],[""]);
);
if(contains(Ch,10),
  Mxfun("9","partfrac",["x^3/((x+1)*(x+2))","x"],[""]);
);
if(contains(Ch,11),
  Mxfun("10","float",["%pi"],[""]);
);
if(contains(Ch,12),
  Mxfun("11","bfloat",["%pi",",fpprec:40"]);
);
if(contains(Ch,13),
  Mxfun("12","factorout",["x^2*y^2-2*y-2+x^2*y+x*y+y+x","y"]);
);
Figpdf();
Windispg();

```

---

### 解説

このコードは、KeTCindyを用いてMaximaの代数処理機能を試すデモです。

* `Mxfun`, `Mx`: KeTCindyからMaxima関数を呼び出すための専用関数。
* `ratsimp`, `radcan`, `sum`, `expand`, `factor`, `partfrac`, `float`, `bfloat`, `factorout`など多様な代数処理が実行されます。
* `Ch` 配列で有効な処理を選択可能（例: `[3..13]`）

---

### ラベル（関数KeTCindy）

`Ketinit`, `Setparent`, `Mxfun`, `Mx`, `Figpdf`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`

---

### ラベル（その他）

`algebra`, `symbolic`, `Maxima`, `simplify`, `expand`, `factor`, `sum`, `float`
