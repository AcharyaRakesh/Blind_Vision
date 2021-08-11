from speech_to_text import STT
import cv2
from imutils.video import VideoStream
from speech import speak
from New import main
from ObjectDetection import take_Photo
import os
from vqa import test_model
from threading import Thread
import time
stt = STT()


def Obj_command():

    with open("coco.names", "r") as f:
        classes = f.read().splitlines()
    voice = stt.speech_to_text()

    def CLASSES():
        for i in classes:
            if i in voice:
                print(i)
                return i
            else:
                return None
    to_check =CLASSES()

    if to_check is not None:
        DIR = None
        POS = "pos"
        main(DIR, POS, to_check)

    elif voice is None:
        speak('Please say the command again')

    elif "moving" in voice:
        DIR = "dir"
        POS = None
        main(DIR, POS, voice)

    elif "what" in voice:
        take_Photo()

    elif "object" in voice:
        take_Photo()

    elif "status" in voice:
        DIR = "dir"
        POS = None
        main(POS, DIR, voice)
    else:
        speak('Please say the command again')








class Compute(Thread):
    def __init__(self, answer):
        Thread.__init__(self)
        self.answer = answer

    def run(self):
        time.sleep(1)
        print(self.answer)
        speak(self.answer)


def vqa_command():
    vs = VideoStream(0).start()
    image = vs.read()
    image_path = "opencv_frame.png"
    cv2.imwrite(image_path, image)

    question = stt.speech_to_text()
    question_input = [f"<start> {question} <end>"]
    ans = test_model(image_path, question_input)
    ans = ans[0]
    for i in ["<start>", "<end>"]:
        ans = ans.replace(i, "")
    answer = f"The Answer is {ans}"
    thread_a = Compute(answer)
    thread_a.start()
    os.remove(image_path)


