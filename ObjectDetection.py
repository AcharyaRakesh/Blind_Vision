import os
import cv2
import numpy as np
from imutils.video import VideoStream
from speech import speak
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
classes = []
box = []

font = cv2.FONT_HERSHEY_DUPLEX

with open("coco.names", "r") as f:
    classes = f.read().splitlines()


def take_Photo():
    vs = VideoStream(0).start()
    image = vs.read()
    height, width = image.shape[:2]
    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, image)
    frame = cv2.imread("opencv_frame.png")
    boxes = []
    confidenses = []
    class_ids = []
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    output_name = net.getUnconnectedOutLayersNames()
    layerOutput = net.forward(output_name)

    for output in layerOutput:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidense = scores[class_id]
            if confidense > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidenses.append((float(confidense)))
                class_ids.append(class_id)

    index = cv2.dnn.NMSBoxes(boxes, confidenses, 0.3, 0.2)
    if len(index) > 0:
        for i in index.flatten():
            label = str(classes[class_ids[i]])
            box.append(label)
        os.remove(img_name)
        string = ''.join(box)
        speak(string)


