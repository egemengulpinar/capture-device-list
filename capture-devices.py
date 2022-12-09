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

parser.add_argument('-audio', '-a', action='store_true' ,  help='Select only audio devices.')
parser.add_argument('-video', '-v', action='store_true', help='Select only video devices.')
parser.add_argument('-audio_video', '-av', action='store_true', help='Select only video devices.')
parser.add_argument('-alternative', '-alt', action='store_true', help='Show alternative names.')
parser.add_argument('-list_all', '-l', action='store_true' , default =True , help='Print the list of all devices.')
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
    
    
    0: "(audio)",
    1: "(video)",
    2: "(audio, video)",
    3: ""
}
print([x for x in [args.audio,args.video,args.audio_video,args.list_all]])
contain_object = dict_args[[x for x in [args.audio,args.video,args.audio_video,args.list_all]].index(True)]

print(contain_object)

for x in json_object.split("\n"):
    try:
        if x.__contains__(f"{contain_object}"):
            print("-->", re.findall(r'"([^"]*)"', x )[0].__contains__("@device"))
            if re.findall(r'"([^"]*)"', x )[0].__contains__("@device") == False:
                only_video_json_object.append("DEVICE NAME : " + re.findall(r'"([^"]*)"', x )[0] )
                cont = True
        if cont == True: 
            if args.alternative == True and re.findall(r'"([^"]*)"', x )[0].__contains__("@device") == True:
                only_video_json_object.append("ALTERNATIVE NAME : " +  re.findall(r'"([^"]*)"', x )[0] + "\n")
                cont = False
    except:
        continue
#re_json_object = re.findall(r'"([^"]*)"', str(only_video_json_object))
#print(only_video_json_object)

if args.list_all != False:
    print(only_video_json_object)
if args.save !=False:
    ###write the results to a file.
    with open('devices.txt',"w", encoding="utf-8") as output:
        output.write("###############################Device List##################################" + "\n")
        output.write("----------------------------------------------------------------------------" + "\n")
        for line in only_video_json_object:
            output.write(line + "\n")
    ###or you can print the results.
else:
    print("Please use -h to see the help menu")
