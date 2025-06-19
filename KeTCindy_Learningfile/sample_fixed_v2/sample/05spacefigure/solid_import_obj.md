### 想定質問

KeTCindyで `.obj` 形式の3Dモデルを読み込んで表示するにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d();
Setketcindyjs(["Label=[]"]);

// ユーザディレクトリ内の obj ファイルを読み込む
// 例: http://mitani.cs.tsukuba.ac.jp/polyhedron/index.html
Setdirectory("cmetohm(\"~/polyhedrons_obj\")");
polyS=Readobj("r04.obj",["Size=3.5"]);
Setdirectory("cmywork");

Xyzax3data("","x=[-5,5]","y=[-5,5]","z=[-5,5]");
Vertexedgeface("1",polyS,["Obj=y"]);

// 表示制御（非表示処理・骨組み表示）
if(nohidflg!=1,
  tmp1=["ax3d","phf3d1"];
  tmp2=["phf3d1"];
  Nohiddenbyfaces("1",tmp1,tmp2);
);
if(skeleflg!=1,
  tmp=["ax3d","phf3d1"];
  Skeletonparadata("1",tmp,tmp,[1.5]);
);

Windispg();
```

---

### 解説とラベル

このコードは、**KeTCindyで3Dモデル（.obj形式）を読み込み、表示・非表示・骨組みを制御する一連の処理**を示しています。

* `Readobj(...)`：外部の`.obj`形式のファイルを3Dオブジェクトとして読み込み
* `Vertexedgeface(...)`：読み込んだポリゴンオブジェクトをKeTCindy上に描画
* `Setdirectory(...)`：ファイル読み込み用のパスを設定
* `Nohiddenbyfaces(...)`：隠面消去処理を実行
* `Skeletonparadata(...)`：骨組み構造をオーバーレイ表示

**応用例：**

* 外部で作成した多面体・CADオブジェクトの教育教材化
* オブジェクト構造の視認性強化（骨組み表示）
* WebGLとの連携を見据えた3D処理の可視化演習

---

### ラベル（タグ）

`Start3d`, `Setdirectory`, `Readobj`, `Vertexedgeface`, `Nohiddenbyfaces`, `Skeletonparadata`, `KeTCindy`, `3D`, `.obj import`, `hidden surface removal`, `solid model`, `external file`, `polyhedron`, `Xyzax3data`
