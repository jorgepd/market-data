# imports
import time

# custom imports
from config import logger



def retry(exc, delay, tries):
    '''
    Decorator designed to deal with APIs that limit request
    number. When a request fails, the decorator sleeps for
    'delay' seconds and try again, at most 'tries' times.
    '''
    def decorator(fn):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return fn(*args, **kwargs)
                except exc:
                    print('Too many requests, sleeping...')
                    time.sleep(delay)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def try_catch(fn):
    '''
    Decorator to be used as a try catch block, only to
    standardize error logging.
    '''
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            logger.error(e)

    return wrapper