## タイトル（三角形の内接円と弓型領域のハッチング）

### 想定質問

内接円と三角形の間の弓型領域を斜線でハッチングするにはどうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Listplot("1",[A,B,C,A]);       // 三角形の描画
Circledata("1",[D,E]);         // 内接円の描画

// 弓型の描画（各辺に対応）
Bowdata("1",[B,A],[1,0.5,"Expr=σ","da"]);
Bowdata("2",[C,B],[1,0.5,"Expr=β","da"]);
Bowdata("3",[A,C],[1,0.5,"Expr=α","da"]);

Pointdata("1",D,["size=4"]);   // 内心の強調表示
Letter([A,"sw","A"],B,"ne","B",C,"se","C",D,"se","I");  // ラベル

Ch=[1];

// 条件付きハッチング（点未選択時）
if(contains(Ch,1),
  if(!Ptselected(),
    Hatchdata("1",["cr1"],["dr,0.7"]);
  );
);

if(contains(Ch,2),
  if(!Ptselected(),
    Hatchdata("2",["oi"],["cr1","sg1"],["dr,0.7",""]);
  );
);

Windispg();
```

---

### 解説とラベル

このスクリプトは、三角形とその内接円、および接円との接点に基づく弓型領域を斜線で塗り分ける例です。

* `Bowdata`：三角形の辺上に半弧を描画し、視覚的な補助とします。
* `Hatchdata`：指定領域（例：`cr1`）を斜線（引数 `"dr,0.7"`）でハッチングします。
* `Ptselected()` により、点選択がなければ自動でハッチングが適用されます。
* 条件付き表示により、柔軟な視覚制御が可能です。

この技法は、内接円と接線の関係、三角形内部構造の強調など、幾何教材として非常に有効です。

### ラベル
`Bowdata`, `Hatchdata`, `Circledata`, `Listplot`, `Pointdata`, `Letter`, `incircle`, `triangle`, `hatching`, `arc_fill`, `2D`, `geometry`

---
