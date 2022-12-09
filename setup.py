from setuptools import setup, find_packages

VERSION = '3.01' 
DESCRIPTION = 'Get list of Capture Devices easily with Directshow and Python'
LONG_DESCRIPTION = 'Simplest way to connect DirectShow Windows API with FFmpeg and list all capture devices with alternative names.\
    The user can save the results to a file or print either "video", "audio", or both "audio, video" devices. '


# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="capture_devices", 
        version=VERSION,
        author="Egemen Gulpinar",
        author_email="<egemengulpinar@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        license = 'MIT',
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['DirectShow', 'Windows','Capture Device','Device List','FFmpeg'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
            "Topic :: Software Development",
        ]
)