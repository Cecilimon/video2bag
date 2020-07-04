from __future__ import print_function
import cv2
from os import makedirs
import re
from cv_bridge import CvBridge
import numpy as np
import time
import rosbag
from sensor_msgs.msg import Image
from glob import glob


def open_output_dir(path):
    try:
        makedirs(path)
        print("Directory ", path, " Created")
    except FileExistsError:
        print("Directory ", path, " already exists")

def open_bag_file(filename):
    try:
        bag = rosbag.Bag(file, 'w')
    except Exception as e:
        print(e)
    return bag


def write_bag(image, bagfile, sleep_rate=0.01):
    bridge = CvBridge()

    try:
        image_message = bridge.cv2_to_imgmsg(image, encoding="bgr8")
        bagfile.write('/camera/image',  image_message)
        time.sleep(sleep_rate)
    except Exception as e:
        print(e)

def extract_frame(input_path, output_dir, output_file):
    cap = cv2.VideoCapture(input_path)
    cap.set(cv2.CAP_PROP_CONVERT_RGB, True)

    open_output_dir(output_dir)
    bagfile = open_bag_file(output_file)

    i = 0
    count=0
    div_num = 2

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break
        if i%div_num==0:
            im_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # Used to remove the time written over the image frame
            # im_crop = im_bgr[:980, :1919]
            # Resize resolution
            im_resize = cv2.resize(im_bgr, None, fx=0.5, fy=0.5)
            # cv2.imwrite(output_dir + 'extracted_frame_' + str(count) + '.jpg', im_resize)
            write_bag(im_resize, bagfile)
            print("Wrote extracted_frame_"+str(count)+'.jpg'+"\n")
            count +=1
        i += 1
        
    print("Total {} of frames are made".format(count))
    cap.release()
    cv2.destroyAllWindows()
