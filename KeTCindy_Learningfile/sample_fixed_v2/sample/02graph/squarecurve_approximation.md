## タイトル（二乗曲線への点プロットと近似評価）

### 想定質問

KeTCindyで \( y = x^2 \) 上に点をプロットして、点列をなめらかに補間したり、近似精度を計算することはできますか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");

Setketcindyjs(["Grid=0.5","Nolabel=all","Color=offwhite"]);
Setwindow([-4.5,4.5],[-0.5,10.5]);
Drawgrid([-4,4],[0,10]);

Expr([[1,YMAX],"ne","y=x^2",["size->20"]]);

if(prepreactr,
  cptL=Preparectpt(ctrlL);
  prepreactr=false;
);

if(resetctr,
  Resetctrpt(cptL);
  resetctr=false;
);

if(length(ptL)>0,
  Pointdata("0",ptL,["Size=3","Color=blue","Msg=n"]);
);

if(movectr,
  if(setctr,
    kcl=Setbezier(sort(ptL));
    setctr=false;
  );
  Movectr(kcl_2);
  Bezier("1",kcl_1,kcl_2,["Num=20","Msg=n"]);

  tmp=apply(bzl,abs(#_2-(#_1)^2));
  if(length(tmp)>0,
    mean=sum(tmp)/length(bzl);
    tmp="D="+Sprintf(mean*1000,2);  // 誤差スコア表示
    Expr([[5,4],"e",tmp,["notex","Size=1.5"]]);
  );
);

if(drawgraph,
  Plotdata("qg","x^2","x",["Color=blue"]);
);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このスクリプトは、次のような教育的・視覚的目的で構成されています：

* $y = x^2$ 上に **複数の点**をクリック等でプロット (`ptL`)
* `Bezier` 補間を用いて、点をなめらかに曲線で接続
* `apply(... abs(...))` により各点の誤差を計算
* `Expr` を使って平均誤差（1000倍スケーリング）の数値を表示
* `Drawgrid`, `Setwindow` により、視覚的に整ったグラフ表示領域

関数曲線の近似、点の補間、近似評価などを体験的に学ぶのに適しています。

**ラベル（タグ）**
`Pointdata`, `Bezier`, `apply`, `Expr`, `approximation`, `curve_fit`, `graph`, `parabola`, `education`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
