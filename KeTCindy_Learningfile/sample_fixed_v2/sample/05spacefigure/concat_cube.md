### 想定質問

KeTCindyで複数の立方体を連結して表示し、構造の可視化と隠面処理を施すにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d();
//Putaxes3d(5);
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

vertex=[[2,2,-2],[-2,-2,-2],[-2,2,-2],[2,-2,-2],
        [2,2,2],[-2,-2,2],[-2,2,2],[2,-2,2]];
edge=[[1,2],[1,5],[1,4],[1,3],[4,3,2],
      [6,5],[6,2],[6,7],[8,5,4]];
cubic=[vertex,edge];

VertexEdgeFace("1",cubic);

if(nohidflg!=1,
  printIn(15);
  Nohiddenbyfaces("1",["ax3d","phe3d1"],["phf3d1"]);
);

if(skeleflg!=1,
  Skeletonparadata("1",[1.5]);
);

Windispg();
```

---

### 解説とラベル

このスクリプトは、**3D空間上に2つの立方体を結合した構造体を可視化し、隠面処理と骨組み表示を併用**する例です。

* `vertex=...` と `edge=...`：2つの立方体の頂点と辺を定義
* `VertexEdgeFace(...)`：頂点と辺・面の情報から立体を構築
* `Nohiddenbyfaces(...)`：隠面消去処理（正面の視界を強調）
* `Skeletonparadata(...)`：骨組みのみを描画するオプション（スライダ切替対応）

**活用例：**

* 複合立体の表現（直方体や連結構造）
* 可視性の改善（隠面表示切替による学習補助）
* 数学・工学・建築分野の立体構成モデリング

---

### ラベル（タグ）

`3D`, `KeTCindy`, `CindyScript`, `VertexEdgeFace`, `Nohiddenbyfaces`, `Skeletonparadata`, `Start3d`, `Xyzax3data`, `Windispg`, `連結立方体`, `構造体`, `頂点と辺の定義`, `隠面処理`, `骨組み表示`, `立体構成`, `3次元図形`, `STEM教材`, `geometry`, `spatial modeling`, `axes3d`
