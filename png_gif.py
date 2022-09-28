import PIL.Image
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

#GUI画面で編集するフォルダパスを取得

def open_folder(path):
    subprocess.run('explorer {}'.format(path))
    
# フォルダ指定の関数
def dirdialog_clicked1():
    iDir = os.path.abspath(os.path.dirname('__file__'))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)
    
def dirdialog_clicked2():
    iDir = os.path.abspath(os.path.dirname('__file__'))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry2.set(iDirPath)

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""

    dirPath1 = entry1.get()
    dirPath2 = entry2.get()
    if dirPath1:
        text += "GIFの作成を完了しました,\n"
    if dirPath2:
        text += "GIFは" + dirPath2 + "に保存されました."
    if text:
        messagebox.showinfo("info", text)
        files = sorted(glob.glob(dirPath1 +'/*.png'))  
        images = list(map(lambda file : PIL.Image.open(file).convert("RGBA") , files))
　　　　　images[0].save('./image.gif',save_all = True ,format='GIF', append_images = images[1:] , duration = 300 ,transparency=255, loop = 0)
    else:
        messagebox.showerror("error", "パスの指定がありません.")

if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title("PNGファイルをGIFに変換します.")

    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="GIFに変換するフォルダを選択＞＞", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame1, text="参照", command=dirdialog_clicked1)
    IDirButton.pack(side=LEFT)
    
    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    # 「ファイル参照」ラベルの作成
    IFileLabel = ttk.Label(frame2, text="GIFの保存先を選択＞＞", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    # 「ファイル参照」エントリーの作成
    entry2 = StringVar()
    IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
    IFileEntry.pack(side=LEFT)

    # 「ファイル参照」ボタンの作成
    IFileButton = ttk.Button(frame2, text="参照", command=dirdialog_clicked2)
    IFileButton.pack(side=LEFT)

    
    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=5,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="実行", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame3, text=("キャンセル"), command=quit)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()
