# openRTSP-recorder
This is a simple python script that converts your Linux based machine to an NVR. The code streams video from IP cameras in your network and splits the video into pretermined segments (by default, 10 minute-long segments). This is achieved using RTSP protocol, and the code calls openRTSP (http://www.live555.com/openRTSP/). See prerequisites for openRTSP installation instructions.

## Usage:
`python record.py --camera camera1 --record-period 600`

*Please edit camera1's IP address in the code.*

## Motivation
In theory, openRTSP should automatically perform streaming the video and splitting it into predetermined chunks. In practice, I found out that RTSP connections drop and saved files are much longer than they should be, with frequent errors. The goal of this script is to run openRTSP only for relatively short periods of time (10 minutes each), and open a new stream every 10 minutes.

## Prerequisites
Install openRTSP as below (from https://askubuntu.com/questions/693396/openrtsp-problem)
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
*Stop being root:

`exit`
