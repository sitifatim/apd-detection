from ultralytics import YOLO
import cv2

from db.database import *
from db.model import *
from db.queries import *


model1 = YOLO(r'models\yolov8n.pt')
model2 =YOLO(r'models\predict1\weights\best.pt')

def image_detect():
    image = 'uploads/image.jpg'
    cap = cv2.VideoCapture(image)
    while cap.isOpened():
        succes, frame = cap.read()
        if succes:
            results = model1.predict(frame, conf=0.5, classes=0)
            for result in results:
                boxes = result.boxes.xyxy.to('cpu').numpy().astype(int)
                for box in boxes:
                    human_frame = frame[box[1]:box[3], box[0]:box[2]]
                    apd_results = model2.predict(human_frame, conf=0.5)
                    # print(apd_results[0])
                    for apd in apd_results:
                        boxes_apd = apd.boxes.xyxy.to('cpu').numpy().astype(int)
                        for ba in boxes_apd:
                            roi = human_frame[ba[1]:ba[3],ba[0]:ba[2]]
                            # cv2.imwrite("oke.jpg", roi)
                            screenshoot_image = cv2.imencode('.jpg', roi)[1].tobytes()
                            insert_image_detect(screenshoot_image, datetime.now())
                            cv2.rectangle(human_frame, (ba[0], ba[1]), (ba[2], ba[3]), (255,255,255), 2, lineType=cv2.LINE_AA)
    
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        else:
            break


def video_detect():
    image = 'uploads/video.mp4'
    cap = cv2.VideoCapture(image)
    while cap.isOpened():
        succes, frame = cap.read()
        if succes:
            results = model1.predict(frame, conf=0.5, classes=0)
            # print(results)
            for result in results:
                boxes = result.boxes.xyxy.to('cpu').numpy().astype(int)
                for box in boxes:
                    # cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (1,1,1), 2, lineType=cv2.LINE_AA)
                    human_frame = frame[box[1]:box[3], box[0]:box[2]]
                    apd_results = model2.predict(human_frame, conf=0.5)
                    for apd in apd_results:
                        boxes_apd = apd.boxes.xyxy.to('cpu').numpy().astype(int)
                        
                        for ba in boxes_apd:
                            roi = human_frame[ba[1]:ba[3],ba[0]:ba[2]]
                            screenshoot_image = cv2.imencode('.jpg', roi)[1].tobytes()
                            insert_image_detect(screenshoot_image, datetime.now())
                            
                            cv2.rectangle(human_frame, (ba[0], ba[1]), (ba[2], ba[3]), (255,255,255), 2, lineType=cv2.LINE_AA)
    
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        else:
            break
