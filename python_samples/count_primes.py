import argparse
import pickle
import time, sys
from itertools import count, islice
from math import sqrt
import hydra

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=5, help='primes')
parser.add_argument('--print_every', type=int, default=1, help='print_every')
parser.add_argument('--hydra_checkpoints', action='store_true', default=False,
                    help='Save checkpoints to borg server.')
parser.add_argument('--hydra_checkpoint_every', type=int, default=10, help='Save checkpoints to borg every.')
args = parser.parse_args()

start_index = 0
primes = 0
with open('primes.txt', 'w'):
    pass

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
            primes = ck.primes

sys.stderr.flush()

for n in range(start_index, args.n + 1):
    time.sleep(1)
    if is_prime(n):
        primes += 1
        with open('primes.txt', "a") as f:
            f.write(str(n) + '\n')
            f.close()
    if n % args.print_every == 0:
        print(n, '/', args.n, ':', primes)
        sys.stdout.flush()
    if args.hydra_checkpoints and (n + 1) % args.hydra_checkpoint_every == 0:
        ck = hydra.checkpoint()
        ck.n = n
        ck.primes = primes
        ck.link_file('primes.txt')
        ck.save_to_server()

print('There are', primes, 'primes below', args.n)
