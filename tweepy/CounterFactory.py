class Counter(object):
    def __init__(self,n=1):
        self.n = n
        self.i = 0
        
    def countUp(self):
        self.i += 1
        if self.n == self.i:
            self.i = 0
            return True
        return False
        

class CounterFactory(object):
    counters = {}
    
    @staticmethod   
    def getCounter(name,n):
        if not CounterFactory.counters.has_key(name):    
            CounterFactory.counters[name] = Counter(n)
        return CounterFactory.counters.get(name)