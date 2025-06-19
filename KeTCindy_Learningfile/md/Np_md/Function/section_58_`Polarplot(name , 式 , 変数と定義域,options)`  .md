# 平面の図形とグラフ  
## 描画  
### 関数のグラフ  
#### `Polarplot(name , 式 , 変数と定義域,options)`  
`Polarplot(name , 式 , 変数と定義域,options)`  
極座標表示 $$r = f(\theta)$$ の曲線を描く。  
  
【例】アルキメデスの螺旋を描く。  
```  
Ketinit();  
  
Polarplot("1","t/5","t=[0,6*pi]",["Num=2000"]);//r=t/5で表される極座標表示の曲線をtが0から6piまで描く。  
  
Windispg();  
```
