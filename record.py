
import cv2
from utils import manage_record_video
import time
import argparse




ap = argparse.ArgumentParser()

ap.add_argument("-ww", "--width", required=False,
                  help="video width", default=640)

ap.add_argument("-hh", "--height", required=False,
                  help="video heigth", default=480)

args = vars(ap.parse_args())

width = args["width"]
height = args["height"]


vs = cv2.VideoCapture(0, cv2.CAP_DSHOW)

vs.set(cv2.CAP_PROP_FRAME_WIDTH, int(width))
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height))

m_record_video = manage_record_video.manage_record_video()

duration = 0
interval = 1
last_durr = time.time()

print("start...")

while True:

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


	if ret:
		m_record_video.do_record_3(image, [])
	else:
		break


print("record saved")