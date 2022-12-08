import urllib.request
import zipfile
import os 
def load_utils():
  with urllib.request.urlopen('https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip') as response:
    data = response.read()
  with open('ffmpeg.zip', 'wb') as f:
    print("Please wait while we download the required files...")
    f.write(data)  
  with zipfile.ZipFile('ffmpeg.zip', 'r') as zip:
    zip.extractall()
if os.path.exists('ffmpeg.zip'):
  os.remove('ffmpeg.zip')


  