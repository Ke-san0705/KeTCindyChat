### 想定質問

KeTSlideのタイトル表示を設定するコード例を教えて

---

### コード（CindyScript）

```cindy
Ketinit();
//Addpackage("qrcode");

Setslidebody("black",0);
//Setslidehyper("dvipdfmx",["cl=false,lc=blue,fc=blue"]);
Setslidehyper("");

Texcom("¥Large¥bf¥boldmath");
Titlesize("s");

Settitle([
  "s{67}{10}{KeTSlideの使い方}",
  "s{67}{40}{Setsuo Takato}",
  "s{67}{50}{KeTCindy Center}",
  "s{67}{60}{2024.12.23}"
],["Color=[0.98,0.13,0.0.43]"]);

Ch=[];
if(contains(Ch,0),
);

Windispg();
```

---

### 解説とラベル

このコードは、KeTSlideのタイトルスライドを作成するものです。

* `Settitle`：タイトルや著者情報などを段階的に配置。
* `Setslidebody`, `Setslidehyper`: スライド全体の外観設定。
* `Texcom`, `Titlesize`: タイトル用のテキストスタイル指定。
* `Anime`, `Flip`, `Title`, `Slide`, `Digest`のようなボタンを押すと同じフォルダ内に格納したスライドを確認できる。
---

### ラベル（関数KeTCindy）

`Ketinit`, `Setslidebody`, `Setslidehyper`, `Settitle`, `Texcom`, `Titlesize`, `Windispg`

---

### ラベル（関数CindyScript）

`contains`, `if`

---

### ラベル（その他）

`slide`, `title`, `presentation`, `KeTSlide`, `display`, `text layout`
