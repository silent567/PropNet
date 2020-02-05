#!/usr/bin/env python
# coding=utf-8

from utils import run_config
import argparse

def command2name(command):
    args = command.split()[2:]
    print(command)
    print(args)
    return '-'.join([''.join([a.strip('-')[0]+''.join([aa for aa in a.strip('-')[1:] if aa.isupper() or aa in '0123456789'])
                              for a in arg.split('_')]) for arg in args])
def commands2name(commands):
    return 'ht-'+('test-' if 'test.py' in ''.join(commands) else '')+\
        ('.'.join([command2name(cmd) for cmd in commands]).lower())
def commands2command(commands):
    return 'cd /cephfs/haotang/PropNet && bash parallel.sh ' + (' '.join(["'%s'"%cmd for cmd in commands]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('commands', default=[], type=str, nargs='+')
    parser.add_argument('--name', default=None, type=str)
    parser.add_argument('--cpu_request', default=2, type=int)
    parser.add_argument('--cpu_limit', default=3, type=int)
    parser.add_argument('--memory_request', default=8, type=int)
    parser.add_argument('--memory_limit', default=10, type=int)
    parser.add_argument('--gpu_request', default=1, type=int)
    parser.add_argument('--gpu_limit', default=1, type=int)
    parser.add_argument('--public_flag', action='store_true', default=False)
    args = parser.parse_args()

    name = args.name or commands2name(args.commands)
    public_flag = args.public_flag
    command = commands2command(args.commands)
    resources = args.__dict__

    run_config(name, public_flag, command, resources)
