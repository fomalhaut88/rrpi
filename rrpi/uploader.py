import os

import paramiko


class Uploader:
    def __init__(self, host, username='pi', password='raspberry', src_dir='.', trg_dir='/home/pi'):
        self._src_dir = src_dir
        self._trg_dir = trg_dir

        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(hostname=host, username=username, password=password, port=22)

        self._sftp = self._ssh.open_sftp()

    def __del__(self):
        self._sftp.close()
        self._ssh.close()

    def upload(self, data):
        for src, trg in data:
            src_path = os.path.join(self._src_dir, src)
            trg_path = os.path.join(self._trg_dir, trg)
            self._upload_entity(src_path, trg_path)

    def _upload_entity(self, src_path, trg_path):
        if os.path.isdir(src_path):
            try:
                self._sftp.chdir(trg_path)
            except IOError:
                self._sftp.mkdir(trg_path)

            for name in os.listdir(src_path):
                s_path = os.path.join(src_path, name)
                t_path = os.path.join(trg_path, name)
                self._upload_entity(s_path, t_path)

        else:
            self._sftp.put(src_path, trg_path)
