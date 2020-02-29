from . import utils

class checkpoint:
    def __init__(self):
        self.linked_files = []
    def save_to_server(self):
        self.request_type = 'save_checkpoint'
        utils.send_object(self)

    def link_file(self,path):
        self.linked_files.append(path)
