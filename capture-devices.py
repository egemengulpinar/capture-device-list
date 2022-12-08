########################################
##                                    ##
##      Author : Egemen Gulpinar      ##
##  Mail : egemengulpinar@gmail.com   ##
##     github.com/egemengulpinar      ##
##                                    ##
########################################

import subprocess
import json
import re
import os
import argparse
from utils import load_utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-list', '-l', action='store_true' , default =True , help='Print the list of all devices.')
parser.add_argument('-audio', '-a', action='store_true' ,  help='Select only audio devices.')
parser.add_argument('-video', '-v', action='store_true', help='Select only video devices.')
parser.add_argument('-save', '-s', action='store_true' ,  help='Save the results to a file.')
args = parser.parse_args()


if not os.path.exists("ffmpeg-master-latest-win64-gpl-shared"):
    load_utils()

ffmpeg_path = os.getcwd() + "/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
only_video_json_object =[]
proc = subprocess.Popen([f'{ffmpeg_path}', '-stats', '-hide_banner','-list_devices', 'true', '-f', 'dshow', '-i', 'dummy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
json_object = json.dumps(stderr.decode("UTF-8"))
json_object = json.loads(json_object)

dict_args= {
    
    0: "(audio, video)",
    1: "(audio)",
    2: "(video)",
}

contain_object = dict_args[[x for x in [args.a1,args.a2,args.a3]].index(True)]
only_video_json_object = str([x for x in json_object.split("\n") if x.__contains__(contain_object)])
re_json_object = re.findall(r'"([^"]*)"', only_video_json_object)
res = [x for x in re_json_object if not x.__contains__("@device")]
if res == [] and args.audio == False:
    only_video_json_object = str([x for x in json_object.split("\n") if x.__contains__("(video)")])
    re_json_object = re.findall(r'"([^"]*)"', only_video_json_object)
    res = [x for x in re_json_object if not x.__contains__("@device")]

if args.list != False:
    print(res)
elif args.save !=False:
    ###write the results to a file.
    with open('devices.txt',"w", encoding="utf-8") as output:
        output.write("Device List" + "\n")
        for line in res:
            output.write(line + "\n")
    ###or you can print the results.
else:
    print("Please use -h to see the help menu")
