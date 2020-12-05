# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
import cv2

# 監視対象ディレクトリを指定する
target_dir = 'static/upload_img/'

face_cascade_path = "templates/haarcascade_frontalface_default.xml"
window = "Push ESC key to stop this program"

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):
    # ファイル作成時のイベント
    def on_created(self, event):
        print('[作成]', event)
        filepath = event.src_path
        filename = os.path.basename(filepath)
        detect_face(filename)

    # ファイル変更時のイベント
    def on_modified(self, event):
        print('[変更]', event)
        filepath = event.src_path
        filename = os.path.basename(filepath)
        detect_face(filename)

def detect_face(img):
    image_path = 'static/upload_img/' + img
    print(image_path)
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



# コマンド実行の確認
if __name__ == "__main__":
    # ファイル監視の開始
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=True)
    observer.start()
    # 処理が終了しないようスリープを挟んで無限ループ
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
