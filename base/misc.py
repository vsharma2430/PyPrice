import re
from datetime import datetime
from functools import wraps
import time
from logging import getLogger

logger = getLogger('uvicorn.error')

def get_data_from_dict(dictObj:dict,key:object):
    if(dictObj != None):
        if(key in dictObj):
            return dictObj[key]
    return None

def average(range:list):
    return sum(range)/len(range)

def get_date(text:str):
    print(text)
    #2024-10-11 00:00:00+05:30
    match = re.search(r'\d{4}-\d{2}-\d{2}', text)
    if(match != None):
        date = datetime.strptime(match.group(), '%Y-%d-%m').date()
        return date.strftime('%d-%m-%Y')
    return text

def get_change(initial:float,final:float)->float:
    if(initial!=None or final != None or initial!=0):
        return (final - initial) / initial
    return 0

def get_change_percentage(initial:float,final:float,n_digits:int=2)->float:
    if(initial!=None or final != None or initial!=0):
        return round((final - initial) / initial * 100,2)
    return 0

def get_round(data):
    if(data!=None):
        return round(data,3)
    return 0

def get_format(data):
    if(data!=None):
        return "{:,}".format(data)
    return 0

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        logger.info(f'Function {func.__name__}{args} {kwargs} took {total_time:.4f} seconds.')
        
        return result
    return timeit_wrapper
    