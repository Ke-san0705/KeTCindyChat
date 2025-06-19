### 想定質問

KeTCindyで三次元空間に多面体を描画し、辺・面の構造や骨組み表示を行う方法を教えてください。

---

### コード（CindyScript）

```cindy
Start3d();
//Setparent(Cdyname()+"fig");
Setketcindyjs(["Color=white"]);
//Putaxes3d(5);
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

polytd=[[ [1,2,4,7,2,4,7,0],[-2.47,2.47,0],[-2.47,-2.47,0],
          [0,0,3.5],[0,0,-3.5] ],
        [[1,2,5],[1,5,4],[1,4,6],[1,6,3],[3,4,5],[3,6,4]]];

Vertexedgeface("1",polytd,[ "Obj=jY"]);

if(nohidflg!=1,
  tmp1=["ax3d","phe3d1"];
  tmp2=["phf3d1"];
  Nohiddenbyfaces("1",tmp1,tmp2,[],["do"]);
);

if(skeleflg!=1,
  tmp1=["ax3d","phe3d1"];
  Skeletonparadata("1",tmp1,tmp1,[1.5]);
);

Windispg();
```

---

### 解説とラベル

このスクリプトは、**3次元空間上に任意の多面体（polyhedron）を定義し、それを可視化・解析する**ための基本例です。

* `polytd=...`：頂点座標および面構成をリストで定義
* `Vertexedgeface(...)`：指定した頂点と面から多面体を構築
* `Nohiddenbyfaces(...)`：隠面消去による輪郭強調（表示ON/OFF対応）
* `Skeletonparadata(...)`：骨組み表示。立体構造の強調と理解支援

**活用例：**

* 正多面体や任意多面体の構造解析
* 教育用に面・辺・頂点の関係性を可視化
* 数学オリンピック・STEAM教材向けコンテンツ生成

---

### ラベル（タグ）

`3D`, `polyhedron`, `Vertexedgeface`, `structure`, `KeTCindy`, `CindyScript`, `hidden surface removal`, `Nohiddenbyfaces`, `geometry`, `Skeletonparadata`, `多面体`, `頂点と面の定義`, `構造表示`, `STEAM`, `教育用可視化`
