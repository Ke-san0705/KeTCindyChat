## タイトル（両軸対数目盛の方眼紙生成）

### 想定質問

KeTCindyで、X軸もY軸も両方対数スケールにしたログ・ロググラフ用の方眼紙を作成したいです。どうすればできますか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["color=lightgray"]);

Addax(0);

if(nmx>0 && nmy>0,
  thick0=[0,"dr","Move=SW_xy"];
  thick1=[0,"dr_0.3","Move=SW_xy"];

  w=round(NE.x-SW.x);
  h=round(NE.y-SW.y);
  xL=apply(1..10,h/10);
  yL=apply(1..10,w/10);
  tb1=Tabledata(xL,yL,[],thick);
  xthick=apply(tb1_1,#1);
  ythick=apply(tb1_2,#2);

  // X軸の対数目盛配列
  xall=[];
  forall(1..nmx,
    x0=apply(1..10,log(1+#)/log(10));
    xL=apply(x0,#*h/10);
    xall=concat(xall,xL);
  );

  // Y軸の対数目盛配列
  yall=[];
  forall(1..nmy,
    y0=apply(1..10,log(1+#)/log(10));
    yL=apply(y0,#*w/10);
    yL=reverse(yL);
    yall=concat(yall,yL);
  );

  tb2=Tabledata(xall,yall,[],thin);

  // 不要な外枠を消す
  cL=select(1..length(tb2_1),contains(xthick,tb2_2_#1));
  cL=apply(cL,"c"+text(#)+"/r"+text(length(tb2_2)-1));
  rL=select(1..length(tb2_2),contains(ythick,tb2_2_#2));
  rL=apply(rL,"r"+text(#)+"/c"+text(length(tb2_1)-1));
  Changetablestyle(concat(cL,rL),["nodisp"]);
);

// ラベル追加オプション
if(tick0>0,
  htick=[];
  forall(0..nmx,
    htick=concat(htick,[[SW.x+xthick_#,"s",text(10^#)]]);
  );
  Expr(concat(htick,[]),[]);
);

if(tick1>0,
  vtick=[];
  forall(0..nmy,
    vtick=concat(vtick,[[SW.y+ythick_#,"s",text(10^#)]]);
  );
  Expr(concat([],vtick),[]);
);

//Figpdf([10,10,5,5]);
Windispg();
````

---

### 解説とラベル

このスクリプトでは、KeTCindyを使って **X軸・Y軸ともに対数スケール** に設定した方眼紙（log-logグラフ用）を描画します。

* `apply(1..10, log(1+#)/log(10))`：1〜10の対数を等間隔に計算
* `concat(xall,xL)`：各スケール分のログ目盛を結合
* `Tabledata(xall, yall, [], thin)`：細線グリッドを生成
* `Changetablestyle`：不要な罫線を削除して外枠を整える

この形式は、**指数関数・べき乗関数・スケーリング現象の可視化**などで活躍します。

**ラベル（タグ）**
`Tabledata`, `Expr`, `log_scale`, `loglog`, `graphpaper`, `tickmark`, `plot_base`, `grid`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
