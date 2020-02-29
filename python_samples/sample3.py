import time, sys

from python_samples.communication import communication

sys.stdout.write('stdout: started process')
sys.stdout.flush()

time.sleep(1)

with open('hello.txt', 'w') as f:
    f.write("Hello, world!")
    f.write("This file was generated by a sample3.py")
    f.write("At time "+str(time.time()))
    f.close()

ck = communication.checkpoint()
ck.link_file('hello.txt')
ck.last_epoch = 45
ck.best_epoch = 34
ck.model = 'PNA'
ck.save_to_server()

time.sleep(1)
sys.stdout.write('stdout: finished process')
sys.stdout.flush()
exit(42)
communication.comm_pipe.close()
