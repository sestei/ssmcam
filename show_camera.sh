#!/bin/sh
port=540$1
gst-launch -e -v udpsrc port=$port ! application/x-rtp,payload=96,width=640,height=480 ! rtph264depay ! decodebin ! textoverlay text="$2" ! clockoverlay ! xvimagesink sync=false
