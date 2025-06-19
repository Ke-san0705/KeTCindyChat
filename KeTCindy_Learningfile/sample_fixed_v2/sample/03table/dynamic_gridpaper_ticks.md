## タイトル（KeTCindyで可変マス目とメモリ付きの方眼紙を描く）

### 想定質問

KeTCindyで方眼紙のようなグリッドを描きたいのですが、メモリ付きで2, 5, 10マスごとに線を太くしたり、数値を表示する方法はありますか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");

// 太線の区切りを調整
thick0=[0,"dr","Move=SW_xy"];
thick5=[0,"dr_0.3","Move=SW_xy"];

if(tick==1,
  vtick=[];
  forall((round(SW.x))..(round(NE.x)),
    tick=concat(tick,[#,SW.y,"s",text(#)]);
  );
);

if(tick==2,
  htick=[];
  forall((round(SW.y))..(round(NE.y)),
    tick=concat(tick,[SW.x,#,"s",text(#)]);
  );
);

Expr(concat(htick,vtick),[]);

// グリッドの基本表
w=round(NE.x-SW.x);
h=round(NE.y-SW.y);
xL0=apply(1..w,10);
yL0=apply(1..h,10);
tb1=Tabledata(xL0,yL0,[],thick);
xThick=apply(tb1_1,#1);
yThick=apply(tb1_2,#2);

// メモリ線の間隔に応じて、太さ・ラベル設定
if(w>0,
  ndx=round(10/w/vd);
  xL=apply(1..ndx,vd);
  ndy=round(10/h/vd);
  yL=apply(1..ndy,vd);
  tb2=Tabledata(xL,yL,[],thin);

  cL=select(1..length(tb2_1),contains(xThick,tb2_1_#1));
  rL=select(1..length(tb2_2),contains(yThick,tb2_2_#1));
  cL=apply(cL,"c"+text(#)+"/0c"+text(length(tb2_2)));
  rL=apply(rL,"r"+text(#)+"/0r"+text(length(tb2_1)-1));
  Changetablestyle(concat(cL,rL),["nodisp"]);
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードでは、KeTCindyを使って以下のような「方眼紙」を作成します：

* `Tabledata(...)`：方眼のマス目を構成
* `xThick`, `yThick`：X軸・Y軸方向に太線を入れる箇所の記録
* `Expr(...)`：目盛りのラベル（数値）を表示
* `vd`（メモリ幅）を2, 5, 10などに変えることで、グリッド感を調整
* `Changetablestyle(...,"nodisp")`：不要な補助線を非表示にして明瞭化

このような仕組みは、座標学習や図解補助教材として応用できます。

**ラベル（タグ）**
`Tabledata`, `Expr`, `Changetablestyle`, `grid`, `graphpaper`, `tickmark`, `dynamic_display`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
