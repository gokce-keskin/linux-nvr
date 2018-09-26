'''
Simple recorder for cheap IP cameras using openRTSP
Usage:
    Record camera1's footage in 600 second chunks
    python record.py --camera camera1 --record-period 600
    
'''

import subprocess
import time
import os
import signal
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--camera", type=str, default="door",
                    help="Camera (camera1 or camera2)")
parser.add_argument("--record-period", type=int, default=600,
                    help="Output file size in seconds")
args = parser.parse_args()

common =' -4 -B 10000000 -b 10000000 -f 20 -w 1920 -h 1080 -t -V' 
if args.camera == "camera1":
    # modify the IP address below to your camera1's IP
    # RTSP path might be different for each camera brand
    # also, modify the username and password
    # default might be like admin:admin 
    end = 'rtsp://username:password@192.168.1.2:554/11'
elif args.camera == "camera2":
    end = 'rtsp://username:password@192.168.1.3:554/11'

common = common + ' -d %d ' % args.record_period
# Create the output directory
outdir = './%s/' % args.camera
os.system('mkdir -p %s' % outdir)

def return_filename():
    # Creates a filename with the start time
    # of recording in its name
    fl = time.ctime().replace(' ', '_')
    fl = fl.replace(':', '_')
    return fl

while True:
    filename = return_filename()
    outfile = './%s/%s.mp4' % (outdir, filename)
    # Create the openRTSP command and its parameters
    cmd = 'openRTSP ' + common + end 
    cmd = cmd.split(' ')
    cmd = [ix for ix in cmd if ix != '']

    st = time.time()
    with open(outfile,"wb") as outp:
        proc = subprocess.Popen(cmd, shell=False,
                                stdin=None, stdout=outp,
                                stderr=None, close_fds=True)
    time.sleep(args.record_period)
    # Send the termination signal
    print('Send termination signal')
    proc.send_signal(signal.SIGHUP)
    time.sleep(1)
    os.kill(proc.pid, signal.SIGTERM) 

    print('Elapsed %1.2f' % (time.time() - st))
