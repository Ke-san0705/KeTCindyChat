## タイトル（三角形の内接円と弓型塗りつぶしの活用）

### 想定質問

三角形とその内接円に加えて、各辺から内接円に接する弓型部分を塗り分けるにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Listplot("1",[A,B,C,A]);      // 三角形ABCの描画
Circledata("1",[D,E]);        // 内接円（中心D, 半径DE）

// 各辺に対する弓型Bowdataの設定
Bowdata("1",[B,A],[1,0.5,"Expr=σ","da"]);
Bowdata("2",[C,B],[1,0.5,"Expr=β","da"]);
Bowdata("3",[A,C],[1,0.5,"Expr=α","da"]);

Ch=[];

// 条件付きで塗りつぶし
if(contains(Ch,1),
  Dotfilldata("1",["cr1"],[""]);
);

if(contains(Ch,2),
  Dotfilldata("2",["oi"],["cr1"],["sg1"]);
);

Pointdata("1",D,["size=4"]);  // 内心の表示
Letter([A,"sw","A"],B,"ne","B",C,"se","C",D,"se","I");  // ラベル表示

Windispg();
```

---

### 解説とラベル

このコードは、三角形の内接円と、その接点を使って描かれる弓型領域（Bowdata）を利用し、構造的な補助図として視覚的に理解を促す構成です。

* `Bowdata`：辺の上に半円状の構造を作る。内接円との接点と辺の端点を指定
* `Dotfilldata`：指定された図形領域を条件によって塗りつぶし
* `contains(Ch,...)` によって表示条件を柔軟に切り替え可能
* `Expr=α` 等で弧に文字を表示可能（ギリシャ文字も可）

この手法は、幾何的性質の視覚化、特に接円構造や角の成り立ちの補足に有効です。

---

### ラベル

`Listplot`, `Circledata`, `Bowdata`, `Dotfilldata`, `Pointdata`, `Letter`, `incircle`, `triangle`, `arc_fill`, `2D`, `geometry`
---
