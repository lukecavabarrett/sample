import time, sys

from .worker import checkpoint

if not checkpoint.is_available():
    sys.stderr.write('borg checkpoints option not available\n')
else:
    sys.stderr.write('borg checkpoints option is available\n')

sys.stderr.flush()

time.sleep(1)

ck = checkpoint.checkpoint()
ck.jack = 'sparrow'
ck.save_to_server()

time.sleep(1)
