import time, sys

from .worker import checkpoint

if not checkpoint.is_available():
    sys.stderr.write('borg checkpoints option not available\n')
else:
    sys.stderr.write('borg checkpoints option is available\n')
    ck = checkpoint.restore_checkpoint()
    if ck is None:
        sys.stderr.write('but no checkpoint already here\n')
        time.sleep(1)
        sys.stderr.write("I'll generate one\n")
        time.sleep(1)
        ck = checkpoint.checkpoint()
        ck.jack = 'sparrow'
        ck.save_to_server()
    else:
        sys.stderr.write('recovered checkpoint\n')
        time.sleep(1)
        sys.stderr.write('Jack is: '+ck.jack+'\n')

sys.stderr.flush()


