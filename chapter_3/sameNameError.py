#!/usr/bin/env python3

def spam():
    print(eggs) # error!
    eggs = 'spam local'

eggs = 'global'
spam()