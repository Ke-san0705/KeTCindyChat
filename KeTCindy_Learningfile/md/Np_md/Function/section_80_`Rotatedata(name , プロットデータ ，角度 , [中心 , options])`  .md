# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Rotatedata(name , プロットデータ ，角度 , [中心 , options])`  
`Rotatedata(name , プロットデータ ，角度 , [中心 , options])`  
プロットデータの位置を回転する  
図形を，中心で示された点の周りに回転する。角度は弧度法で与える  
中心と options はまとめてリストで与える。  
  
【例】y=sin x のグラフを 90度回転する  
```  
Ketinit();  
  
Plotdata("1","sin (x)","x",["Num=200","nodisp"]);//y=sin xのグラフを描く。"nodisp"オプションによってCinderellaの画面上には出力しない  
  
Rotatedata("1","gr1",pi/2,[[0,0]]);//gr1を点(0,0)に対してpi/2(90度)回転させる  
  
Windispg();  
```
