
## タイトル（CRスプラインとDスプラインで描く円の比較）

### 想定質問

KeTCindyで円のような滑らかな曲線を描く方法として、CRスプラインとDスプラインの違いを確認したいです。

---

### コード（CindyScript）

```cindy
Ketinit();

p0=[-3,0];
p1=[-2,1];
p2=[-1,2];
p3=[0,1];
p4=[-1,0];

q0=[2,1];
q1=[3,2];
q2=[4,1];
q3=[3,0];
q4=[2,1];

Circledata("1",[p0,p1]);
Pointdata("1",[p1,p2,p3,p4,p1],["Size=3"]);
Circledata("2",[q0,q1]);
Pointdata("2",[q1,q2,q3,q4,q1],["Size=3"]);

Ch=[1];

if(contains(Ch,1),
  CRspline("1",[p1,p2,p3,p4,p1],["Colored"]);
  Dspline("1",[q1,q2,q3,q4,q1],["Colored"]);
);

Windispg();
````

---

## 解説とラベル

このスクリプトは、**円を模した制御点をもとに、CRスプラインとDスプラインを比較表示**しています。

* `CRspline(...)`：CRスプライン補間。連続性（曲率）を重視して滑らかな曲線を生成。端点の接続性が高い。
* `Dspline(...)`：Dスプライン補間。通常の補間スプライン。やや直線的な接続が強調される。
* `Pointdata(...)`：各制御点の可視化（比較のために円に近い制御点配置）
* `Circledata(...)`：円との比較用に参考円も同時表示

この例は、**円の近似にどのような補間法が有効かを学ぶ**目的に適しています。

## ラベル（タグ）

`CRspline`, `Dspline`, `Pointdata`, `Circledata`, `closed curve`, `interpolation`, `geometry`, `circular approximation`, `2D`, `comparison`

```
```
