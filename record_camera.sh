#!/bin/sh
port=540$1
overlay="$2 - RECORDING"
gst-launch -e -v udpsrc port=$port ! application/x-rtp,payload=96,width=640,height=480 ! rtph264depay \
    tee name=t ! queue ! decodebin ! textoverlay text="$overlay" color=4294901760 ! clockoverlay ! xvimagesink sync=false \
    t. ! queue ! filesink location="~/Desktop/$3.h264"
