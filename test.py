#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 WooParadog <guohaochuan@gmail.com>
#
# Distributed under terms of the MIT license.

import ctypes

utils = ctypes.cdll.LoadLibrary('./lib.so')

import time
while 1:
    time.sleep(1)

