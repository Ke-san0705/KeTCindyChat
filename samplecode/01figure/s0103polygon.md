### 想定質問

2点を基準に正六角形を描画するには、KeTCindyでどのようなコードを書けばよいですか？

### コード（CindyScript）

```cindy
Ketinit();
//Setketcindyjs(["Color=0.9*[1,1,1]","Label=[]"]);

Addax(0);
Polygonplot("1",[A,B],6);
Windispg();
```

### 解説

このコードは、点Aと点Bを基準に、正六角形（6辺の正多角形）を描くものです。関数`Polygonplot`により、2点間を1辺とした正多角形が自動生成され、座標軸も併せて表示されます。

### 関数(KeTCindy)

`Ketinit`, `Addax`, `Polygonplot`, `Windispg`

### 関数(CindySqript)

なし

### その他

`polygon`, `hexagon`, `geometry`, `2D`, `regular_polygon`, `construction`
