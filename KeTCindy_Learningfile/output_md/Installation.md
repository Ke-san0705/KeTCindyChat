# Installation ドキュメント

## install-ketcindy.pdf

### Page 1

K TCindy インストール方法
E
NIT, Numazu College
2023 年9月20 日
1 KeTCindy のインストール
Windows1164ビット版(ビルド22621.2070)及びMicrosoftEdge(バージョン115.0.1901.188)
を利用しています。macOS の場合は、https://s-takato.github.io/ketcindyorg/indexj.html を参
照してください。(インストールするソフトは同じです。)
1.1 Cinderella のインストール
https://beta.cinderella.de/にアクセスし、Windows 64 Bit Installer をクリックしてダウ
ンロードしてください。
Windows 64 Bit Installer でインストールできない場合、Windows 32 Bit Installer を
利用してください。
図1 https://beta.cinderella.de/のダウンロードページ
ブラウザの環境によって「一般的にダウンロードされていません」のようなエラーが表示される
ことがありますが、エラーの上にカーソルを置き、三点リーダー (···) →詳細表示→保持すると押
して保存してください。
1

### Page 2

ダウンロードが完了したら、クリックして実行してください。
インストールプログラムが立ち上がったら、右下の次へを何度か押してインストールを進めてく
ださい。
セットアップ完了となったら終了を押してインストールを終了してください。
これでCinderella のインストールは完了です。
1.2 KeTTeX のインストール
https://github.com/ketpic/kettex/releases にアクセスし、
KeTTeX-windows-yyyymmdd.zip をダウンロードしてください。(yyyymmdd は日付を
表し、最新のものをダウンロードしてください）
ダウンロードが終わったら、クリックして開いてください。
2

### Page 3

エクスプローラが開くので、上側のすべて展開を選択してください。
ウィンドウが開いたら展開を押してください。
新しいエクスプローラが開いたら、画像の場所をクリックし１つ前のフォルダに戻ってください。
フォルダを一度クリックした後、右クリックしコピーしてください。
3

### Page 4

左のメニューからPCを選択し、末尾に(C:) のついたドライブを開いてください。
何もないところで右クリックし、貼り付けてください。貼り付けが完了したら、そのフォルダを
開いてください。
kettexinst をダブルクリックして実行してください。
続行するには何かキーを押してください... が表示されるまで待つ
(cid:19) (cid:16)
注意！
指定されたパスが見つかりませんと表示されるとエラーが発生したと思い終了してしまいた
くなるかもしれませんが、必ず続行するには何かキーを押してください... が表示されるまで
待ってください。
(cid:18) (cid:17)
続行するには何かキーを押してください... と表示されたら何かキーを押してください。
これでKeTTeX のインストールは完了です。
4

### Page 5

1.3 R のインストール
https://cran.r-project.org/にアクセスし、Download R for Windowsをクリックしたあと、
base →Download R-x.x.x for Windows をクリックしてダウンロードしてください。
ダウンロードが終わったら、クリックしてインストーラを実行してください。
言語選択が表示されるのでOK をクリックしてください。
次へを何度かクリックするとインストールが完了します。
1.4 SumatraPDF のインストール
https://www.sumatrapdfreader.org/download-free-pdf-viewerにアクセスし、SumatraPDF-
x.x.x-64-install.exe をダウンロードしてください。
インストールできない場合はSumatraPDF-x.x.x-install.exeをダウンロードしてください。
ダウンロードが終わったら、ダウンロードされたファイルを右クリックしてファイルを開くを選
択してください。
エクスプローラが開いたら、一度クリックで選択した後右クリックして、管理者として実行を選
択してください。
5

### Page 6

インストーラが開いたら、右下のオプションを選択してください。
すべてのユーザーに対してインストールにチェックを入れ、右下の SumatraPDF をインス
トールを選択してください。
これでSumatraPDF のインストールは完了です。
1.5 Maxima のインストール
https://sourceforge.net/projects/maxima/files/Maxima-Windows/にアクセスし、最新版(一
番上)のフォルダーを開き、maxima-x.xx.x-win64.exe をダウンロードしてください。
インストールできない場合はmaxima-x.xx.x-win32.exe をダウンロードしてください。
ダウンロードが終わったら、クリックしてインストーラを実行してください。
次へを何度かクリックすると、インストールが完了します。
これでMaxima のインストールは完了です。
6

### Page 7

1.6 GCC(GNU C Compiler) のインストール
https://sourceforge.net/projects/mingw/にアクセスし、緑のDownloadボタンを押してくだ
さい。ダウンロードが終わったら、そのファイルを開いてください。
ファイルが実行されたら、Install → Continue の順にクリックするとインストールが始まり
ます。
ダウンロードが終わったら、Continue をもう一度クリックしてください。
MinGW Installation Manager が開いたら、mingw-developer-toolkit, mingw32-base,
mingw32-gcc-g++, msys-base の4個にチェックを入れてください。
チェックは、項目左側の四角をクリックし、Mark for Installation をクリックすることで入
れることができます。
7

### Page 8

すべてのチェックが終わったら、左上の Installation から Apply Changes を選択してくだ
さい。
開いたウィンドウで Apply を選択することでパッケージがインストールされます。インストー
ルが終了したらClose を選択してください。
Windows キーを押し、環境変数と入力し、システム環境変数の編集を選択してください。
下側のPathを選択し、編集を選択してください。
新規を選択し、C:￥MinGW￥bin と入力し、Enter を押してください。
OK を押して閉じてください。
これでGCC のインストールは完了です。
8

### Page 9

1.7 KeTCindy のインストール
https://github.com/ketpic/ketcindy/releases にアクセスし、最新版の Source Code (zip)
を選択し、ダウンロードしてください。
ダウンロードが終わったら、KeTTeX のインストールで行ったのと同じようにファイルを展開
し、(C:) ドライブに貼り付けてください。
貼り付けできたら、貼り付けたフォルダを右クリックし、名前を変更を選択してください
ketcindy-x.x.xx のハイフンを消してEnter を押してください。
変更できたら、そのフォルダ→ doc フォルダの順に開き、ketcindysettings をダブルクリッ
クしてください。
左の黒文字で示されている部分が、language=j, tex=platex, graphics=pict2e になって
いることを確認してください。違う場合は上部の黄色ボタンを押して変更できます。
黄色のボタンをKettex →Mkinit →Update →Work の順にクリックしてください。
Work を選択するとコマンドプロンプトが開きます。数分たっても自動で閉じない場合はウィ
ンドウを選択してEnter を押してください。
(C:)のついたドライブの中にあるketcindyx.x.xxフォルダを開き、doc→work→templates
の順に開いてください。
9

### Page 10

その中の 01figure ファイルを開き、画像のような三角形が表示されたら KeTCindy のインス
トールは成功です。
この01figure ファイルをもとにして複製しながらプログラムなどを書いていきます。
2 追加情報
KeTCindyのリファレンスはhttps://s-takato.github.io/ketcindyorg/offline/KeTCindyReferenceJ.pdf
にあります。
10

