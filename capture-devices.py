import subprocess
import json
import re
import os
import argparse
from utils import load_utils
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-list', '-l', type=str, help='Print the list of devices.')
parser.add_argument('-save', '-s', type=str, help='Save the results to a file.')
args = parser.parse_args()


if not os.path.exists("ffmpeg-master-latest-win64-gpl-shared"):
    load_utils()

ffmpeg_path = os.getcwd() + "/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
only_video_json_object =[]
proc = subprocess.Popen([f'{ffmpeg_path}', '-stats', '-hide_banner','-list_devices', 'true', '-f', 'dshow', '-i', 'dummy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
json_object = json.dumps(stderr.decode("UTF-8"))
json_object = json.loads(json_object)
only_video_json_object = str([x for x in json_object.split("\n") if x.__contains__("(audio, video)")])
re_json_object = re.findall(r'"([^"]*)"', only_video_json_object)
res = [x for x in re_json_object if not x.__contains__("@device")]
if res == []:
    only_video_json_object = str([x for x in json_object.split("\n") if x.__contains__("(video)")])
    re_json_object = re.findall(r'"([^"]*)"', only_video_json_object)
    res = [x for x in re_json_object if not x.__contains__("@device")]

if args.list != None:
    print(res)
elif args.save !=None:
    ###write the results to a file.
    with open('devices.txt',"w", encoding="utf-8") as output:
        output.write("Device List" + "\n")
        for line in res:
            output.write(line + "\n")
    ###or you can print the results.
else:
    print("Please use -h to see the help menu")
