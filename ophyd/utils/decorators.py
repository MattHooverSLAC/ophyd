import functools


def cached_retval(fcn):
    '''
    Function decorator

    Caches the wrapped functions return value

    .. note:: parameters are not taken into account (TODO)
    '''
    status = {'called': False,
              'retval': None}

    @functools.wraps(fcn)
    def wrapped():
        if not status['called']:
            status['called'] = True
            status['retval'] = fcn()

        return status['retval']

    return wrapped
