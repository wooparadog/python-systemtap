DTRACE=dtrace
CFLAGS = -O2 -g -Wall -D_GNU_SOURCE -fPIC
CC = gcc

all: probes.o probes.h
	$(CC) $(CFLAGS) -c -m64 -o pytap.o pytap.c 
	$(CC) -shared -o lib.so pytap.o probes.o

lib: probes.h probes.o

probes.h: probes.d
	$(DTRACE) -C -h -s $< -o $@

probes.o: probes.d
	$(DTRACE) -64 -C -G -s $< -o $@

clean:
	rm lib.so probes.h probes.o pytap.o
