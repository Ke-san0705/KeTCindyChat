# 平面の図形とグラフ  
## その他  
### マーキング  
#### `Sla2fra(文字列)`  
`Sla2fra(文字列)`  
文字列の中の / を簡易 TeX-like 書式の分数に直す。  
  
【例】  
```  
Ketinit();  
println(Sla2fra(("(4+pi)/3")));//(4+pi)/3を簡易 TeX-like 書式の分数に変換する  
  
Windispg();  
```  
  
# KeTCindy3D  
## 概要  
KeTCindy3Dの描画は次のように構成される.  
  
Cinderellaの画面に白の短径で囲んだ領域が2つできる.  
NE, SWを対角とする左側の領域を主画面, 右側の領域を副画面という.  
  
主画面は平面の場合と同様, $$\TeX$$に出力される範囲を示し,  
NE, SWの2点をドラッグすることにより変更できる.  
主画面の下方のスライダーで視点が移動でき,  
主画面上では軸が回転する.  
副画面はx, y平面上に視点を置いたものと考えればよい.  
  
主画面上にCinderellaの作図ツールで点や線分を作図すると,  
副画面に対応する点が作図される.  
主画面上の点をドラッグするとx, y座標を変更でき,  
副画面上の点をドラッグするとz座標を変更できる.  
  
KeTCindy3Dでは, 線や面についての陰線処理を行う.  
陰線処理はC言語との連携により処理を速めている  
(C言語を使う環境整備が必要であるが, 現在はこれを標準としている).  
  
## 設定
