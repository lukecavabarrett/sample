import json
from . import comm_pipe, utils
import os


def is_available():
    return comm_pipe is not None


class checkpoint:
    def __init__(self):
        self.linked_files = []

    def save_to_server(self):
        self.request_type = 'save_checkpoint'
        utils.send_object(self)

    def link_file(self, path):
        self.linked_files.append(path)


def restore_checkpoint():
    if not os.path.exists('/tmp/worker_checkpoint/checkpoint.json'):
        return None
    with open('/tmp/worker_checkpoint/checkpoint.json') as json_file:
        ck = checkpoint()
        for key, value in json.load(json_file).items():
            setattr(ck, key, value)
        return ck
# Checkpoint available: {'best_epoch': 340, 'best_epoch_loss': 0.019209275022149086, 'last_epoch': 749, 'linked_files': ['340.pkl', '749.pkl'], 'request_type': 'save_checkpoint'}
