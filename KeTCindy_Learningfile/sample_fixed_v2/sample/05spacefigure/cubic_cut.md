### 想定質問

KeTCindyで2つの立方体の交差部分を表現し、その立体構造を視覚化するにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Start3d();
Putaxes3d(5);
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

pA3d=[-3.5,0.0,0];
pB3d=[3.5,0.0,0];
pC3d=[0.0,-3.5,0];
pD3d=[0.0,3.5,0];

Pointdata3d("1",[pA3d,pB3d,pC3d],["Color=blue"]);
pD3d_1=[pB3d_1,pB3d_2,0];
pD3d_2=[0,pC3d_2,pC3d_3];

Pointdata3d("2",[pD3d_1,pB3d_2,pC3d_3],["Color=yellow"]);

// 点の位置設定
Putonseg3d("H",[pA3d,pE3d]);
Putonseg3d("K",[pC3d,pE3d]);
Putonseg3d("L",[pC3d,pF3d]);

// 交差の計算
IntersectspGL("pM","pG~pD","H~K~L",["ie"]);
IntersectspGL("pN","pF~pB","H~K~L",["ie"]);

tmp1=[[pH,pM3d,pN3d,L],[1,2,3,4,5],[4,5,6]];
tmp2=[[pA3d,pD3d,pM3d],[1,2,3,4]];
tmp3=[[pM3d,pD3d,pB3d,pN3d],[1,2,3,4]];
tmp4=[[pC3d,L,pN3d,pB3d,K,pA3d],[1,2,3,4,5],[1,2,6,7,8]];

dtp=concatobj([tmp1,tmp2,tmp3,tmp4]);

VertexEdgeFace("1",dtp);

Ch=[Z];
if(contains(Ch,1),
  Nohiddenbyfaces("1",["phe3d1"],["phf3d1"]);
);
if(contains(Ch,2),
  Skeletonparadata("1",["phe3d1"],[1.5]);
);

Windispg();
```

---

### 解説とラベル

このコードは、**空間中の2つの立方体を交差・切断し、その交差領域を明示的に可視化する**例です。

* `Pointdata3d(...)`：基本点の配置
* `Putonseg3d(...)`：ベクトル上の点の導出（中点や交点）
* `IntersectspGL(...)`：空間内の線分・平面交差計算
* `concatobj(...)`：構成面を結合し立体化
* `VertexEdgeFace(...)`：立体データとして描画
* `Nohiddenbyfaces(...)`, `Skeletonparadata(...)`：隠面処理と骨組み切替

**活用例：**

* 幾何の空間交差・切断演習
* 多面体と空間構成の視覚教材
* 工学設計図のモデリング・可視化補助

---

### ラベル（タグ）

`3D`, `Start3d`, `Putaxes3d`, `Xyzax3data`, `Pointdata3d`, `Putonseg3d`, `IntersectspGL`, `concatobj`, `VertexEdgeFace`, `Nohiddenbyfaces`, `Skeletonparadata`, `立方体`, `交差`, `切断図形`, `立体構造`, `空間幾何`, `spatial geometry`, `solid modeling`, `KeTCindy`, `CindyScript`
