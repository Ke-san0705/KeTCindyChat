## タイトル（暗黙的曲線の描画とスライダーによる回転）

### 想定質問

KeTCindyで暗黙的関数 \( f(x, y) = 0 \) の曲線を描き、スライダーでその曲線を回転させるにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
Setketcindyjs(["Nolabel=all"]);

Slider("T",[0,-6],[2*pi,-6]);

Implicitplot("1","x^2+xy+2*y^2=4","x=[-3,3]","y=[-3,3]");

// 以下の行は回転後の代替式の例（使用しない場合はコメントのままで可）
// Implicitplot("2",(x-A.x)^2+2*(x-A.x)*(y-A.y)+2*(y-A.y)^2=1",x=[-3,3],y=[-3,3]);

Rotatedata("1","imp1",T.x);

// Hatchdata で塗りつぶし等も可能
// Hatchdata("1",["imp1"],[["re"]]);

Windispg();
````

---

### 解説とラベル

このコードでは、暗黙的に定義された2変数関数（例：$x^2 + xy + 2y^2 = 4$）の曲線を描画し、スライダー `T` によってその全体を回転させる操作を実現しています。

* `Implicitplot(...)`：明示的に解けない関係式から曲線を描画
* `Slider("T",...)`：回転角度をユーザーが操作可能にする
* `Rotatedata(...)`：指定された角度だけ、オブジェクトを回転
* コメントの `Hatchdata` を使えば塗り潰し表現も追加可能

このような設定は、回転対称性の確認や軌道の操作の可視化など、応用範囲の広い構成です。

**ラベル（タグ）**
`Implicitplot`, `Slider`, `Rotatedata`, `transformation`, `algebraic_curve`, `rotation`, `interactive`, `geometry`, `2D`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
