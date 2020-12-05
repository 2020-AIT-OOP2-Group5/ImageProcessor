import cv2
import time
from  import MyFileSelector

cascade_path="templates/haarcascade_frontalface_default.xml"
window = "Push ESC key to stop this program"

def detect_face(img):
    img_prefix = img[0:-4]
    img_name = "FaceFrame_img/" +  img_prefix + "_faceframe.jpg"

    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    #顔の数だけ処理
    if len(facerect) > 0:
        for rect in facerect:
            #矩形描画
            cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]),(255,255,255),3)
    cv2.imshow(window, img)
    print(facerect)
    cv2.imwrite(img_name,img)
    

if(__name__ == '__main__'):

    img = cv2.imread('static/ARASHI2.jpg')

    #顔検出
    detect_face(img)
    time.sleep(0.050)
    cv2.destroyAllWindows()