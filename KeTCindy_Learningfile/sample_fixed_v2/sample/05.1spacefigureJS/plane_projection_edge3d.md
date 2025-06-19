### 想定質問

3次元空間上に平面を定義し、特定の点や線分を平面上に投影する方法を教えてください。

---

### コード（CindyScript）

```cindy
poy=4.5;
drwt(line,str):=(
  drawtext([−5,poy],text(line)+" "+str,size->15);
  poy=poy−0.8;
);

Start3d([]);

Pointdata3d("O",[0,0,0]);
Xyzax3data("","x=[−5,5]","y=[−5,5]","z=[−5,5]");
Pointdata3d("A",[2,2,3]);
Spaceline("1",[O3d,A3d]);

tmp2=Perplane("B~C","A",A3d-O3d,["Size=0.1","Color=white"]);
tmp=A3d+2*(B3d-A3d)+2*(C3d-A3d);
Pointdata3d("D",tmp,["Size=1"]);
tmp=A3d+2*(B3d-A3d)-2*(C3d-A3d);
Pointdata3d("E",tmp,["Size=1"]);

Spaceline("2",[O3d,A3d]);

S3dall=["s3d1"];
objd=[[D3d,E3d,F3d,G3d],[1,2,3,4]];
VertexEdgeFace("1",objd);

Ch=[1];
if(contains(Ch,1),
  Nohiddenbyfaces("1",
    ["ax3d","s3d1all","phe3d1","phf3d1"]
  );
);

// 骨組み表示は任意で有効化可能
// if(contains(Ch,2),
//   Skeletonparadata("1",[],[1.5]);
// );

Windispg();
```

---

### 解説とラベル

このコードは、**任意の点とベクトルを基に3次元空間上の平面を定義し、そこに図形（四角形）を形成する一連の操作**を示しています。

* `Start3d()`：3次元描画を初期化
* `Pointdata3d(...)`：点の定義（O, A など）
* `Perplane(...)`：A−O方向に垂直な平面を構成し、平面上のBとCを自動配置
* `Spaceline(...)`：空間ベクトルを描画（A→B、A→C等）
* `VertexEdgeFace(...)`：点集合に基づいてポリゴン面を描画
* `Nohiddenbyfaces(...)`：隠面消去によって可視部分のみを描写

**応用例：**

* 平面ベクトルの直交性の可視化
* 3次元空間内の四角形投影と面の可視化
* 座標から定義される空間平面の構築練習

---

### ラベル（タグ）

`Start3d`, `Pointdata3d`, `Xyzax3data`, `Spaceline`, `Perplane`, `VertexEdgeFace`, `Nohiddenbyfaces`, `s3d1`, `3D`, `平面構成`, `空間投影`, `面の描画`, `CindyScript`, `KeTCindy`, `直交ベクトル`, `geometry`, `平面作図`, `構造可視化`
