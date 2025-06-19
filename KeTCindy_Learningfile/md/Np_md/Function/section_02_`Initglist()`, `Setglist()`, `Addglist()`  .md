# 平面の図形とグラフ  
## 設定・定義  
### 環境設定  
#### `Initglist()`, `Setglist()`, `Addglist()`  
`Initglist()`, `Setglist()`, `Addglist()`  
ketlib スロットで作られる描画データを描画リストに追加する。  
`Implicitplot`,`Hatchdata` など実行時間のかかるコマンドを figures スロットにおくと，その都度実行されてしまう。それを避けるため ketlib スロットにおいたときに用いる。  
【例】  
Initializationスロットに以下を追記する  
```  
Initglist(); // 描画データを初期化  
Implicitplot('1',fun,rng);//関数fun範囲rngの陰関数のグラフを描く  
Setglist(); //描画データをセット  
```  
以下はDrawスロットに書く。  
```  
Ketinit();   
Addglist();//Initializationスロットでセットした描画データをまとめて追加する  
```
