from base.misc import *
from base.stock_base import *
from base.stock_enum import Stock_Type

def get_stock_price(STK:str,stock_type:Stock_Type=None,session=None)->float:
    stock_ticker = get_ticker_info(STK=STK,session=session)
    
    if(stock_ticker!=None):
        
        if(stock_type == None):
            stock_type = get_stocktype_from_ticker(stock_ticker)

        if(stock_type == Stock_Type.EQUITY):
            if('currentPrice' in stock_ticker):
                return float(get_data_from_dict(stock_ticker,'currentPrice'))
            else:
                return float(get_data_from_dict(stock_ticker,'previousClose'))
        
        elif(stock_type == Stock_Type.ETF):
            if('bid' in stock_ticker and 'ask' in stock_ticker):
                return float(average([get_data_from_dict(stock_ticker,'bid'),get_data_from_dict(stock_ticker,'ask')]))
            else:
                return float(get_data_from_dict(stock_ticker,'previousClose'))
    
def get_stock_price_print(STK:str,stock_type:Stock_Type=None)->str:
    stock_ticker = get_ticker_info(STK)
    
    if(stock_ticker!=None):
        
        if(stock_type == None):
            stock_type = get_stocktype_from_ticker(stock_ticker)

        if(stock_type == Stock_Type.EQUITY):
            return f'{get_data_from_dict(stock_ticker,'currentPrice')}'
        elif(stock_type == Stock_Type.ETF):
            return f'{get_data_from_dict(stock_ticker,'bid')} - {get_data_from_dict(stock_ticker,'ask')}'
