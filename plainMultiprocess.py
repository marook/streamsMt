#!/usr/bin/python2

import multiprocessing as mp

def main():
    processes = []
    
    numbers = mp.Queue(maxsize=3)
    processes.append(mp.Process(target=buildNumbers, args=(10, numbers,)))

    negatedNumbers = mp.Queue(maxsize=3)
    processes.append(mp.Process(target=negate, args=(numbers, negatedNumbers)))

    processes.append(mp.Process(target=printer, args=(negatedNumbers,)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    
def buildNumbers(n, sink=None):
    for i in xrange(n):
        print 'Generate %s' % (i, )
        sink.put(i)

    sink.put('eom')

def negate(source=None, sink=None):
    while True:
        msg = source.get()

        if(msg == 'eom'):
            sink.put('eom')
            break

        print 'Negate %s' % (msg, )

        sink.put(-msg)

def printer(source=None):
    while True:
        msg = source.get()

        print 'Print %s' % (msg,)

        if(msg == 'eom'):
            break

if __name__ == '__main__':
    main()
