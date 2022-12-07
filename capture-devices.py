import subprocess
import json
import re

only_video_json_object =[]
proc = subprocess.Popen(['ffmpeg', '-stats', '-hide_banner','-list_devices', 'true', '-f', 'dshow', '-i', 'dummy'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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

###write the results to a file.
with open('output_devices.txt',"w", encoding="utf-8") as output:
    output.write("Windows" + "\n")
    for line in res:
        output.write(line + "\n")
###or you can print the results.
print(res)