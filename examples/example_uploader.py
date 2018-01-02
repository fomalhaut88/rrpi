from rrpi.uploader import Uploader

HOST = '192.168.1.9'
DATA = [
    ('test1.py', 'test1/test1.py'),
]

Uploader(HOST, trg_dir='/home/pi/Dev').upload(DATA)
