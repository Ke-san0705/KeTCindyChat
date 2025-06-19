# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Readcsv(path,filename,option)`  
`Readcsv(path,filename,option)`  
csv ファイルを読む。  
  
【例】以下のファイルを読み込む  
```csv  
1,2,3,4  
5,6,7,8  
```  
  
```  
Ketinit();  
a=Readcsv("path/to/your/file","example.csv");//第1引数のディレクトリにある第2引数のcsvファイルを読み込んで変数aに格納。(2次元配列)  
println(a);//変数aを表示  
Windispg();  
```  
この出力結果は以下のようになる  
```txt  
[[1,2,3,4],[5,6,7,8]]  
```
