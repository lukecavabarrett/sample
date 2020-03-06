import os

if os.path.exists('/tmp/__hydra_control_pipe_out'):
    comm_pipe = open('/tmp/__hydra_control_pipe_out', 'w')
else:
    comm_pipe = None
