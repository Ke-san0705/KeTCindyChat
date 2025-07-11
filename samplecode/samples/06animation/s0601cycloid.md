### 想定質問

アニメーションでサイクロイド曲線を描くKeTCindyのコード例を教えて。

---

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"fig");
Setketcindyjs(["Label=[]","Color=offwhite"]); //no ketjs

Slider("C",[XMIN,YMIN-1],[XMAX,YMIN-1]);

Setax(["","","sw","","sw"]);
Circledata("1",[[0,1],[1,1]],["Color=red","Msg=n"]);

mf(s0):=(
  regional(s,fun,rng);
  s=mod(s0,10);
  Circledata("2",[[s,1],[s+1,1]],["Msg=n"]);
  Pointdata("2",[s-sin(s),1-cos(s)],["Size=3","Msg=n"]);
  if(s>0,
    rng=Assign("t=[0,s]",["s",s]);
    Paramplot("2","[t-sin(t),1-cos(t)]",rng,["do","Msg=n"]);
  );
);
Setpara("cycloid","mf(s)","s=[0,10]",["Div=25"],
 ["Frate=10","Scale=1","OpA=","Title=Cycloid"]);

ss=Animationparam(C.x-XMIN,2,20);
mf(ss);

Figpdf();
Windispg();
```

---

### 解説とラベル

このコードは、円の周縁上の1点が描く「サイクロイド曲線」の軌跡をKeTCindyでアニメーション付きで表示します。

* `Slider("C",...)`: アニメーション用スライダー
* `mf(s())`: フレームごとに描画する関数

  * 円の描画 `Circledata("2",...)`
  * 点の描画 `Pointdata(...)`
  * 軌跡 `Paramplot(...)`
* `Setpara(...,"mf(s)",...)`: アニメーションパラメータ設定
* `Animationparam(...)`: 実行アニメの軸指定

---

### ラベル（関数KeTCindy）

`Slider`, `Setax`, `Circledata`, `Pointdata`, `Paramplot`, `Setpara`, `Animationparam`, `Figpdf`, `Windispg`

---

### ラベル（関数CindyScript）

`regional`, `mod`, `sin`, `cos`, `Assign`, `if`

---

### ラベル（その他）

`cycloid`, `animation`, `curve`, `parametric`, `geometry`, `2D`, `rolling`, `円運動`, `軌跡`, `サイクロイド`
