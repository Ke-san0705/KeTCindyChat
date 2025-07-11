### 想定質問

三角形ABCと内接円、弓形補助線を使って特定の領域を条件に応じてドットで塗りつぶすKeTCindyコード例を教えてください。

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Listplot("1",[A,B,C,A]);
Circledata("1",[D,E]);
Bowdata("1",[B,A],1,0.5,"Expr=c","da");
Bowdata("2",[C,B],1,0.5,"Expr=a","da");
Bowdata("3",[A,C],1,0.5,"Expr=b","da");

Ch=[];
if(contains(Ch,1),
  Dotfilldata("1",["i"],[["cr1"]],[""])
);
if(contains(Ch,2),
  Dotfilldata("2",["oi"],[["cr1"],["sg1"]],[""])
);

Pointdata("1",D,["size=4"]);
Letter([A,"sw","A",B,"ne","B",C,"se","C",D,"se","I"]);

Windispg();
```

### 解説

このコードは、三角形ABCと内接円を中心に、3つの弓形を描画し、条件に応じて特定の領域にドットパターンで塗り分ける処理を行います。論理分岐`contains`により、描画領域が動的に変化します。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Listplot`, `Circledata`, `Bowdata`, `Dotfilldata`, `Pointdata`, `Letter`, `Windispg`

### 関数(CindySqript)

なし

### その他

`triangle`, `incircle`, `bowcurve`, `dotfill`, `conditional_fill`, `geometry`, `2D`, `visualization`
