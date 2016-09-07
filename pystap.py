# -*- coding: utf-8 -*-

import ctypes
import functools

pystap = ctypes.cdll.LoadLibrary('./libpystap.so')

pystap.probe.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
pystap.probe.restype = ctypes.POINTER(ctypes.c_void_p)

def dtrace_deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        pystap.probe(func.__name__, "%r, %r" % (args, kwds))
        return func(*args, **kwds)
    return wrapper

