## タイトル（三角形と内接円の塗り分け）

### 想定質問

KeTCindyで三角形とその内接円を色分けして塗るにはどうしたらよいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Listplot("1",[A,B,C,A]);  // 三角形ABC
Circledata("1",[D,E]);    // 内接円（中心D、半径DE）

Shade(["sg1"],["Color=green"]);              // 三角形を緑で塗る
Shade(["cr1"],["Color=0.4*[1,1,0]"]);         // 円を紫寄りの色で塗る

Pointdata("1",D,["Size=4"]);                 // 中心点Dの強調表示
Letter([A,"sw","A"],B,"ne","B",C,"se","C",D,"se","I");  // 点のラベル
Windispg();
````

---

### 解説とラベル

このコードでは、三角形と内接円を別々の色で塗り分け、構造を視覚的に強調しています。

* `Shade(["sg1"],["Color=green"])`：三角形（Listplotの図形名）を緑に塗りつぶす
* `Shade(["cr1"],["Color=0.4*[1,1,0]"])`：内接円（Circledataの図形名）を半透明の紫で塗る（黄色×0.4）
* `Pointdata("1",D,["Size=4"])`：円の中心Dを強調表示
* `Letter([...])`：各頂点や中心にラベルを表示

色や透明度の調整によって、重なった図形も見やすく表現できます。

**ラベル（タグ）**
`Shade`, `Circledata`, `Listplot`, `Pointdata`, `Letter`, `incircle`, `triangle`, `fill_color`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
