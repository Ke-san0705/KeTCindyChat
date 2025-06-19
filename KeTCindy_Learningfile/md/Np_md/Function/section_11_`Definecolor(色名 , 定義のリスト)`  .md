# 平面の図形とグラフ  
## 設定・定義  
### 描画設定・定義  
#### `Definecolor(色名 , 定義のリスト)`  
`Definecolor(色名 , 定義のリスト)`  
色名を定義する  
ユーザー命名の色名を定義する。定義リストは RGB または CMYK のリスト  
各色０〜１の範囲で指定する。定義した色名は，`Setcolor(color,options)` で使うことができる。  
なお，KETCindy では，68 色を色名で使うことができる。色の名称はカラーコード一覧参照。  
【例】暗い紫色を darkmaz の名称で定義して使う。  
```  
Definecolor("darkmaz",[0.8,0,0.8]);//(R,G,B)=(0.8,0,0.8)の色をdarkmazとして定義  
Setcolor("darkmaz");//darkmaz色をsetcolorする  
```
