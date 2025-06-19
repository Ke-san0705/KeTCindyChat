# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `WriteOutData(ファイル名,PD リスト)`  
`WriteOutData(ファイル名,PD リスト)`  
外部データに書き出す  
  
【例】x^2のプロットデータを外部ファイルに書き込む  
```  
Ketinit();  
Plotdata("1","x^2","x",["Num=200"]);//x^2のグラフをプロットデータを作成する。  
WriteOutData("gr1.txt",["gr1"]);//gr1をgr1.txtに書き込む  
Windispg();  
```
