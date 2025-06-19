## タイトル（放物線・楕円・双曲線の切替描画）

### 想定質問

KeTCindyで放物線・楕円・双曲線の描画を選択式で切り替え表示したいのですが、どうすればいいですか？

---

### コード（CindyScript）

```cindy
Ketinit();
//Setfiles("");

Setketcindyjs(["Nolabel=all","Color=white"]);

// Put A,B,C on the screen
Ch=[chno];

if(contains(Ch,1),
  Setparent(Cdyname()+"fig1");
  Parabolaplot("1",[A,B,C],["-5,10"]);
);

if(contains(Ch,2),
  Setparent(Cdyname()+"fig2");
  Ellipseplot("1",[A,B,C],["0,2*pi"]);
);

if(contains(Ch,3),
  Setparent(Cdyname()+"fig3");
  Hyperbolaplot("1",[A,B,C],["Asy=da"]);
);

Figpdf();
Windispg();
````

---

### 解説とラベル

このコードでは、変数 `chno` の値に応じて次の3つの円錐曲線のいずれかを描画します：

* `Parabolaplot`：放物線（例：$y = ax^2$）
* `Ellipseplot`：楕円（例：$x^2/a^2 + y^2/b^2 = 1$）
* `Hyperbolaplot`：双曲線（例：$x^2/a^2 - y^2/b^2 = 1$）

それぞれ `Setparent` によりPDF出力用ファイル名も分岐し、自動保存対応となっています。点 A, B, C は各曲線を定義する3点です。

**ラベル（タグ）**
`Parabolaplot`, `Ellipseplot`, `Hyperbolaplot`, `Setparent`, `conic`, `plot_switch`, `interactive`, `geometry`, `2D`, `curve`

```
```


---

### ラベル

`KeTCindy`, `CindyScript`
