### 想定質問

3次元空間において、任意の平面上に円を描きたいのですが、どのようにEmbedを用いればよいですか？

---

### コード（CindyScript）

```cindy
Start3d();
Putaxes3d(5);
Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

// 平面と基準点の指定
Pointdata3d("O",[0,0,0],["notex"]);
Pointdata3d("A",[2,1,2],["Size=4","notex"]);
Perplane("B~C","A",A3d-O3d,["L=1,red","Size=3","Color=red","notex"]);

// 平面上のベクトル（AB, AC）による基底とEmbedの準備
AB3d=B3d-A3d;
AC3d=C3d-A3d;
pD3d=A3d+2*(AB3d-AC3d);
pE3d=A3d+2*(AB3d+AC3d);
pF3d=A3d+2*(-AB3d+AC3d);
pG3d=A3d+2*(-AB3d-AC3d);
Spaceline("1",[D3d,E3d,F3d,G3d,D3d]);

// 円の描画（Embedで平面に変換）
Circledata("1",[[0,0],[1,0]],["nodisp"]);
Embed("1",["cr1"],A3d+x*(B3d-A3d)+y*(C3d-A3d),["x,y"]);

if(nohidflg!=1,
  Nohiddenbyfaces("","[ax3d]","[face3d]");
);

Windispg();
```

---

### 解説とラベル

このコードは、**3次元空間において、平面上に円を描くためのEmbed操作の具体例**です。

* `Perplane(...)`：指定した法線ベクトルから平面を生成
* `Embed(...)`：2次元座標系（x, y）で定義した円を3次元空間上の平面に写像
* `Circledata(...)`：円の元データ（平面上での円）を指定
* `Spaceline(...)`：Embedされた領域の確認や骨組み表示などの補助的描画

この手法は、**平面内の2次元図形を3次元空間へ自然に拡張するための基本的な方法**です。

---

### ラベル（タグ）

`3D`, `Embed`, `Perplane`, `Circledata`, `平面`, `平面上の円`, `KeTCindy`, `幾何可視化`, `投影`, `空間図形`, `座標変換`, `ベクトル平面`, `CindyScript`
