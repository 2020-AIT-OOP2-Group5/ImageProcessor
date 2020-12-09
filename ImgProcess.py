import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。

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