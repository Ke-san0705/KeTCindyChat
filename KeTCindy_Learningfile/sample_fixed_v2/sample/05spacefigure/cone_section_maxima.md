### 想定質問

Maximaで円錐と平面の交線を解析し、KeTCindyで可視化するにはどうすれば良いですか？

---

### コード（CindyScript）

```cindy
Start3d([A,B,C,D]);

Putaxes3d(5.5);
//Xyzax3data("","x=[-4,4]","y=[-4,4]","z=[-2,6]");

Listplot("sa",[[-6,6],[-6,0]],["color->[0,0,1]"]);
Putonseg("A","sgsa");
Putonseg("B","sgsa");
C.xy=[-10,0];

Listplot([C,D],["color->[0,0,1]"]);
angle=re(arctan2(D-C));
drawtext(D+[0,0.2],text(angle*180/pi),align->"left");

ptA=[0,0,A.y];
ptB=[|D-C|*cos(angle),|D-C|*sin(angle),B.y];

fd=[
"z=2.5*(2-R))",
"x=R*cos(T)","y=R*sin(T)",
"R=[0,2]","T=[0,2*pi]","e"
];

cmdL=[
 "n:[n1,n2,n3]",[],
 "b:[-n[2],n[1],0]",[],
 "c1:n[2]*b[3]-n[3]*b[2]",[],
 "c2:n[3]*b[1]-n[1]*b[3]",[],
 "c3:n[1]*b[2]-n[2]*b[1]",[],
 "c:[c1,c2,c3]",[],
 "nb:sqrt(b.b)",[],
 "nc:sqrt(expand(c.c))",[],
 "p:[0,0,zA]+r*cos(T)*b/nb+r*sin(T)*c/nc",[],
 "eq:x^2+y^2-(k-z/hgt)^2",[],
 "eq2:ev(eq,[x=p[1],y=p[2],z=p[3]])",[],
 "sol:solve(eq2=0,r)",[],
 "p1:ev(p,sol[1])",[],
 "p2:ev(p,sol[2])",[],
 "nv:[diff(eq,x),diff(eq,y),diff(eq,z)]",[],
 "p1::p2::nv::eq2",[]
];
CalcbyM("base",cmdL,[""]);
nv=ptB-ptA;
Spaceline("AB",[ptA,ptB],["color->[1,0,0]"]);
Arrowhead(Parapt(ptB),Parapt(ptB)-Parapt(ptA),
    ["color->[1,0,0]"]);
crv=Assign(base_1,
    ["zA",ptA_3,"k",2,"hgt",2.5,"n1",nv_1,"n2",nv_2,"n3",nv_3]);
clr=[1,0,0];
clrc=Colorrgb2cmyk(clr);
//  Setcolor(clrc);
Spacecurve("1",crv,"T=[0,2*pi]",["nodisp","color->"+clr]);
//  Setcolor(black);
  Fontsize("s");
  Expr([-2,5.3],"c",nv_1+"x+"+nv_2+"y+"+nv_3+"(z-2)=0");
  Expr(Parapt([0,0,5]),"ne","5");
  Expr(Parapt([2,0,0]),"w","2");
  Fontsize("n");

Ch=[1,2];
if(contains(Ch,1),
 nvec=Assign(base_3,["zA",ptA_3,"k",2,"hgt",2.5]);
 tmp=Sileq(nvec);
 cmdL=[
  "x:R*c",[],
  "y:R*s",[],
  "z:2.5*(2-R)",[],
  "eq:"+tmp,[],
  "eq:expand(eq)",[],
  "eq:expand(eq/r)",[],
  "sol:solve([eq=0,s^2+c^2=1],[s,c])",[],
  "ans1:ev([x,y,z],sol[1])",[],
  "ans2:ev([x,y,z],sol[2])",[],
  "ans1::ans2",[]
 ];
 CalcbyM("ans",cmdL,[""]);

 pvec=[sin(THETA)*cos(PHI),sin(THETA)*sin(PHI),cos(THETA)];
 tmp=Assign(ans_1,["p1",pvec_1,"p2",pvec_2,"p3",pvec_3]);
 Spacecurve("s1",tmp,"R=[0,2]");
 tmp=Assign(ans_2,["p1",pvec_1,"p2",pvec_2,"p3",pvec_3]);
 Spacecurve("s2",tmp,"R=[0,2]");
);
if(contains(Ch,2),
 Spacecurve("cr","2*[cos(T),sin(T),0]","T=[0,2*pi]",
   ["Num=100"]);
 Divnohidhid("1","sc3dcr",nvec);
 tmp2=select(sc3d1,#_3>=0 & #_3<=5);
 tmp1=select(1..(length(tmp2)-1),
 norm(tmp2_(#+1)-tmp2_#)>1);
 if(length(tmp1)==0,
   Spaceline("1n1",tmp2);
   Divnohidhid("1n1","sl3d1n1",nvec);
 ,
   tmp3=[tmp2_(1..tmp1_1)];
   n1=tmp1_1+1;
   forall(2..(length(tmp1)),
     n2=#;
     tmp3=append(tmp3,tmp2_(n1..n2));
     n1=n2;
   );
   tmp3=append(tmp3,tmp2_(n1..(length(tmp2))));
   forall(1..length(tmp3),
     Spaceline("1n"+text(#),tmp3_#);
     Divnohidhid("1n"+text(#),"sl3d1n"+text(#),nvec);
   );
  );
 //Crvsfparadata("1","ax3d","sfbd3d1",fd,["r"],["do"]);
);
if(contains(Ch,3),
  Sf3data("1",fd);
);

Windispg();

//Help("Divno");

```

---

### 解説とラベル

このスクリプトは、**Maximaと連携して3次元空間における円錐と平面の交線を求め、KeTCindyで可視化する**例です。

* `Start3d()`：3D空間の初期化
* `Xyzax3data(...)`：空間の軸範囲を定義
* `Putonseg3d(...)`：点やベクトルの定義（図形の構成要素）
* `Spacecurve(...)`：Maximaから得た交線の式を描画
* `Divnohidden(...)`：交線の可視性処理
* `Assign`, `clacbyM`, `Parapt`, `Arrowhead`：KeTCindyとMaximaを連携させるための関数群

このような処理は、**立体図形の交差問題・ベクトル解析・関数空間の可視化**に有効です。

---

### ラベル（タグ）

`Start3d`, `Putaxes3d`, `Xyzax3data`, `Putonseg3d`, `Listplot`, `drawtext`, `Assign`, `Parapt`, `Spacecurve`, `Divnohidden`, `Arrowhead`, `Maxima`, `cone`, `plane`, `intersection`, `symbolic computation`, `3D`, `geometry`, `KeTCindy`, `解析幾何`, `CindyScript`, `立体交線`
