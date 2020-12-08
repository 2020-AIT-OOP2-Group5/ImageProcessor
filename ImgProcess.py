import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。
def cannyfilter(str filename):
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