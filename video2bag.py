import cv2
import re
from cv_bridge import CvBridge
import numpy as np
import time
import rosbag
from sensor_msgs.msg import Image
from glob import glob

SLEEP_RATE = 0.01
images = []
bridge = CvBridge()
bag = rosbag.Bag('image.bag', 'w')

print("Frame read start")
filenames = glob("Frame/*.jpg")
filenames.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

try:
    print("Bag write start")
    for i in range(len(filenames)):
        print("Wrote {} index image\n".format(i))
        image = cv2.imread(filenames[i])
        image_message = bridge.cv2_to_imgmsg(image, encoding="bgr8")
        bag.write('/camera/image',  image_message)
        time.sleep(SLEEP_RATE)
    
finally:
    print("Done!")
    bag.close()
