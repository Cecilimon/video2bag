import cv2

# Opens the Video file
cap = cv2.VideoCapture('/home/neubility001/Data_set/steven/steven_cut.mp4')
cap.set(cv2.CAP_PROP_CONVERT_RGB, True)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
i = 0
count=0
dump_num = 116
#div_num = int(length/dump_num)
div_num = 2
images = []

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break
    if i%div_num==0:
        im_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        im_crop = im_bgr[:980, :1919]
        im_resize = cv2.resize(im_crop, None, fx=0.5, fy=0.5)
        cv2.imwrite('/home/neubility001/Data_set/steven/Frame/steve_frame_' + str(count) + '.jpg', im_resize)
        print("Wrote steve_frame_"+str(count)+'.jpg'+"\n")
        count +=1
    i += 1
print("Total {} of frames are made".format(count))
cap.release()
cv2.destroyAllWindows()
