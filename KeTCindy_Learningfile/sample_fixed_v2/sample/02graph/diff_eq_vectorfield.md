## タイトル（微分方程式の解曲線とベクトル場の描画）

### 想定質問

KeTCindyで微分方程式の解曲線を描くにはどうすればよいですか？ベクトル場や注釈も表示できますか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setketcindyjs(["Color=white","Nolabel=all"]);

Ch=[3];

if(contains(Ch,1),
  Setparent(Cdyname()+"fig1");
  Deqplot("1","y=y","x",0,1);
);

if(contains(Ch,2),
  Setparent(Cdyname()+"fig2");
  Deqplot("2","y=-4*y","x",0,[1,0],["Num=200"]);
);

if(contains(Ch,3),
  Setparent(Cdyname()+"fig3");
  Putpoint("A",[0.5,0.5],A.xy);
  Deqplot("3","[x,y]=[x*(1-y),0.3*y*(x-1)]","t=[0,20]",0,A,["Num=200"]);
  Expr([[0,4],"w","(x, y)=(x(1-y), 0.3 y(x-1))"],["size->20"]);
  Expr([[0,3],"w","(x, y)=\\mathrm{A} \\; (t=0)"],["size->20"]);
  Pointdata("1",A,["Size=3"]);
  Letter([A,"se","A"]);
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、微分方程式（常微分方程式・ベクトル場）に基づく解曲線の描画を行います。

* `Deqplot(...)`：常微分方程式の数値解を描く関数
* `"t=[0,20]"`：解を描く時間範囲を指定（tがパラメータ）
* `Putpoint("A",...)`：初期条件の点Aを定義
* `Expr(...)`：ベクトル場や初期条件に関する式を注釈として図中に表示
* `Ch=[3]`：描画モード（1：恒等式, 2：減衰, 3：2変数ベクトル）

動的な挙動の可視化に適しており、複雑な微分方程式モデルにも拡張できます。

**ラベル（タグ）**
`Deqplot`, `Putpoint`, `Expr`, `Pointdata`, `differential_equation`, `vectorfield`, `solution_curve`, `2D`, `geometry`, `visualization`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
