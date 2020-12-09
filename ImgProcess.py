import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

target_dir = "./upload_img"

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。

#4.画像のグレースケール化（出来れば2値化も）

#watchdogを実装

class ChangeHandler(FileSystemEventHandler):
    #ファイル作成時のイベント
    def on_created(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
        #print("作成を検出")
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
        #print("移動を検出")
    #ファイル削除時のイベント
    def on_deleted(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #それぞれの処理後にあるファイルも削除
        #print("削除を検出")

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

