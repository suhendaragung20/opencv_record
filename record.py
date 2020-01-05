
import cv2
from utils import manage_record_video
import time



vs = cv2.VideoCapture(0)
m_record_video = manage_record_video.manage_record_video()

duration = 0
interval = 1
last_durr = time.time()

print("start...")

while True:

	ret, image = vs.read()

	m_record_video.init_video(image)
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