# linux-nvr
This is a simple python script to use a Linux machine as an NVR. The code streams video from IP cameras in your network and splits the video into pre-determined segments (by default, 10 minute-long segments). The videos are stored in your local hard-drive. If you do not need any fancy GUIs, motion detection, etc., this is a simple tool to build your own NVR with cheap cameras purchased online. 

This is achieved using RTSP protocol, and the code calls [openRTSP](http://www.live555.com/openRTSP/). See prerequisites for openRTSP installation instructions.

## Usage:
`python record.py --camera camera1 --record-period 600`

*Please edit camera1's IP address in the code. Also, you might need to modify the RTSP command in `record.py` to match your camera's format. You can find that format from the camera's user manual. [This](https://www.ispyconnect.com/sources.aspx) webpage also has a comprehensive list of RTSP commands for many brands.*

## Deleting old videos
I use a `cron` job to delete old videos. You can find an example [here](https://askubuntu.com/questions/789602/auto-delete-files-older-than-7-days).

## Motivation
In theory, openRTSP should automatically perform streaming the video and splitting it into pre-determined chunks. In practice, I found out that RTSP connections drop and saved files are much longer than they should be, with frequent errors. The goal of this script is to run openRTSP only for relatively short periods of time (10 minutes each), and open a new stream every 10 minutes.

## Prerequisites
Follow the instructions below to install openRTSP (taken from [here](https://askubuntu.com/questions/693396/openrtsp-problem)):
* Run as root:

`sudo -i`
* Go to /usr/src:

`cd /usr/src`
* Get the live555 liveMedia source code:

`wget http://www.live555.com/liveMedia/public/live555-latest.tar.gz`
* Unpack it:

`tar -xzf live555-latest.tar.gz`
* Go into the directory that's just been unpacked:

`cd live`
* Generate the make files:

`./genMakefiles linux`
* Build the code:

`make`
* Install the new version:

`make install`
* Stop being root:

`exit`
