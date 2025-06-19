# 平面の図形とグラフ  
## その他  
### マーキング  
#### `Animationkey([番号リスト, 横位置リスト, 縦位置])`  
`Animationkey([番号リスト, 横位置リスト, 縦位置])`  
アニメーションの PLAY,REV,PAUSE,STOP を作成  
すでにある場合は位置を設定  
オプションのデフォルト値は，[71,72,73,74],[-4,-2,0,2],-6  
  
【例】  
```  
Ketinit();  
Setketcindyjs(["Label=[]","Color=offwhite","Figure=y"]);  
Animationkey();//Animationkeyを作成  
ss=Animationparam(0,2,2*pi);//ssをアニメーション用変数として設定。変域は0から2piで速度は2  
  
Plotdata("1","sin(x)","x=[0,"+text(ss)+"]",["Num=200"]);  
  
Windispg();  
```
