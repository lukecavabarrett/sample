import json
import time

from python_samples import communication


def send_object(obj):
    communication.comm_pipe.write(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True))
    time.sleep(1)
    communication.comm_pipe.flush()
    communication.comm_pipe.write('\0')
    communication.comm_pipe.flush()


class checkpoint:
    def __init__(self):
        self.linked_files = []
    def save_to_server(self):
        self.request_type = 'save_checkpoint'
        send_object(self)

    def link_file(self,path):
        self.linked_files.append(path)
