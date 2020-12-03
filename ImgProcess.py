import cv2
import numpy as np

#1.顔を検出し、モザイク処理。

#2.顔を検出し、枠で囲う。

#3.Cannyフィルタによる輪郭抽出。

#4.画像のグレースケール化（出来れば2値化も）
img = cv2.imread("sourse.jpg",0)

#閾値の自動設定
img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

#画像の確認
cv2.imwrite("after_sourse.jpg",img_otsu)