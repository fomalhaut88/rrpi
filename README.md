# rrpi

**rrpi** is a python frameworks that helps to interact with your raspberry pi device.
It includes the manage of GPIO, connection through UDP, uploading data by SFTP, etc.
It works with Python 3 strictly.


## Installation

Execute following command on your device:

```
sudo pip3 install -U git+https://github.com/fomalhaut88/rrpi.git
```

If everything is fine, this command won't raise an import error:

```
python3 -c "import rrpi"
```


## Simple example

An example of a blinking light connected via GPIO:

```python
from time import sleep
from rrpi import gpio


gpio.set_bcm_mode()

light = gpio.PinOut(17)

val = True
while True:
    light.set(val)
    val = not val
    sleep(1.0)
```


## Uploading data

If you need to upload your python program to your device, or some other data files, do it easily with rrpi uploader:

```python
from rrpi.uploader import Uploader

HOST = '192.168.1.9'
DATA = [
    ('test1.py', 'test1/test1.py'),
]

Uploader(HOST, trg_dir='/home/pi/Dev').upload(DATA)
```
