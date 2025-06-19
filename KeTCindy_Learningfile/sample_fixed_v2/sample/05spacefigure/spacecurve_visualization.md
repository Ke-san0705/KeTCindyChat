
## タイトル（螺旋曲線の可視化と投影の比較）

### 想定質問

空間曲線（例えば螺旋）をKeTCindyで可視化し、透視投影と平行投影の両方で比較表示するにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Start3d();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["Remove=[O,X,Y,Z]"]);

Putaxes3d(5);  // 座標軸の描画
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

// 螺旋の定義と描画
Spacecurve("1","3*[cos(t),sin(t),0.1*t]","t=[0,4*pi]",["Num=200"]);

// 螺旋の端点を定義
pA=[3,0,0];
pB=[3,0,3*0.1*4*pi];
SpaceLine("1",[pA,pB]);

// 骨組み表示の条件処理
if(skeleflg==1,
  tmp=["ax3d","sc3d1","sl3d1"];
  Skeletonparadata("1",tmp,tmp,[1.5,"File=y"]);
);

//Windispg()で表示
//Figpdf();
Windispg();
````

---

### 解説

このスクリプトは、**3次元空間内の螺旋（ヘリカルカーブ）を生成・表示**し、それを異なる投影で描画する方法を示しています。

* `Start3d()`：3Dモードの初期化
* `Putaxes3d(...)`：空間軸の表示
* `Spacecurve(...)`：空間曲線の生成（tパラメータによる）
* `SpaceLine(...)`：補助線（端点を結ぶ線）
* `Skeletonparadata(...)`：透視・平行投影を切り替えた比較図の生成に使える（骨組み表示）

このような可視化は、**空間中のパラメトリック曲線の理解や、数学的概念の説明**に非常に有効です。

---

### ラベル（タグ）

`3D`, `Spacecurve`, `螺旋`, `パラメトリック曲線`, `Start3d`, `Putaxes3d`, `Skeletonparadata`, `projection`, `螺旋曲線`, `CindyScript`, `geometry`, `visualization`, `STEM教育`, `space curve`, `helix`, `透視図法`, `平行投影`

```
