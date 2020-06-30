import cv2
from os import makedirs

input_video_dir = '/home/neubility001/Data_set/steven/steven_cut.mp4'
output_frame_dir = '/home/neubility001/Data_set/steven/Frame/'

# Opens the Video file
cap = cv2.VideoCapture(input_video_dir)
cap.set(cv2.CAP_PROP_CONVERT_RGB, True)


length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
i = 0
count=0
dump_num = 116
#div_num = int(length/dump_num)
div_num = 2
images = []

try:
    makedirs(output_frame_dir)
    print("Directory ", output_frame_dir, " Created")
except FileExistsError:
    print("Directory ", output_frame_dir, " already exists")

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break
    if i%div_num==0:
        im_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        #Used to remove the time written over the image frame
        im_crop = im_bgr[:980, :1919]
        #Resize resolution
        im_resize = cv2.resize(im_crop, None, fx=0.5, fy=0.5)
        cv2.imwrite(output_frame_dir + 'extracted_frame_' + str(count) + '.jpg', im_resize)
        print("Wrote extracted_frame_"+str(count)+'.jpg'+"\n")
        count +=1
    i += 1
    
print("Total {} of frames are made".format(count))
cap.release()
cv2.destroyAllWindows()
