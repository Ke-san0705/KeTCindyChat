## タイトル（対数目盛付きグリッドの作成）

### 想定質問

KeTCindyで縦軸または横軸を対数目盛にした方眼紙（ロググラフ）を描くにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["color=lightgray"]);

Addax();

thick0=[0,"dr","Move=SW_xy"];
thick1=[0,"dr_0.3","Move=SW_xy"];

if(n>0,
  w=round(NE.x-SW.x);
  h=round(NE.y-SW.y);

  xL=apply(1..10,h/10);
  yL=apply(1..10,w/10);
  tb1=Tabledata(xL,yL,[],thick);
  xThick=apply(tb1_1,#1);
  yThick=apply(tb1_2,#2);

  // 対数スケールの目盛計算
  nn=round(10*log10(w/5));
  ndx=round(10*w/5);
  xL=apply(1..ndx,.5);
  yL=exp(h/nn);
  yL=apply(1..10,log(1+#)/log(10));
  yL=apply(yL,#*h/10);
  yL=reverse(yL);
  yAL=[];
  forall(1..nn,
    yAL=concat(yAL,yL);
  );

  tb2=Tabledata(xL,yAL,[],thin);

  // 不要線の除去と強調ラベル
  cL=select(1..length(tb2_1),contains(xThick,tb2_2_#1));
  cL=apply(cL,"c"+text(#)+"/r"+text(length(tb2_2)));
  rL=select(1..length(tb2_2),contains(yThick,tb2_2_#2));
  rL=apply(rL,"r"+text(#)+"/c"+text(length(tb2_1)));
  Changetablestyle(concat(cL,rL),["nodisp"]);
);

// 目盛ラベル表示（オプション）
if(tick0,
  htick=[];
  forall((round(SW.x))..(round(NE.x)),
    htick=concat(htick,[[#,SW.y,"s",text(#)]]);
  );
);
if(tick1,
  vtick=[];
  forall(0..nn,
    y=tick=concat(tick,[[SW.x,yAL_#,"s",text(10^#)]]);
  );
);
Expr(concat(htick,vtick),[]);
````

---

### 解説とラベル

このコードは、KeTCindyで対数グラフのような方眼紙を生成するための構成例です：

* `exp(...)`・`log(...)` を使って対数目盛を作成
* `Tabledata(...,[],thin)`：縦方向に対数目盛グリッドを描画
* `yAL`：logスケールの補助値配列を繰り返して対数目盛を模倣
* `Expr(...)`：数値ラベル（例：1, 10, 100, ...）を表示

**ラベル（タグ）**
`Tabledata`, `Expr`, `log_scale`, `logarithmic`, `grid`, `graphpaper`, `tickmark`, `axis_label`, `2D`, `plot_base`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
