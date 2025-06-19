### 想定質問

3次元空間で任意の平面上に円を描き、その内部をハッチング（斜線）で塗りつぶしたいのですが、どうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d();
Putaxes3d(5);
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

// 平面の定義と基準ベクトル
Perplane("B~C","A",A3d-O3d,["notex"]);
AB3d=B3d-A3d;
AC3d=C3d-A3d;
pt1=A3d+2*(AB3d-AC3d);
pt2=A3d+2*(AB3d+AC3d);
pt3=A3d+2*(-AB3d+AC3d);
pt4=A3d+2*(-AB3d-AC3d);

// 平面上の枠・円・ハッチング
Spaceline("1",[pt1,pt2,pt3,pt4,pt1]);
Circledata("1",[[0,0],[1,0]],["nodisp"]);
Embed("1",["cr1"],A3d+x*(B3d-A3d)+y*(C3d-A3d),["x,y"]);
Hatchdata("1",["i","cr1"],["nodisp"]);
Embed("2","hai",A3d+x*(B3d-A3d)+y*(C3d-A3d),["x,y"]);

// 骨組み構造（スケルトン）表示
if(skeleflg!=1,
  tmp1=["ax3d"];
  tmp2=["sl3d1","em3d1","em3d2"];
  Skeletonparadata("1",tmp1,tmp2,[]);
);

Windispg();
```

---

### 解説とラベル

このスクリプトは、**Embed関数を用いて3D平面上に円を描き、さらにその領域をハッチング処理する**実例です。

* `Circledata(...)`：円の元データ（2D）
* `Embed(...)`：任意の平面上に写像
* `Hatchdata(...)`：円内部の斜線処理（描画指定により非表示にも対応）
* `Spaceline(...)`：四角形の骨組み
* `Skeletonparadata(...)`：対象領域の補助表示（骨構造）

この技法は、**投影平面内の面構造や断面の可視化**に有効であり、教材開発や幾何解析に応用できます。

---

### ラベル（タグ）

`3D`, `Embed`, `Hatchdata`, `Circledata`, `Spaceline`, `投影`, `斜線塗り`, `平面作図`, `KeTCindy`, `CindyScript`, `geometry`, `構造可視化`, `skeleton`, `plane`, `cross section`, `STEM教材`
