import os
import cv2
import time
import argparse
import multiprocessing
import numpy as np
import tensorflow as tf
# from matplotlib import pyplot as plt

# https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


CWD_PATH = os.getcwd()

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
PATH_TO_FROZEN_GRAPH = os.path.join(CWD_PATH,  MODEL_NAME, 'frozen_inference_graph.pb')
print(PATH_TO_FROZEN_GRAPH)

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(CWD_PATH, MODEL_NAME, 'graph.pbtxt')
print(PATH_TO_LABELS)

# Read the graph.
with tf.gfile.FastGFile(PATH_TO_FROZEN_GRAPH, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

with tf.Session() as sess:
    # Restore session
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')

    # Read and preprocess an image.
    img = cv2.imread('images/example1.jpg')
    rows = img.shape[0]
    cols = img.shape[1]
    inp = cv2.resize(img, (300, 300))
    inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

    # Run the model
    out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                    sess.graph.get_tensor_by_name('detection_scores:0'),
                    sess.graph.get_tensor_by_name('detection_boxes:0'),
                    sess.graph.get_tensor_by_name('detection_classes:0')],
                   feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})

    # Visualize detected bounding boxes.
    num_detections = int(out[0][0])
    for i in range(num_detections):
        classId = int(out[3][0][i])
        score = float(out[1][0][i])
        bbox = [float(v) for v in out[2][0][i]]
        if score > 0.3:
            x = bbox[1] * cols
            y = bbox[0] * rows
            right = bbox[3] * cols
            bottom = bbox[2] * rows
            cv2.rectangle(img, (int(x), int(y)), (int(right), int(bottom)), (125, 255, 51), thickness=2)

cv2.imshow('ssd_mobilenet_v1_coco_2017_11_17', img)
cv2.waitKey()