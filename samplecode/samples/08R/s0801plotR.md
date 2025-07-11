### 想定質問

Rを用いての確率密度関数（正規分布など）をKeTCindyで可視化するコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["Color=0.1*[0,0,0,1]"]);

Slider("C",[0,-2],[3,-2]);

Ch=[0];

if(contains(Ch,0), //no ketjs on
 make=""; // Change to "r" when data are generated
 tmp=[make,"nodisp","Num=100","Pre="];
 PlotdataR("1","dnorm(x)","x",tmp);
 PlotdataR("2","dt(x,6)","x",tmp);
 PlotdataR("3","dchisq(x,3)","x=[0,XMAX]",tmp);
 Ketcindyjsdata(["grR1",grR1,"grR2",grR2,"grR3",grR3]);
); //no ketjs off

Setscaling(8);
Htickmark([1,"1"]);
Vtickmark([0.5,"0.5"]);

if(round(C.x)==1,
 Listplot("grR1",grR1);
 Expr([0.5,0.6],"e","N(0,1)",["Size=1.6"]); 
);
if(round(C.x)==2,
 Listplot("grR2",grR2);
 Expr([0.5,0.6],"e","t_6",["Size=1.6"]); 
);
if(round(C.x)==3,
 Listplot("grR3",grR3);
 Expr([0.5,0.6],"e","\chi^2_3",["Size=1.6"]); 
);

//Figpdf();
Windispg();
```

---

### 解説とラベル

このコードは、Rの関数をKeTCindyで呼び出し、正規分布・t分布・カイ二乗分布のグラフを切り替えて表示するものです。

* `PlotdataR`: R言語の関数でプロットする。
* `Ketcindyjsdata`: データを変数として保存。
* `Slider` と `if(round(C.x)==n)`: スライダで分布の種類を切替。

---

### ラベル（関数KeTCindy）

`Ketinit`, `Setketcindyjs`, `PlotdataR`, `Ketcindyjsdata`, `Slider`, `Expr`, `Setscaling`, `Htickmark`, `Vtickmark`, `Listplot`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`, `round`

---

### ラベル（その他）

`R`, `distribution`, `graph`, `normal`, `t-distribution`, `chi-squared`, `statistical`, `2D`
