import argparse,sys,time

parser = argparse.ArgumentParser()
parser.add_argument('--n',type=int,default=5,help='step number')
parser.add_argument('--delay',type=int,default=1,help='single delay')
args = parser.parse_args()
sys.stderr.write('started process\n')
for i in range(args.n):
    print(i)
    sys.stdout.flush()
    time.sleep(args.delay)
print('Done')
sys.stderr.write('ended process\n')
