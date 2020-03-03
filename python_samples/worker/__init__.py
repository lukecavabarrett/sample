import os

if os.path.exists('/tmp/worker_control_pipe_out'):
    comm_pipe = open('/tmp/worker_control_pipe_out', 'w')
else:
    comm_pipe = None
