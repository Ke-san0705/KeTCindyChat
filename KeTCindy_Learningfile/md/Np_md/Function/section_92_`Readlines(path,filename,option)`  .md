# 平面の図形とグラフ  
## プロットデータの操作  
### マーキング  
#### `Readlines(path,filename,option)`  
`Readlines(path,filename,option)`  
テキストファイルを 1 行ずつ読む。  
  
【例】以下のファイルを読み込む  
```txt  
abcde  
fghij  
```  
  
```  
Ketinit();  
a=Readlines("path/to/your/file","example.txt");//第1引数のディレクトリにある第2引数のファイルを読み込んで変数aに格納。(配列)  
println(a);  
Windispg();  
```  
この出力結果は以下のようになる  
```txt  
[abcde,fghij]  
```
