/*
 * pytap.c
 * Copyright (C) 2016 WooParadog <guohaochuan@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <sys/sdt.h>
#include "probes.h"

void probe(char* api_name, char* args){
  DTRACE_PROBE2(pystap, entry, api_name, args);
}
