import cv2
import numpy as np
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path

cascade_path="templates/haarcascade_frontalface_default.xml"
face_cascade_path = "templates/haarcascade_frontalface_default.xml"
window = "Push ESC key to stop this program"
target_dir = 'static/'

#1.顔を検出し、モザイク処理。
def mosaic_face(img):
    image_path = 'static/' + img
    output_path = "mosaic_img/mosaic_" + img

    mosaic_img = cv2.imread(image_path,cv2.IMREAD_COLOR)
    mosaic_gray = cv2.imread(image_path,0)  # cvtColorで変換するのでなくグレースケールで読み込むという手もある

    # mosaic_img.copy()でなくmosaic_imgそのものだとどうなるか確認してみよう
    img_rect = mosaic_img.copy()
    img_mosaic = mosaic_img.copy()

    cascade_path = "templates/haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    faces = cascade.detectMultiScale(mosaic_gray)

    if len(faces) > 0:
        for face in faces:
            x, y, w, h = face

            # 検出した顔の範囲を四角で囲む
            img_rect = cv2.rectangle(img_rect, (x, y), (x+w, y+h), color=(255, 255, 255), thickness=2)

            # 検出した顔の範囲をモザイクする
            roi = img_mosaic[y:y+h, x:x+w]
            roi = cv2.resize(roi, (w//10, h//10))
            roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
            img_mosaic[y:y+h, x:x+w] = roi               

    cv2.imwrite(output_path,img_mosaic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#2.顔を検出し、枠で囲う。
def detect_face(img):
    image_path = 'static/' + img
    output_path = "FaceFrame_img/frame_" + img

    frame_img = cv2.imread(image_path,cv2.IMREAD_COLOR)

    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(frame_img, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    #顔の数だけ処理
    if len(facerect) > 0:
        for rect in facerect:
            #矩形描画
            cv2.rectangle(frame_img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(255,255,255),3)
    cv2.imwrite(output_path, frame_img)

#3.Cannyフィルタによる輪郭抽出。
def cannyfilter(filename):
    image_path = 'static/' + filename
    output_path = "Canny_img/Canny_" + filename

    # 入力画像を読み込み
    cny_img = cv2.imread(image_path,cv2.IMREAD_COLOR)

    # グレースケール変換
    gray = cv2.cvtColor(cny_img, cv2.COLOR_RGB2GRAY)

    #Cannyフィルタで輪郭抽出
    cny_img = cv2.Canny(gray, 100, 200)
    
    # 結果を出力
    cv2.imwrite(output_path, cny_img)

#4.画像のグレースケール化（出来れば2値化も）
def grayscale(filename):

    image_path = 'static/' + filename
    output_path = "Gray_img/Gray_" + filename

    gray_img = cv2.imread(image_path,0)

    #画像の確認
    cv2.imwrite(output_path,gray_img)

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
            mosaic_face(filename)
            detect_face(filename)
            cannyfilter(filename)
            grayscale(filename)

    #ファイル変更時のイベント
    def on_modified(self,event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        #ここはそれぞれの処理の関数
        print("変更を検出")
        ext = os.path.splitext(filename)[1]
        if ext == ".png" or ext == ".jpeg" or ext == ".jpg":
            mosaic_face(filename)
            detect_face(filename)
            cannyfilter(filename)
            grayscale(filename)

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