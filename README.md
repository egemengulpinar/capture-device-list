
# capture-device-list
[![Build status](https://img.shields.io/travis/Pythonity/icon-font-to-png.svg)][egemen]
[![Latest PyPI version](https://img.shields.io/pypi/v/django-icons.svg)](https://pypi.org/project/capture-devices/)


Simplest way to connect DirectShow Windows API with FFmpeg and list all capture devices with alternative names. The user can save the results to a file or print either “video”, “audio”, or both “audio, video” devices.


## Screenshots
![ss2](https://github.com/egemengulpinar/capture-device-list/blob/main/pic2.jpg)


## Setting Options

| Parameter              | Values   | Description    | Type  
| ----------------- | -------------- | ---------|--------
| device_type | `'audio' , 'video', 'audio_video'` |  Device Type  |str
| alt_name | `True , False` |  Show alternative name   | bool
| result_ |    `True , False`                | Return result |bool 
|  list_all |     `True , False`                  |Show all devices |bool
| save       |    `True , False` |Save result to text |bool 



## Setting Arguments

| Description              | Values     
| ----------------- | ---- |   
| Only audio devices | `'-audio', '-a'` | 
|  Only video devices | `'-video', '-v'` |  
| Only audio and video devices |    `'-audio_video', '-av'`               
|  Show alternative names |     `'-alternative', '-alt'`                 
| Show all devices       |    `'-list_all', '-l'` |
| Save to text       |    `'-save', '-s'` |

## Build

To build this project, follow these commands

```bash
  git clone https://github.com/egemengulpinar/capture-device-list.git
  cd capture-device-list
  python setup.py sdist bdist_wheel
```

  
## Usage with Arguments 

First clone the repo and go to directory. After, based on arguments table, follow the syntax below.

```bash 
  python capture_devices.py -list_all -save
  # or
  python capture_devices.py -audio -alternative -save
  
```


## Usage with pip

First install the packages using with pip

```bash 
  pip install capture-devices
```
After, you can import package similarly:
```python
from capture_devices import devices
```
For using this library, follow these structure:
```python
result = devices.run_with_param(device_type='audio', alt_name=True,result_= True)
print(result)

# or 

devices.run_with_param(alt_name=True,list_all=True)
```

    
## License

[MIT](https://github.com/egemengulpinar/capture-device-list/blob/main/LICENSE)



[pypi]: https://pypi.org/project/capture-devices/
[egemen]: https://pypi.org/project/capture-devices/
  
