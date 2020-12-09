import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。
def cannyfilter(filename):
    #カレントディレクトリの移動
    os.chdir("./upload_img")

    # 入力画像を読み込み
    cny_img = cv2.imread(filename)

    # グレースケール変換
    gray = cv2.cvtColor(cny_img, cv2.COLOR_RGB2GRAY)

    #Cannyフィルタで輪郭抽出
    cny_img = cv2.Canny(gray, 100, 200)

    #カレントディレクトリの移動
    os.chdir("../Canny_img")
    # 結果を出力
    cv2.imwrite(filename, cny_img)
    #カレントディレクトリの移動
    os.chdir("../")

#4.画像のグレースケール化（出来れば2値化も）
def grayscale(filename):
    #カレントディレクトリの移動
    os.chdir("./upload_img")
    gray_img = cv2.imread(filename,0)

    #カレントディレクトリの移動
    os.chdir("../Gray_img")

    #画像の確認
    cv2.imwrite(filename,gray_img)
    #カレントディレクトリの移動
    os.chdir("../") 

#watchdog実装

class ChangeHandler(FileSystemEventHandler):
    #ファイル作成時のイベント
    def on_created(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
        print("作成を検出")
        ext = os.path.splitext(filename)[1]
        if ext == ".png" or ext == ".jpeg" or ext == ".jpg":

    #ファイル変更時のイベント
    def on_modified(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
        print("変更を検出")
        ext = os.path.splitext(filename)[1]
        if ext == ".png" or ext == ".jpeg" or ext == ".jpg":

    #ファイル移動時のイベント
    def on_moved(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
        print("移動を検出")
    #ファイル削除時のイベント
    def on_deleted(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #それぞれの処理後にあるファイルも削除
        print("削除を検出")

if __name__ == "__main__":
    #ファイルの監視を開始
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()