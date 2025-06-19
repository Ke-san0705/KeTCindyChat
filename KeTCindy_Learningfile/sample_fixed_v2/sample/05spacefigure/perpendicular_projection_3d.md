### 想定質問

KeTCindyで、3次元空間上の平面に垂直な方向から投影された四角形を描画し、骨組み表示と非表示の切り替えを行いたいのですが、どうすればいいですか？

---

### コード（CindyScript）

```cindy
Start3d();
//Putaxes3d(5); // 軸は不要であれば省略可
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

// 基準点と平面上の点
Pointdata3d("O",[0,0,0],["notex"]);
Pointdata3d("A",[2,1,2],["Size=4","notex"]);
Perplane("B~C","A",A3d-O3d,["L=ne,1,red","notex"]);

// 四角形の他の頂点の定義
AB3d=B3d-A3d;
AC3d=C3d-A3d;
D3d=A3d+2*(AB3d-AC3d);
E3d=A3d+2*(AB3d+AC3d);
F3d=A3d+2*(-AB3d+AC3d);
G3d=A3d+2*(-AB3d-AC3d);

Vertexedgeface("1",["D","E","F","G"]);

// 表示切り替え
if(nohidflg!=1,
  Nohiddenbyfaces("1",["ax3d","phf3d1"]);
);

if(skeleflg!=1,
  Skeletonparadata("1",[1.5]);
);

Windispg();
```

---

### 解説

このスクリプトは、**3次元空間における平面とその垂直方向の投影を含む視覚的な構造描画**を行います。

* `Start3d()`：3D空間の初期化
* `Perplane(...)`：指定したベクトルに垂直な平面を構築
* `Vertexedgeface(...)`：平面上の四角形を頂点と辺、面で描画
* `Nohiddenbyfaces(...)`：隠面消去処理（視認性のため）
* `Skeletonparadata(...)`：骨組み構造のオーバーレイ表示（平面・輪郭の確認用）

このような処理は、**平面幾何や3Dのベクトル解析の教材・可視化に有効**です。

---

### ラベル（タグ）

`3D`, `平面の可視化`, `垂直投影`, `Perplane`, `Vertexedgeface`, `構造解析`, `幾何学`, `隠面消去`, `Nohiddenbyfaces`, `Skeletonparadata`, `STEM教育`, `KeTCindy`, `CindyScript`, `平面作図`, `直交`, `投影幾何`

---

### 解説とラベル

このコードは、KeTCindyを使って特定の幾何・グラフを描画するものです。
