from fastapi import FastAPI, Request
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
