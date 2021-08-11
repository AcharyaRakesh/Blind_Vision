# importing  Libraries
import cv2
import time
from speech import speak


def line_dis(image, m, n,label, distance,command):
    Line_Position2 = int(image.shape[1] * (50 / 100))
    cv2.line(image, pt1=(Line_Position2, 0), pt2=(Line_Position2, image.shape[0]), color=(255, 0, 0),
             thickness=2, lineType=8, shift=0)

    bounding_mid = (int(m), int(n))
    if (bounding_mid):
        #distance_from_line = Line_Position2 - bounding_mid[0]
        if label==command:
            if (m > 320):
                    step = (distance / 9)
                    step = round(step, 0)
                    speak(f"{label} at a distance{distance} on my right,and nearly {step} steps Forward from me")

            else:
                step = (distance / 9)
                step=round(step,0)
                speak(f"{label} at a distance{distance}on my left,and nearly {step} steps Forward from me")
        return

