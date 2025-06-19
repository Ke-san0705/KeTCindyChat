# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Extractdata(データ名, 属性)`  
`Extractdata(データ名, 属性)`  
`ReadOutData()` で読み込んだデータに属性をつける。  
  
【例】`WriteOutData`の説明で書き出したファイルを読み込んで`dr,2`属性をつける  
```  
Ketinit();  
ReadOutData("gr1.txt");  
Extractdata("gr1",["dr,2"]);  
  
Windispg();  
```  
  
## 計算
