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
from . import utils_capture
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-audio', '-a', action='store_true' ,  help='Select only audio devices.')
parser.add_argument('-video', '-v', action='store_true', help='Select only video devices.')
parser.add_argument('-audio_video', '-av', action='store_true', help='Select only video devices.')
parser.add_argument('-alternative', '-alt', action='store_true', help='Show alternative names.')
parser.add_argument('-list_all', '-l', action='store_true' , help='Print the list of all devices.')
parser.add_argument('-save', '-s', action='store_true' ,  help='Save the results to a file.')
args = parser.parse_args()
only_video_json_object = []


contain_object = []

if not os.path.exists("ffmpeg-master-latest-win64-gpl-shared"):
    utils_capture.utils.load_utils()

ffmpeg_path = os.getcwd() + "/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
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

class Settings():
    """
    This class is used to set the parameters for the program.
        '-audio': "(audio)",
        '-a': "(audio)",
        '-video': "(video)",
        '-v': "(video)",
        '-audio_video': "(audio, video)",
        '-av': "(audio, video)",
        '-list_all': "list_all_b",
        '-l': "list_all_b",
        '-alternative': "alternative_b",
        '-alt': "alternative_b",
        '-save': "save_b",
    """
    def __init__(self,device_type = "", alt_name = False, save = False, list_all = False):
        self.device_type = device_type
        self.alt_name = alt_name
        self.save = save
        self.list_all = list_all




    ###or you can print the results.

def save():
    ###write the results to a file.
    with open('devices.txt',"w", encoding="utf-8") as output:
        output.write("###############################Device List##################################" + "\n")
        output.write("----------------------------------------------------------------------------" + "\n")
        for line in only_video_json_object:
            output.write(line + "\n")
    ###or you can print the results.

def print_all():
    print(only_video_json_object) 

def run_with_param(device_type = "", alt_name = False, save = False, list_all = False):
    set_obj = Settings(device_type = device_type, alt_name = alt_name, save = save, list_all = list_all)
    process(set_obj,None)

def process(obj,args):
        for x in json_object.split("\n"):
            try:
                if x.__contains__(f"{obj.device_type}"):
                    if re.findall(r'"([^"]*)"', x )[0].__contains__("@device") == False:
                        only_video_json_object.append("DEVICE NAME : " + re.findall(r'"([^"]*)"', x )[0] )
                        cont = True
                if cont == True: 
                    if (obj.alt_name == True or args.alternative == True) and re.findall(r'"([^"]*)"', x )[0].__contains__("@device") == True:
                        only_video_json_object.append("ALTERNATIVE NAME : " +  re.findall(r'"([^"]*)"', x )[0] + "\n")
                        cont = False
            except:
                continue
        if obj.list_all == True:
            print_all()
        if obj.save == True:
            save()
    
def run_with_args(args):
    contain_object = dict_args[[x for x in [args.audio,args.video,args.audio_video,args.list_all]].index(True)]
    setting_obj = Settings(device_type = contain_object, alt_name = False, save = False, list_all = False)
    process(setting_obj,args)
    if args.list_all != False:
        print(only_video_json_object)
    if args.save !=False:
        ###write the results to a file.
        with open('devices.txt',"w", encoding="utf-8") as output:
            output.write("###############################Device List##################################" + "\n")
            output.write("----------------------------------------------------------------------------" + "\n")
            for line in only_video_json_object:
                output.write(line + "\n")

if __name__ == "__main__":


    for arg in vars(args):
        if getattr(args,arg) == True:
            run_with_args(args)
            break
        else:
            pass

        

   
    
    
    
    