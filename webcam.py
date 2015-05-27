#!/usr/bin/env python

#webcam - a simple as fuck webcam viewer 
#v1.0 
#by Erik Perillo

VERSION = "1.1"

import cv2
import sys
import oarg2 as oarg

#command line parameters descriptors
frame_rate     = oarg.Oarg(int,"-f --frame-rate",24,"Frame rate to be used")
cam_ind        = oarg.Oarg(int,"-i --cam-index",0,"Index of webcam to be used") 
win_size_descr = oarg.Oarg(int,"-s --win-size",0,"Window size of image (in format width height)")
output         = oarg.Oarg(str,"-o --file-output","","File to save output")
helpmsg        = oarg.Oarg(bool,"-h --help",False,"This help message")

#parsing args
if oarg.parse() != 0:
     print "error: invalid options passed:",oarg.Oarg.invalid_options
     exit()

#setting window size
if len(win_size_descr.vals) < 2:
     win_size = 2*(win_size_descr.val,)
else:
     win_size = (win_size_descr.getVal(0),win_size_descr.getVal(1))

#checking if frame must be resized:
resize = (win_size != (0,0))

#help message
if helpmsg.val:
     print "webcam: a simple as fuck webcam viewer - version",VERSION
     print "by Erik Perillo"
     print "Avaliable command line options are:"
     oarg.describeArgs()
     exit()

#opening video capture device
cap = cv2.VideoCapture()
cap.open(cam_ind.val)

#creating named window
cv2.namedWindow("video",cv2.WINDOW_AUTOSIZE)

# Define the codec and create VideoWriter object
if output.found:
     fourcc = cv2.cv.CV_FOURCC(*'MJPG')
     out = cv2.VideoWriter(output.val,fourcc, 20.0, (640,480))

#main loop
while True:
     ret, frame = cap.read()
     if frame != None and cv2.waitKey(1000/frame_rate.val) & 0xFF != 27:
          if resize:
               frame = cv2.resize(frame,win_size)
          cv2.imshow("video",frame)
          if output.found:
               out.write(frame)
     else:
          break

#closing capture
cap.release()
if output.found:
     out.release()
