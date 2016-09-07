#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pystap import dtrace_deco

@dtrace_deco
def its_a_test(a_para, that_para=None):
    print a_para, that_para

if __name__ == '__main__':
    import time
    i = 0
    while 1:
        i += 1
        its_a_test(time.time(), that_para=i)
        time.sleep(1)
