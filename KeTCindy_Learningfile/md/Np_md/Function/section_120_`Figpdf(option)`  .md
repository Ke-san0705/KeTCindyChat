# 平面の図形とグラフ  
## その他  
### マーキング  
#### `Figpdf(option)`  
`Figpdf(option)`  
出力枠サイズの PDF を作る。  
```  
Ketinit();  
  
Listplot("1",[A,B,C,A],["dr,2"]);  
Setparent("test.pdf");  
Figpdf();  
Windispg();  
```  
ここで、Parentボタンを押すと、test.pdfが生成される。
