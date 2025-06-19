## タイトル（手入力座標の正誤判定とプロット）

### 想定質問

KeTCindyで生徒が入力した座標が関数グラフ上にあるかを自動で判定し、正解なら点を表示したいです。どうすればできますか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setparent(Cdyname()+"fig");

Setketcindyjs(["Grid=0.5","Nolabel=all","Color=offwhite"]);
Seteditable("0",["x=","Size=18","Width=100"]);
Seteditable("1",["y=","Size=18","Width=100"]);

Setwindow([-4.5,4.5],[-0.5,10.5]);
Drawgrid([-4,4],[0,10]);

Expr([[1,YMAX],"ne","y=x^2",["size->20"]]);

if(drawgraph,
  Plotdata("qg","x^2","x",["Color=blue"]);
);

str1="x=2";  // 入力例
str2="y=4";

tmp1=Strsplit(str1,"=");
tmp2=Strsplit(str2,"=");

if((length(tmp1)>1)&&(length(tmp2)>1),
  tmp1=Tocindyform(tmp1_2);
  tmp2=Tocindyform(tmp2_2);
  x=parse(tmp1);
  y=parse(tmp2);

  if(y==x^2,
    Expr([[6,0.5],"e","Good!",["Size=1.5","Color=red"]]);
    plotL=append(plotL,[x,y]);
  ,
    Expr([[6,0.5],"e","Tray again.",["Size=1.5","Color=red"]]);
  );
);

if(length(plotL)>0,
  Pointdata("1",plotL,["Size=3","Color=red","Msg="]);
);

//Figpdf();
Windispg();
````

---

### 解説とラベル

このコードは、関数 $y = x^2$ に対して、ユーザーが手入力した $(x, y)$ 座標がグラフ上にあるかどうかをチェックし、正解なら赤い点でプロットします。

* `Seteditable(...)`：入力ボックスを表示
* `Strsplit` → `Tocindyform` → `parse`：文字列として入力された座標を式として処理
* `if(y==x^2)`：入力値が関数を満たしているかどうかを判定
* `Expr(...)`："Good!" や "Try again." の表示でフィードバック
* `Pointdata`：正解座標はリストに蓄積して表示

生徒のインタラクティブな入力確認や反復練習などに応用可能です。

**ラベル（タグ）**
`Seteditable`, `Expr`, `parse`, `Pointdata`, `Plotdata`, `input_check`, `function_graph`, `math_quiz`, `interactive`, `2D`, `geometry`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
