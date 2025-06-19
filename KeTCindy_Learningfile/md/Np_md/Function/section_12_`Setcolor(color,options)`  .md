# 平面の図形とグラフ  
## 設定・定義  
### 描画設定・定義  
#### `Setcolor(color,options)`  
`Setcolor(color,options)`  
描画色の設定  
引数 color はカラーコードまたは色の名称。  
カラーコードは RGB または CMYK をリストで与える。各色０～１。  
色の名称はカラーコード一覧 の 68 色が指定できる。  
```  
Ketinit();  
  
C.xy=|B.xy|/|C.xy|*C.xy;  
Listplot([B,A,C]);  
Setcolor("red");//描画色のデフォルトを赤色にする。ここより下ではSetcolorが再度実行されるまで赤色で描画される。  
Anglemark("1",[B,A,C],[3]);   
Arrowhead(C,"ag1",1);  
Setcolor("black");  
  
Windispg();  
```  
  
**座標軸を描く場合は，このあと `Setcolor("black")` で黒に戻しておかないと，座標軸が赤で表示されてしまうので要注意。**
