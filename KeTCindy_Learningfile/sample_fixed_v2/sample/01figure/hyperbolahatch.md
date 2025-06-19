## タイトル（双曲線の描画と領域のハッチング）

### 想定質問

KeTCindyで双曲線を描き、その開いた領域を斜線でハッチングするにはどうすればよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Hyperbolaplot("1",[A,B,C],"[-2,2]");

Ch=[1];

if(contains(Ch,1),
  Hatchdata("1",["ii1"],[["r1hyp1","w"],["r1hyp2","e"]],["Max=100"]);
);

if(contains(Ch,2),
  Hatchdata("1",["ii1"],[["r1hyp1","w"],["r1hyp2","e"]],["Max=100"]);
);

Windispg();
````

---

### 解説とラベル

このコードは、KeTCindyで双曲線の両腕を描き、その間の領域をハッチング（斜線塗り）する例です。

* `Hyperbolaplot`：指定した3点に基づいて双曲線を描画します。
* `"[-2,2]"`：描画するx軸方向の範囲を指定。
* `Hatchdata`：領域を構成する右腕と左腕（`r1hyp1`, `r1hyp2`）の間を斜線で塗りつぶします。
* `"Max=100"`：ハッチの密度（ライン数）を指定。

`contains(Ch,1)` や `Ptselected()` を使うことで、条件に応じた表示制御も可能です。

**ラベル（タグ）**
`Hyperbolaplot`, `Hatchdata`, `conic`, `hyperbola`, `hatching`, `region_fill`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
