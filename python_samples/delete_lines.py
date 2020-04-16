import sys
import time

if __name__ == '__main__':

    for i in range(100):
        sys.stdout.write("\rTest" + str(i))
        if i % 5 == 4:
            sys.stdout.write("\n")
        time.sleep(0.5)
