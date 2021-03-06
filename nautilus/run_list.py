#!/usr/bin/env python
# coding=utf-8

import subprocess
import sys, random
random.seed(0)

with open('job_list.txt') as f:
    commands = f.readlines()
commands = [cmd.strip() for cmd in commands]
random.shuffle(commands)
commands = [commands[i:i+3] for i in range(0, len(commands), 3)]

for cmd in commands:
    subprocess.call(['python', 'run.py']+list(cmd)+list(sys.argv[1:]))
