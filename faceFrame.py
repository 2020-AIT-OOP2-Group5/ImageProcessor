# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time
import cv2

# 監視対象ディレクトリを指定する
target_dir = 'static/upload_img/'

cascade_path="templates/haarcascade_frontalface_default.xml"
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
    print(facerect)

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
