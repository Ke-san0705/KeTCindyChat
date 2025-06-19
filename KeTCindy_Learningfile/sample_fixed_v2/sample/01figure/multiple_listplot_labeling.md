## タイトル（複数の線分とラベルの描画）

### 想定質問

KeTCindyで複数の線分を描いて、点や線分に複数のラベルをつける方法を教えてください。

---

### コード（CindyScript）

```cindy
Ketinit();
Setketcindyjs(["Label=[]","Color=offwhite"]);  // デフォルト設定の初期化

Addax(0);  // 座標軸表示

Listplot("1",[A,B,C,A]);  // 三角形ABC
Listplot("2",[C,D]);      // 辺CD
Listplot("3",[A,E]);      // 辺AE

Letter([F,"n-3w5","G"]);  // G点に文字Gを少しずらして表示
Letter([A,"sw","A"],B,"se","B",C,"n2","C");  // ABCのラベル
Letter([D,"s","M"],E,"ne","N");              // D→M, E→Nのラベル
Windispg();
````

---

### 解説とラベル

このコードは、三角形と補助線を複数描き、それぞれの点に位置調整されたラベルを付けた図形を表示します。

* `Setketcindyjs(["Label=[]","Color=offwhite"])`：KeTCindyJS向けの描画オプション（ラベルと背景色）を初期化
* `Listplot("1",[A,B,C,A])`：三角形ABCの描画
* `Listplot("2",[C,D])`, `Listplot("3",[A,E])`：補助線の追加
* `Letter([...])`：点に対してラベルを個別に付与。例えば `"n2"` は上側、`"sw"` は左下などの位置指定

これにより、補助点を含めた複雑な図形を視覚的に整理できます。

**ラベル（タグ）**
`Setketcindyjs`, `Addax`, `Listplot`, `Letter`, `multi_segment`, `labeling`, `geometry`, `2D`, `triangle`, `auxiliary_lines`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
