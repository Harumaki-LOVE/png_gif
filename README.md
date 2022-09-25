# PNGファイル → GIF結合プログラム
## プログラムの説明・概要
指定フォルダのpngファイルからgifを作成し，指定フォルダに保存します.  
GUI画面から変換するフォルダの選択，GIFの保存フォルダの選択が可能です. 
## 動作環境
Windows 11 Home  
Python 3.9.13
## インストールが必要なモジュール
Pillow 9.2.0 　
## 使い方
1. pyファイルをダブルクリック，またはコマンドプロンプトからpyファイルの保存先に移動し $ Python3 png_gif.pyを実行
2. 表示されたGUI画面から，gifに変換するフォルダ, 出力されるgifの保存先を選択
3. 出力完了のメッセージとgifの保存先が表示されます.
## 注意
・pngファイルの結合の順番はファイル名を昇順にソートした順番になります. 
・GIFの切り替え速度はデフォルトでは400msです。変更する場合は
images[0].save(dirPath2+'/image.gif',save_all = True , append_images = images[1:] , duration = 400 ,disposal=2, loop = 0)のdurationを変更します. 
