
## タイトル（3次元空間で点とベクトルを描画）

### 想定質問

3次元空間で座標軸を表示し、点とベクトルを描画するにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d();
SetketcindyJS(["Label=[]"]);

// 座標軸と原点
Xyzaxesdata("X",["x=[-5,5]","y=[-5,5]","z=[-5,5]"]);
Pointdata3d("A",[2,1,3],["Size=1"]);
Pointdata3d("B",[-1,1,-2],["Size=4"]);

// ベクトル表示
Sparcline("1",[A3d,B3d]);

// ラベルと角度測定補助（任意）
if(!islangled(),
  gtxt(["a3d3","3d3"]);
  Skeletorparadata("1",edt,edt,[1.5]);
);

Windispg();
````

---

### 解説

このコードは、**3次元座標空間における基本的なベクトル描画と点表示**の構成を示します。

* `Start3d()`：3次元空間モードへの切替
* `Xyzaxesdata(...)`：XYZ軸を指定範囲で表示（立体的）
* `Pointdata3d(...)`：3D空間上の点の描画（A, B など）
* `Sparcline(...)`：点と点の間のベクトル（直線）を描画
* `gtxt(...)` や `Skeletorparadata(...)`：補助記号（オプション）

**活用例：**

* 3次元ベクトルの可視化・計測演習
* 立体座標系の理解支援
* 空間図形の構造分析

---

### ラベル（タグ）

`3D`, `Start3d`, `Xyzaxesdata`, `Pointdata3d`, `Sparcline`, `vector`, `coordinate axes`, `spatial geometry`, `CindyScript`, `KeTCindy`, `visualization`, `geometry`

```
