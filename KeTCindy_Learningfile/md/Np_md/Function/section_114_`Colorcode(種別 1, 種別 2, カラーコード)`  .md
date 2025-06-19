# 平面の図形とグラフ  
## その他  
### マーキング  
#### `Colorcode(種別 1, 種別 2, カラーコード)`  
`Colorcode(種別 1, 種別 2, カラーコード)`  
種別 1 から種別 2 へカラーコードを変換する。戻り値は変換されたコード。  
種別は，"rgb","cmyk","hsv"のいずれか。  
【例】変換例  
```  
Ketinit();  
col=Colorcode("rgb","cmyk",[1,0,0]);//RGBをCMYKに変換  
println(col);  
col=Colorcode("cmyk","rgb",[0,1,1,0]);//CMYKをRGBに変換  
println(col);  
col=Colorcode("rgb","hsv",[1,0,0]);//RGBをHSVに変換  
println(col);  
Windispg();  
```
