
## タイトル（地図画像上にBezier曲線を重ねて距離と面積を計測）

### 想定質問

地図画像上にBezier曲線を重ねて、距離や面積を可視化する方法を教えてください。

---

### コード（CindyScript）

```cindy
Ketinit();
Addax(0);

// 地図画像の読み込み（dogwalk.png）
drawimage([0,0],"dogwalk.png",scale->2,alpha->0.5);

// Bezierパスの描画（制御点 A〜H）
Mkbezierptcrv([A,B,C,D,E,F,G,H,A]);

// 曲線長と囲まれた面積を計算
tmp=Findlength("bza")*200/(L.x-ℓ.x);
Expr([−4,0],"L="+Sprint(tmp,2),["Size=1.6"]);
Expr([−4,3],"S="+Sprint(tmp^2,2),["Size=1.6"]);

Windispg();
````

---

### 解説とラベル

このコードは、**地図画像上にBezier曲線で道順をなぞり、その長さと面積を計測する**応用例です。以下のような機能があります：

* `drawimage(...)`：背景に地図画像（`dogwalk.png`）を読み込む
* `Mkbezierptcrv(...)`：地点 A〜H を通る閉じたBezier曲線の生成
* `Findlength(...)`：曲線長を計算し、地図スケールに基づいて距離換算
* `Expr(...)`：テキスト表示として距離 L と面積 S を描画

**応用例：**

* ウォーキングコースや通学路の距離測定
* 公園・施設の占有エリアの計測
* 地図上のパス可視化・ベクトル図形練習

---

### ラベル（タグ）

`Bezier`, `drawimage`, `Findlength`, `distance`, `area`, `scale conversion`, `map overlay`, `curve tracing`, `2D`, `geometry`

```
