import sys
import os

def die(msg):
    #print os.getcwd()
    print >> sys.stderr, "ERROR: {e}".format(e=msg)
    exit(1)


def warn(msg):
    #print os.getcwd()
    print >> sys.stderr, "ERROR: {e}".format(e=msg)


