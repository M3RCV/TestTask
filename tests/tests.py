import os, signal
os.kill(os.getpid(), signal.SIGINT)