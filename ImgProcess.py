import cv2
import numpy as np

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。

# 入力画像を読み込み
cny_img = cv2.imread("ここはwatchdogで読み込んだファイル名")

# グレースケール変換
gray = cv2.cvtColor(cny_img, cv2.COLOR_RGB2GRAY)

#Cannyフィルタで輪郭抽出
cny_img = cv2.Canny(gray, 100, 200)

# 結果を出力
cv2.imwrite("Canny_img/ここはwatchdogで読み込んだファイル名", cny_img)

#4.画像のグレースケール化（出来れば2値化も）