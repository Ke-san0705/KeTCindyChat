# 平面の図形とグラフ  
## 計算  
### マーキング  
#### `Inversefun(関数 , 範囲 , 値)`  
`Inversefun(関数 , 範囲 , 値)`  
関数の逆関数値を求める  
関数は文字列で，関数式もしくは定義された関数名とする。  
指定された範囲の中で逆関数値を求める。存在しない場合は一方の端点を戻り値とし，コンソールに「not found」と表示される。  
数式処理ではなく数値探索のアルゴリズムを使っているので，単調関数でない場合は範囲をできるだけ狭くとるとよい。値が複数ある場合は，小さいほうが返される。
