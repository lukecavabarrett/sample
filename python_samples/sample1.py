import sys

if __name__ == '__main__':

    sys.stderr.write('Started sample1\n')
    print(type(sys.argv))
    print(len(sys.argv))
    for arg in sys.argv:
        print(type(arg), ':', arg)
    sys.stderr.write('Completed sample1\n')
