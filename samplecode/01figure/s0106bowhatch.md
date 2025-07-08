### 想定質問

三角形ABCに内接円と弓形を描き、条件に応じて特定の領域を斜線でハッチングするKeTCindyコード例を教えてください。

### コード（CindyScript）

```cindy
Ketinit();

Addax(0);

Listplot("1",[A,B,C,A]);
Circledata("1",[D,E]);
Bowdata("1",[B,A],1.0,0.5,"Expr=c","da");
Bowdata("2",[C,B],1.0,0.5,"Expr=a","da");
Bowdata("3",[A,C],1.0,0.5,"Expr=b","da");

Pointdata("1",D,["size=4"]);
Letter([A,"sw","A",B,"ne","B",C,"se","C",D,"se","I"]);

Ch=[1];
if(contains(Ch,1),
  if(!Ptselected(),
    Hatchdata("1",["i"],[["cr1"]],["dr,0.7"]);
  );
);
if(contains(Ch,2),
  if(!Ptselected(),
    Hatchdata("2",["oi"],[["cr1"],["sg1"]],["dr,0.7",""]);
  );
);

Windispg();
```

### 解説

このコードは、三角形ABCの内接円と3辺にまたがる弓形補助線を描いた上で、条件に応じて斜線（ハッチ）で領域を塗りつぶす処理を行います。`Hatchdata`関数を用いたハッチングによって、重なりや領域の違いを視覚的に強調できます。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Listplot`, `Circledata`, `Bowdata`, `Pointdata`, `Letter`, `Hatchdata`, `Windispg`

### 関数(CindySqript)

なし

### その他

`triangle`, `incircle`, `bowcurve`, `hatch`, `geometry`, `2D`, `conditional_fill`, `region_visualization`
