# KeTCindy3D  
## 設定  
### マーキング  
#### `Ketinit3d()`  
`Ketinit3d()`  
KeTCindy3Dの使用宣言.  
Cinderellaの画面を3Dモードにする.  
  
Cinderellaの画面に視点移動のための2つのスライドを作る.  
スライダーは初期位置が左端になる.  
スライダーTHで角THETAを, スライダーFIで角PHIを内部変数として定義する.  
引数に0を入れて`Ketinit3d(0)`とすると, 副画面を表示しない.  
  
**この関数はInitializationスロットに置く.**  
**`Ketinit()`も平面の場合と異なりInitializationスロットに置く.**  
KeTCindy3Dにおける変数の初期化などを行う`Start3d()`はDrawスロットに書く.
