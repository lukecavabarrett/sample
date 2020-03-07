import time, sys, numpy as np, pickle

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
        l = [1, 2, 3]
        m = np.zeros(shape=(20, 20), dtype=float)
        d = {'list': l, 'matrix': m}
        pickle.dump(d, 'stuff.pkl')
        time.sleep(1)
        ck = checkpoint.checkpoint()
        ck.jack = 'sparrow'
        ck.link_file('stuff.pkl')
        ck.save_to_server()
    else:
        sys.stderr.write('recovered checkpoint\n')
        time.sleep(1)
        sys.stderr.write('Jack is: ' + ck.jack + '\n')
        print('Retrieved files:', ck.linked_files())

sys.stderr.flush()
