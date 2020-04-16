import argparse
import sys
import time
from itertools import count, islice
from math import sqrt
import numpy as np

import hydra


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=5, help='primes')
parser.add_argument('--print_every', type=int, default=1, help='print_every')
parser.add_argument('--hydra_checkpoints', action='store_true', default=False,
                    help='Save checkpoints to borg server.')
parser.add_argument('--hydra_checkpoint_every', type=int, default=10, help='Save checkpoints to borg every.')
parser.add_argument('--hydra_eta_every', type=int, default=10, help='Save checkpoints to borg every.')
args = parser.parse_args()

start_index = 0
delay = 5.0

if args.hydra_checkpoints:
    if not hydra.is_available():
        sys.stderr.write('hydra checkpoints option not available\n')
        args.hydra_checkpoints = False
    else:
        sys.stderr.write('hydra checkpoints option is available\n')
        ck = hydra.restore_checkpoint()
        if ck is None:
            sys.stderr.write('no checkpoint to be restored\n')
        else:
            sys.stderr.write('found checkpoint: starting from n={}\n'.format(ck.n))
            start_index = ck.n + 1
            delay = ck.delay

sys.stderr.flush()

exp_it = None
tic = time.time()
damp = 0.7

for n in range(start_index, args.n + 1):
    time.sleep(delay)
    delay += np.random.uniform(-0.1, 0.1)
    if delay < 1.0:
        delay = 1.0

    toc = time.time()

    if exp_it is None:
        exp_it = toc - tic
    else:
        exp_it = damp * (toc - tic) + (1.0 - damp) * exp_it

    tic = toc

    if n % args.print_every == 0:
        print(n, '/', args.n, ' - delay:', delay, ' - exp:', exp_it, ' - eta: ', (args.n - n) * exp_it)
        sys.stdout.flush()

    if hydra.is_available():
        hydra.set_eta((args.n - start_index) * exp_it)

    if args.hydra_checkpoints and n % args.eta_every == 0:
        hydra.set_eta((args.n - start_index) * exp_it)

    if args.hydra_checkpoints and (n + 1) % args.hydra_checkpoint_every == 0:
        ck = hydra.checkpoint()
        ck.n = n
        ck.delay = delay
        ck.save_to_server()

print('Finished ', args.n)
