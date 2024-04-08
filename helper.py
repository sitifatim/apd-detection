from ultralytics import YOLO
import cv2


model1 = YOLO('models/yolov8n.pt')
model2 =YOLO('models/predict1/weights/best.pt')

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
                    for apd in apd_results:
                        boxes_apd = apd.boxes.xyxy.to('cpu').numpy().astype(int)
                        if len(boxes_apd) == 1:
                            for ba in boxes_apd:
                                roi = human_frame[ba[1]:ba[3],ba[0]:ba[2]]
                                cv2.rectangle(frame, (ba[0], ba[1]), (ba[2], ba[3]), (255,255,255), 2, lineType=cv2.LINE_AA)
    
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
                    human_frame = frame[box[1]:box[3], box[0]:box[2]]
                    apd_results = model2.predict(human_frame, conf=0.5)
                    for apd in apd_results:
                        boxes_apd = apd.boxes.xyxy.to('cpu').numpy().astype(int)
                        if len(boxes_apd) == 1:
                            for ba in boxes_apd:
                                roi = human_frame[ba[1]:ba[3],ba[0]:ba[2]]
                                cv2.rectangle(frame, (ba[0], ba[1]), (ba[2], ba[3]), (255,255,255), 2, lineType=cv2.LINE_AA)
    
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        else:
            break
