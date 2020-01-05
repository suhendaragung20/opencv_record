
import cv2
from utils import manage_record_video
import time
import argparse




ap = argparse.ArgumentParser()

ap.add_argument("-ww", "--width", required=False,
                  help="video width", default=640)

ap.add_argument("-hh", "--height", required=False,
                  help="video heigth", default=480)

ap.add_argument("-ss", "--show", required=False,
                  help="show", default=1)

args = vars(ap.parse_args())

width = args["width"]
height = args["height"]

vs = cv2.VideoCapture(0)
#vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#vs.set(cv2.CAP_PROP_FRAME_WIDTH, int(width))
#vs.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height))

m_record_video = manage_record_video.manage_record_video()

duration = 0
interval = 1
last_durr = time.time()

print("start...")

while True:

	tic = time.time()
	
	ret, image = vs.read()

	m_record_video.init_video_2(image)


	# Press any key to close the image
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):

	    break

	if time.time() - last_durr > interval:
		last_durr = time.time()
		duration += interval
		print("duration " + str(duration))
	toc = time.time()
		
	if int(args["show"]) == 1: 
		frame_rate_calc = 1/(toc-tic)
		cv2.putText(image,'FPS: {0:.2f}'.format(frame_rate_calc),(30,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)
		cv2.imshow('record', image)

	if ret:
		m_record_video.do_record_3(image, [])
	else:
		break


print("record saved")
