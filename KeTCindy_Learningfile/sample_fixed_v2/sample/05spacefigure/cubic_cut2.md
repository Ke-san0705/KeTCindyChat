### 想定質問

KeTCindyで立方体の断面と構成線を表示し、任意の線分を交差させた切断立体を描画するにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d();
//Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

Putonseg3d("A",[0,0,2]);
Putonseg3d("B",[0,0,-2]);
Putonseg3d("C",[0,2,0]);
Putonseg3d("D",[0,-2,0]);
Putonseg3d("E",[A3d_1,B3d_2,0],["fix"]);
Putonseg3d("F",[0,B3d_2,C3d_3],["fix"]);
Putonseg3d("G",[A3d_1,B3d_2,C3d_3],["fix"]);

Putonseg3d("P",[0,A3d_1,B3d_2,0]);
Putonseg3d("Q",[0,B3d_2,C3d_3],["fix"]);

Spaceline("1",[0,A]);
Spaceline("2",[0,B]);
Spaceline("3",[0,C]);
Spaceline("4",[0,D]);
Spaceline("5",[0,E]);
Spaceline("6",[0,F]);
Spaceline("7",[0,A]);
Spaceline("8",[B,F]);

alledg=apply([1..8],"s3d"+text(#));

Putonseg3d("H",[E,C]);
Putonseg3d("K",[C,F]);
Putonseg3d("L",[E,A]);

IntersectspGL("M","F~B","H~K~L","put");

Spaceline("9",[H,L,M,K]);

// チェックと切断処理
if(contains(Ch,1),
  changestyle3d(alledg,["do"]);
);
if(contains(Ch,2),
  tmp1=[0,A,D,B];
  tmp2=[B,D,N,M];
  tmp3=[B,O,C,N];
  tmp4=[O,K,N,C];
  tmp5=[A,L,H,K];
  tmp6=[L,H,M,K];
  tmp7=[C,H,K];

  dtp=concatobj([tmp1,tmp2,tmp3,tmp4,tmp5,tmp6,tmp7]);
  VertexEdgeFace("1",dtp);
);

if(contains(Ch,3),
  Nohiddenbyfaces("1",["phe3d1"],["phf3d1"]);
);
if(contains(Ch,4),
  Skeletonparadata("1");
);

Windispg();
```

---

### 解説とラベル

このコードは、**立方体の構造の中に任意の点と線を通して切断・構成要素を表示する**高度な図形生成例です。

* `Putonseg3d(...)`：辺や対角上に点を定義（交点など）
* `IntersectspGL(...)`：点群と線分・平面交点計算
* `Spaceline(...)`：直線の描画
* `concatobj(...)`：切断された面群の定義
* `VertexEdgeFace(...)`：立体の面・辺・頂点の構築

**活用例：**

* 立方体切断の空間把握
* 空間ベクトルと立体構造の練習
* 工業設計・モデリングの補助教材

---

### ラベル（タグ）

`3D`, `Start3d`, `Putonseg3d`, `Spaceline`, `IntersectspGL`, `VertexEdgeFace`, `concatobj`, `立方体`, `切断面`, `交差`, `可視化`, `空間認識`, `KeTCindy`, `CindyScript`, `構造解析`, `hidden face`, `solid geometry`, `geometry`, `STEM`
