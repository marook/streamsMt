#!/usr/bin/python2

import plainMultiprocess
import streamsMt

def main():
    line = streamsMt.Line()

    line.addStep(f=plainMultiprocess.buildNumbers, args=(10,), maxsize=3)
    line.addStep(f=plainMultiprocess.negate, maxsize=3)
    line.addStep(f=plainMultiprocess.printer)

    line.start()
    line.join()

if __name__ == '__main__':
    main()

