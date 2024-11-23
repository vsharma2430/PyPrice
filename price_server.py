import os
import signal
from fastapi import FastAPI, Request , Response
from fastapi.responses import JSONResponse
from base.stock_price import *
from base.stock_base import *

app = FastAPI()

@app.get('/',response_class=JSONResponse)
def stock_price(request: Request):
    return {'message': 'Price server is running.'}

@app.get('/{stk_id}/',response_class=JSONResponse)
def stock_price(request: Request,stk_id:str):
    return {'ticker': get_ticker_info(STK=stk_id,session=None)}

@app.get('/{stk_id}/price/',response_class=JSONResponse)
def stock_price(request: Request,stk_id:str):
    return {'price': get_stock_price(STK=stk_id,session=None)}

@app.get('/{stk_id}/{key}/',response_class=JSONResponse)
def stock_price(request: Request,stk_id:str,key:str):
    return {f'{key}': get_ticker_info(STK=stk_id,session=None)[key]}

# start shutdown server
def start():
    return Response(status_code=200, content='Server started')

def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return Response(status_code=200, content='Server shutting down...')

@app.on_event('shutdown')
def on_shutdown():
    print('Server shutting down...')

app.add_api_route('/start', start, methods=['GET'])
app.add_api_route('/shutdown', shutdown, methods=['GET'])