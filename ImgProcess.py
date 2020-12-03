import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

target_dir = "upload_img"

target_file = ["*.png","*.jpeg","*.jpg"]

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。

#4.画像のグレースケール化（出来れば2値化も）
img = cv2.imread("sourse.jpg",0)

#閾値の自動設定
img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

#画像の確認
cv2.imwrite("after_sourse.jpg",img_otsu)


#watchdogを実装

class　CheckHandler(FileSystemEventHandler):
    #ファイル作成時のイベント
    def on_created(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
    
    #ファイル変更時のイベント
    def on_modified(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
    
    #ファイル移動時のイベント
    def on_moved(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数

    #ファイル削除時のイベント
    def on_deleted(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #それぞれの処理後にあるファイルも削除


if__name__ == "__main__":
    #ファイルの監視を開始
    event_handler = CheckHandler([target_file])
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

