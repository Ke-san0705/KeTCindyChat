### 想定質問

3D空間内の点とベクトル、投影を表示する基本的なKeTCindyコードを教えてください。

---

### コード（CindyScript）

```cindy
Start3d();
//Setparent(Cdyname()+"p");

SetketcindyJS(["Label=[]"]);

//Putaxes3d(5);
D3axesdata3d("O",[0,0,0],["notex"]);
Xyzxdata("","x=[-5,5]","y=[-5,5]","z=[-5,5]");

Pointdata3d("A",[2,1,3],["Size=4"]);
Pointdata3d("B",[1,-1,-2],["Size=4"]);

Spaceline("1",[A3d,B3d]);

if(!Isangle(),
 (
  adt=["ax3d","sl3d1"];
  Skeletonparadata("1",gdt,gdt,[1.5]);
 )
);

//Figpdf();
Windispg();
```

---

### 解説

このコードは、KeTCindyの3D機能を使って基本的な3次元表示を行うサンプルです。左図に立体（X,Y,Z軸）表示、右図にその平面投影を表示しています。

* `Start3d();`
  → 3Dモード開始
* `D3axesdata3d`
  → 3D座標軸の表示（O原点を中心とする）
* `Xyzxdata`
  → 各軸の範囲指定（\[-5,5]）
* `Pointdata3d`
  → 3D空間上に点 A, B を描画
* `Spaceline`
  → A3d と B3d を結ぶ直線（空間ベクトル）を描画
* `Skeletonparadata`
  → 3D→2D投影（右図）を自動生成

---

### ラベル（関数KeTCindy）

`Start3d`, `D3axesdata3d`, `Xyzxdata`, `Pointdata3d`, `Spaceline`, `Skeletonparadata`,`Isangle`,`Windispg`

---

### ラベル（関数CindyScript）

`if`

---

### ラベル（その他）

`3D`, `vector`, `projection`, `point`, `space`, `geometry`, `基本構文`, `視点切替`
