'''Time-related utilities.
'''

from time import time, clock


class HiResTime: #IGNORE:W0232
    '''High-resolution time.
    '''
    base_time = time()
    base_clock = clock()
    REINIT_STEP_SEC = 30

    @classmethod
    def init(cls):
        '''(re-)initialise base parameters.
        '''
        cls.base_time = time()
        cls.base_clock = clock()

    @classmethod
    def time(cls):
        '''Get good time.
        '''
        if cls.REINIT_STEP_SEC < time() - cls.base_time:
            # Reinitialise base clock and time, because clock drifts.
            cls.init()
        return cls.base_time + clock() - cls.base_clock

def hrtime():
    '''Higher-resolution time, based on clock().
    There's a problem with clock() -- it drifts. So every second, we reinitialise base clock and time.
    '''
    return HiResTime.time()
