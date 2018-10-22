import numpy as np
import tensorflow as tf
import cv2 as cv
import os
import argparse

from object_detection.utils import label_map_util

CWD_PATH = os.getcwd()
MODEL_NAME = 'export/'
PATH_TO_FROZEN_GRAPH = os.path.join(CWD_PATH,  MODEL_NAME, 'frozen_inference_graph.pb')
print('the model:', PATH_TO_FROZEN_GRAPH)

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(CWD_PATH, 'data/label.pbtxt')
# PATH_TO_LABELS = os.path.join(CWD_PATH, 'object_detection', 'data','ssd_mobilenet_v1_coco_2017_11_17.pbtxt')
# print(PATH_TO_LABELS)

cvNet = cv.dnn.readNetFromTensorflow(PATH_TO_FROZEN_GRAPH, PATH_TO_LABELS)


def do_work(image_path):
        # img = cv.imread('test_images/image1.jpg')
        img = cv.imread(image_path)
        rows = img.shape[0]
        cols = img.shape[1]
        cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        for detection in cvOut[0,0,:,:]:
                score = float(detection[2])
                if score > 0.3:
                        left = detection[3] * cols
                        top = detection[4] * rows
                        right = detection[5] * cols
                        bottom = detection[6] * rows
                        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

        cv.imshow('img', img)
        cv.waitKey()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Detect objects from an image')
        parser.add_argument('--image', metavar='path', required=True,
                        help='The image path')
        args = parser.parse_args()
        do_work(args.image)

