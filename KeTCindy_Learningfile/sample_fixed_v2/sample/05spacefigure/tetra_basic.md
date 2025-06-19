
## タイトル（正四面体の立体描画と隠面処理・骨組み表示）

### 想定質問

正四面体の頂点を指定して立体を描き、隠面消去や骨組み表示を行いたいです。どうすればよいですか？

---

### コード（CindyScript）

```cindy
Start3d();
SetketcindyJS(["Label=[]"]);

// XYZ軸
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-2,5]");

// 正四面体の頂点
Pointdata3d("O",[0,0,0],["nodisp"]);
Pointdata3d("A",[2*sqrt(1/3),-1/sqrt(3),0]);
Pointdata3d("B",[2*sqrt(1/3),1/sqrt(3),0]);
Pointdata3d("C",[0,2*sqrt(0.3),sqrt(3)]);

// 頂点ラベル付きで点のリストを連結し、立体定義
tmp=[["A","B","C","D"]];
dtp=concatobj(tmp);

// 多面体として描画
Vertexedgeface("1",dtp,["Obj=n"]);

// 隠面消去処理（オプション）
if(nohidflg==1,
  tmp1=["ax3d","phe3d1"];
  tmp2=["phf3d1"];
  Nohiddenbyfaces("1",tmp1,tmp2);
);

// 骨組み表示（オプション）
if(skeleflg==1,
  tmp=["ax3d","phe3d1"];
  Skeletonparadata("1",tmp,tmp,[1.5]);
);

Windispg();
````

---

### 解説とラベル

このコードは、\*\*正四面体の描画とその構造可視化（隠面処理・骨組み表示）\*\*を実現します。

* `Start3d()`：3D空間を初期化
* `Pointdata3d(...)`：頂点 O, A, B, C を明示的に指定して定義
* `concatobj(...)`：点の順序から面情報を生成
* `Vertexedgeface(...)`：立体（頂点・辺・面）として登録
* `Nohiddenbyfaces(...)`：視点に基づき隠面処理（前面だけ表示）
* `Skeletonparadata(...)`：立体のワイヤーフレーム（骨組み）表示

**活用例：**

* 正多面体の構造理解
* 立体の視点変化による見え方の学習
* 3Dモデリングと幾何学教材の基礎として

---

### ラベル（タグ）

`Start3d`, `SetketcindyJS`, `Xyzax3data`, `Pointdata3d`, `concatobj`, `Vertexedgeface`, `Nohiddenbyfaces`, `Skeletonparadata`,
`3D`, `tetrahedron`, `正四面体`, `geometry`, `solid modeling`, `KeTCindy`, `CindyScript`, `STEM`, `visualization`, `spatial reasoning`

```
