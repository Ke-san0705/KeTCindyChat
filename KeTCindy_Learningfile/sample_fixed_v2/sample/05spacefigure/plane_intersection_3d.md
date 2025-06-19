
## タイトル（3D多角形の描画と投影の比較）

### 想定質問

3次元空間において、点を結んでできる多角形の面を描き、透視投影と並列投影を比較表示するにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Start3d();
Xyzaxesdata("1",["x=[-5,5]","y=[-5,5]","z=[-5,5]"]);

// 原点と点の配置
opnt=[0,0,0];
apt(="Size=3","notex",1);
Pointdata3d("O",opnt);
Pointdata3d("A",[0,0,0],["notex"]);
Pointdata3d("B",[2,1,0]);
Pointdata3d("C",[1,2,3]);
Pointdata3d("D",[0,4,3]);
Pointdata3d("E",[4,0,0]);
Pointdata3d("F",[2,3,0]);
Pointdata3d("G",[-1,3,2]);

// 各面の表示
Perpline3d("r",[A3d,B3d],["dr"]);
Perpline3d("r",[C3d,D3d],["dr"]);
Perpline3d("r",[E3d,F3d],["dr"]);
Perpline3d("r",[G3d,O3d],["dr"]);

d1=[A3d,B3d,C3d];
d2=[D3d,E3d,F3d];
d3=[G3d,O3d];
dt1=Connectbonds(d1);
dt2=Connectbonds(d2);
dt3=Connectbonds(d3);

// 多面体の面の集合
VertaExfacedata("1",[dt1,dt2,dt3],["Obj=m"]);

// 投影条件により透明化を切り替え
if(!isNohid(),
  Nohidbindfaces("1",
    tmp,[Pshaded("1",[r1,r2,r3])],
    ["r1","r2","r3"]
  );
);
if(isSkele(),
  Skeletorparadata("1",tmp,tmp,[1.5]);
);

Windispg();
````

---

### 解説

このスクリプトは、**3次元空間上に点群で構成される面（多角形）を配置し、その可視化と投影変換処理を組み込んだ例**です。

* `Start3d()`：3D空間モード
* `Pointdata3d(...)`：各頂点の登録
* `Perpline3d(...)`：辺を表示（点間ベクトル）
* `Connectbonds(...)`：点の配列から辺リストへ変換
* `VertaExfacedata(...)`：面の生成（複数面）
* `Nohidbindfaces(...)`：背面非表示（透視処理）
* `Skeletorparadata(...)`：骨組み構造の表示補助

この図は、**多角形平面の構造理解や3D図形の比較描写に非常に有用**です。

---

### ラベル（タグ）

`3D`, `polygon`, `Start3d`, `Pointdata3d`, `Connectbonds`, `VertaExfacedata`, `Skeletorparadata`, `geometry`, `solid figure`, `face`, `3D_projection`, `visualization`, `parallel vs perspective`, `CindyScript`

```
