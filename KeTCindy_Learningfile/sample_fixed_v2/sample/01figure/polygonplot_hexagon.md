## タイトル（指定点と辺数による正多角形の描画）

### 想定質問

KeTCindyで、任意の点から始まる正多角形を描くにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setketcindyjs(["Color=0.9*[1,1,1]","Label=[]"]);

Addax(0);  // 座標軸の表示
Polygonplot("1",[A,B],6);  // 点A・Bをもとに6角形を描画（正六角形）
Windispg();
````

---

### 解説とラベル

このコードは、指定した2点 `[A,B]` を起点として、正六角形を描画する例です。
`Polygonplot("1",[A,B],6)` の3番目の引数で多角形の辺の数を指定します。

* `A` は多角形の中心
* `B` は頂点の一つとして使われ、半径の長さを決定します
* `"1"` は図形の識別子（任意）

このように、点Aと点Bの位置関係に基づいて、向きや大きさが決まる正多角形を柔軟に作成できます。

**ラベル（タグ）**
`Polygonplot`, `Addax`, `Windispg`, `regular_polygon`, `hexagon`, `geometry`, `2D`, `constructive_geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
