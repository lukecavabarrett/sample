import json
from . import comm_pipe

def send_object(obj):
    comm_pipe.write(json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True))
    comm_pipe.write('\0')
    comm_pipe.flush()
