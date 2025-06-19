## タイトル（高密度グリッドと座標ラベル付き方眼紙の作成）

### 想定質問

KeTCindyで、1.5単位ごとに区切られた高密度な方眼紙を作成し、列番号・行番号を自動で表示する方法を教えてください。

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setparent(Cdyname()+"fig");

xLst=apply(1..50,2);  // 幅50マス
yLst=apply(1..50,2);  // 高さ50マス
rmvL=[];

Tabledata(xLst,yLst,rmvL,[10,"dr_0.5"]);

// 基準線
Tlistplot(["r1","c0r0","c50r0","c50r50","c0r50","c0r0"]);

ct=r5;
sen=5;
forall(1..5,
  tmp1="c0r"+sen;
  tmp2="c50r"+sen;
  Tlistplot(text(ct),[tmp1,tmp2],["dr_0.5"]);
  ct=ct+1;
  tmp1="c"+sen+"r0";
  tmp2="c"+sen+"r50";
  Tlistplot(text(ct),[tmp1,tmp2],["dr_0.5"]);
  ct=ct+1;
  sen=sen+10;
);
````

---

### 解説とラベル

このスクリプトは、KeTCindyで高密度な方眼紙を作成する構成例です。特徴は以下の通りです：

* `xLst=apply(1..50,2)`：2単位ごと（1.5単位幅ベース）で区切られた水平線
* `Tlistplot(...)`：特定のラインや外枠、メモリ線を明示的に強調
* `text(ct)`：ラベル番号をテキストとして利用する準備（必要に応じて数値記載可）

用途：

* 高解像度のグリッドで正確な描画支援が必要な場合
* グラフ用紙や幾何学の作図下地として有用

**ラベル（タグ）**
`Tabledata`, `Tlistplot`, `grid`, `dense_grid`, `labeling`, `geometry`, `2D`, `graphpaper`, `plot_background`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
