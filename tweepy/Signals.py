import signal
import sys


def sigint_handler(signal,frame):
    sys.exit(0)
    
def handle_signals():
    signal.signal(signal.SIGINT,sigint_handler)