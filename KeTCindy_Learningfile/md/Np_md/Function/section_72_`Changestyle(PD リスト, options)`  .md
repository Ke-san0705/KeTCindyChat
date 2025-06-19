# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Changestyle(PD リスト, options)`  
`Changestyle(PD リスト, options)`  
描画オプションを変更する  
複数の図形の描画オプションを一括して変更する。  
  
```  
Ketinit();  
opgr=["dr,3"];//変更用にオプションをリストで保存  
Plotdata("1","x^3+2*x^2+2*x+1","x",["Num=200"]);  
Changestyle(["gr1"],opgr);//オプションを保存したリストをoptionsに渡してgr1に反映させる  
  
Windispg();  
```
