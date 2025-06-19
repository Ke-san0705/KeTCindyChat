# 平面の図形とグラフ  
## 計算  
### マーキング  
#### `integrate(関数式 , 変数 = 範囲 , options),integrate(PD , 範囲 , options)`  
`integrate(関数式 , 変数 = 範囲 , options),integrate(PD , 範囲 , options)`  
関数式またはプロットデータで与えられた関数（データ）の数値積分の値を求める。  
  
 options は次の通り。  
”Rule=s”：シンプソン法による。 初期設定は大島ベジェ公式。  
”Num=数値”：分割数の指定。初期値は 100
