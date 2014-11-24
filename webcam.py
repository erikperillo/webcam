#!/usr/bin/env python

#webcam - a simple as fuck webcam viewer 
#v1.0 
#by Erik Perillo

VERSION = "1.0"

import cv2
import sys
sys.path.insert(1,"/home/erik/prog/py/clarg/")
import clarg

#command line arguments container
container = clarg.Container()
#command line parameters descriptors
delay_desc     = clarg.Clarg("-td",20,"Time delay in milliseconds between frame captures")
cam_ind_desc   = clarg.Clarg("-ci",0,"Index of webcam to be used") 
win_size_desc  = clarg.Clarg("-ws",(0,0),"Window size of image in a tuple (width,height)",2)
helpmsg_desc   = clarg.Clarg("-h",False,"This help message",0)

#delay from one capture to another
delay     = int(container.parse(delay_desc))
cam_ind   = int(container.parse(cam_ind_desc))
win_size  = tuple( int(i) for i in container.parse(win_size_desc))
helpmsg   = bool(container.parse(helpmsg_desc))

#checking if frame must be resized:
if win_size == (0,0):
	resize = False
else:
	resize = True

#help message
if helpmsg:
	print "webcam: a simple as fuck webcam viewer - version",VERSION
	print "by Erik Perillo"
	print "Avaliable command line options are:"
	container.describe()
	exit()

#opening video capture device
cap = cv2.VideoCapture()
cap.open(cam_ind)

#creating named window
cv2.namedWindow("video",cv2.WINDOW_AUTOSIZE)

#main loop
while True:
	ret, frame = cap.read()
	if frame is not None and cv2.waitKey(delay) & 0xFF != 27:
		if resize:
			frame = cv2.resize(frame,win_size)
		cv2.imshow("video",frame)
	else:
		break

#closing capture
cap.release()
