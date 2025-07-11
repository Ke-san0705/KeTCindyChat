### 想定質問

任意の3点を通る平面とその頂点を使った面の描画をKeTCindyで行うには？

---

### コード（CindyScript）

```cindy

poy=4.5;
drwt(line,str):=(
  drawtext([-5,poy],text(line)+" "+str,size->15);
  poy=poy-0.8;
);

Start3d([]);

Pointdata3d("O",[0,0,0]);
Xyzx3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

Pointdata3d("A",[1,2,3]);
Spaceline("1",[O3d,A3d]);

tmp=Perpplane("B-C","A",A3d-O3d,["Size=0.1","Color=white"]);
tmp=A3d+2*(B3d-A3d)+2*(C3d-A3d); Pointdata3d("D",tmp,["Size=1"]);
tmp=A3d+2*(B3d-A3d)-2*(C3d-A3d); Pointdata3d("E",tmp,["Size=1"]);
tmp=A3d-2*(B3d-A3d)+2*(C3d-A3d); Pointdata3d("F",tmp,["Size=1"]);
tmp=A3d-2*(B3d-A3d)-2*(C3d-A3d); Pointdata3d("G",tmp,["Size=1"]);

Spaceline("2",[D3d,E3d,F3d,G3d,D3d]);

sl3dall=["sl3d1"];
objdt=[[ "D3d", "E3d", "F3d", "G3d" ],[[1,2,3,4]]];
VertexEdgeFace("1",objdt);

Ch=[1];
if(contains(Ch,1),
  Nohiddenbyfaces("1",["ax3d","sl3dall","phe3d1","phf3d1"]);
);

//Windispg();
```

---

### 解説とラベル

このコードは、3点（B, C, A）を通る平面を作成し、それを拡張して四角形面（D–E–F–G）として描画するものです。

#### 重要な構文・機能

* `Perpplane("B-C","A",A3d-O3d,...)`
  → B, C, Aを使ってAを通る法線方向の平面ベクトルを生成（法線: OAベクトル）
* `Pointdata3d`
  → 拡張した四角形の頂点D, E, F, Gを配置
* `Spaceline`
  → 四角形の輪郭を線で描画
* `VertexEdgeFace`
  → 多面体面（Polygon）として描画用に構成
* `Nohiddenbyfaces`
  → 平面が他の要素により隠れないよう調整

---

### ラベル（関数KeTCindy）

`Start3d`, `Pointdata3d`, `Spaceline`, `Perpplane`, `VertexEdgeFace`, `Nohiddenbyfaces`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`, `drawtext`, `text`

---

### ラベル（その他）

`3D`, `plane`, `perpendicular`, `projection`, `geometry`, `vector`, `平面描画`, `法線ベクトル`, `4点ポリゴン`
