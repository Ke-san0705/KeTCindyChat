### 想定質問

3次元空間に放物面を表示するKeTCindyのコード例を教えて

---

### コード（CindyScript）

```cindy
Start3d();
//Setangle(70,50);

Putaxes3d(4);
Xyzax3ddata("", "x=[-5,5]", "y=[-5,5]", "z=[-5,5]");

fd1=[
  "z=4-(x^2+y^2)",
  "x=R*cos(T)", "y=R*sin(T)",
  "R=[0,2]", "T=[0,2*pi]", "e"
];

fd2=[ // defined as parametric functions
  "p", 
  "x=R*cos(T)", "y=R*sin(T)", "z=4-R^2",
  "R=[0,2]", "T=[0,2*pi]", "e"
];

Addsurf([fd1,fd2]);

if(!Isangle(), // if TH/FL is selected.
  Sf3data("1",1); // use 1st in Addsurf
  Ch=[];
  Ch=[1];
);

if(contains(Ch,1),
  Startsurf("1");
  opr=["dr,1.5","Color=red",""];
  $fbdparadata("1",1,opr,[]);
  opb=["Color=blue",""];
  Crvsfparadata("1","ax3d","sfbd3d1",1,opb);
  ExecmdC([""]);
);//1

Windispg();
```

---

### 解説

このコードは、KeTCindyで3D放物面 $z = 4 - (x^2 + y^2)$ を描画し、極座標でパラメトリック表示されたサーフェスをアニメーション付きで表示します。

* `fd1`, `fd2`: いずれも放物面をパラメータ表示した定義
* `Addsurf`: 曲面データの追加
* `Sf3data`, `Startsurf`, `Crvsfparadata`: 表示設定や軌跡描画を担うKeTCindy関数

---

### ラベル（関数KeTCindy）

`Start3d`, `Putaxes3d`, `Xyzax3ddata`, `Addsurf`, `Sf3data`, `Startsurf`, `Isangle`, `Crvsfparadata`, `ExecmdC`, `Windispg`

---

### ラベル（関数CindyScript）

`if`, `contains`

---

### ラベル（その他）

`3D`, `surface`, `paraboloid`, `parametric`, `graph`, `axis`, `rotation`
