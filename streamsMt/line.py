
import multiprocessing as mp

class Line(object):

    def __init__(self):
        self._processes = []

        self._lastStep = None
        self._lastSink = None

    def addStep(self, f, args=(), kwargs=None, maxsize=None):
        self._buildProcessFromLastStep(lastProcess=False)

        self._lastStep = (f, args, kwargs, maxsize)
    
    def start(self):
        self._buildProcessFromLastStep(lastProcess=True)
        
        for p in self._processes:
            p.start()

    def _buildProcessFromLastStep(self, lastProcess=False):
        if(self._lastStep is None):
            return

        f, args, kwargs, maxsize = self._lastStep

        kwargs = {} if kwargs is None else kwargs.copy()

        if(not self._lastSink is None):
            kwargs['source'] = self._lastSink

        if(not lastProcess):
            self._lastSink = mp.Queue(maxsize=maxsize)
            
            kwargs['sink'] = self._lastSink

        self._processes.append(mp.Process(target=f, args=args, kwargs=kwargs))

    def join(self):
        for p in self._processes:
            p.join()
