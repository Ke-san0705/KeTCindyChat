### 想定質問

図形をPDFとして正確なサイズで出力するには、KeTCindyでどのようにコードを書けばよいですか？

### コード（CindyScript）

```cindy
Ketinit();
Setparent(Cdyname()+"p");

Addax(0);
Listplot("1",[A,B,C,A],[]);
Circledata("2",[A,B,C]);
Letter([A,"sw","A",B,"se","B",C,"n2","C"]);

Figpdf();
Windispg();
```

### 解説

このコードは、三角形ABCとその外接円を描き、PDF出力のための正確なレイアウトを整える処理を含んでいます。`Setparent`と`Figpdf`の併用で、印刷用に整った図を生成します。

### 関数(KeTCindy)

`Ketinit`, `Setparent`, `Addax`, `Listplot`, `Circledata`, `Letter`, `Figpdf`, `Windispg`

### 関数(CindySqript)

なし

### その他

`triangle`, `circle`, `geometry`, `2D`, `label`, `pdf_output`
