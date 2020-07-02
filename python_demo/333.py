import time, threading

import sys, os
from multiprocessing import Pool
from multiprocessing import Process
from locust import User, TaskSet, task, events
import subprocess

def run(i):
    if i == "master":
        # subprocess.Popen(("python"),shell=True).wait()
        print(i)
        a = os.popen("python").read()
        print(a)
    else:
        print(i)
        os.popen("python").read()

t = threading.Thread(target=run, args=("master",))
t.start()

for i in range(5):
    t1 = threading.Thread(target=run, args=(i,))
    t1.start()

