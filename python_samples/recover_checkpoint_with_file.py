import time, sys, os

from .worker import checkpoint

if not checkpoint.is_available():
    sys.stderr.write('borg checkpoints option not available\n')
else:
    sys.stderr.write('borg checkpoints option is available\n')
    ck = checkpoint.restore_checkpoint()
    if ck is None:
        sys.stderr.write('but no checkpoint already here\n')
        time.sleep(1)
        sys.stderr.write("I'll generate one, with a file\n")
        with open('greetings.txt', 'w') as f:
            f.write('Hello, world!\n')
            f.close()
        time.sleep(1)
        ck = checkpoint.checkpoint()
        ck.jack = 'sparrow'
        ck.link_file('greetings.txt')
        ck.save_to_server()
    else:
        sys.stderr.write('recovered checkpoint\n')
        print(ck.__dict__)
        time.sleep(1)
        sys.stderr.write('Jack is: '+ck.jack+'\n')
        if os.path.exists('greetings'):
            sys.stderr.write('found file!\n')
        else:
            sys.stderr.write('file is not here\n')


sys.stderr.flush()


