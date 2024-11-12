import datetime as dt
from base.misc import *
from base.stock_base import *
from base.stock_price import *
from logging import getLogger
from pandas import DataFrame
from base.stock_chart import *

logger = getLogger('uvicorn.error')

@timeit
def get_historical_data(STK:str,
                        start_date:dt.date = (dt.datetime.now()-dt.timedelta(days=365)).date(),
                        end_date:dt.date=dt.datetime.now().date(),
                        session=None):
    logger.info(f'Fetcing data for {STK}')

    STK = get_yfin_symbol(STK)
    stk_ticker= get_ticker(STK=STK,session=session)
    stk_historical_df = stk_ticker.history(start=start_date, end=end_date)
    
    average_price_30 = average([stk_historical_df['Open'].tail(20).mean() , stk_historical_df['Close'].tail(20).mean()])
    average_price_90 = average([stk_historical_df['Open'].tail(60).mean() , stk_historical_df['Close'].tail(60).mean()])
    average_price_365 = average([stk_historical_df['Open'].mean() , stk_historical_df['Close'].mean()])

    average_volume_30 = stk_historical_df['Volume'].tail(20).mean()
    average_volume_90 = stk_historical_df['Volume'].tail(60).mean()
    average_volume_365 = stk_historical_df['Volume'].mean()
    
    return {'df' : stk_historical_df ,
            'start_date' : start_date , 
            'end_date' : end_date,
            'dma_30' : average_price_30 , 
            'dma_90' : average_price_90 , 
            'dma_365' : average_price_365 , 
            'volume_30':average_volume_30,
            'volume_90':average_volume_90,
            'volume_365':average_volume_365,
            } 

def get_current_data(STK:str,
                     session=None):
        return  {
                'current_stock_price' : get_round(get_stock_price(STK,Stock_Type.ETF))
        }
        
def get_dma_change(history_data:dict,current_data:dict):
        average_price = get_round(get_data_from_dict(history_data,'dma_30'))
        current_stock_price = get_data_from_dict(current_data,'current_stock_price')
        return get_change_percentage(average_price,current_stock_price)

def get_history_context(STK:str,
                        session=None):
    history_data = get_historical_data(STK,session=session)
    current_data = get_current_data(STK,session=session)
    
    history_data_df : DataFrame = get_data_from_dict(history_data,'df')
    history_data_html = history_data_df.to_html().replace('dataframe','table table-fixed')
    current_stock_price = get_data_from_dict(current_data,'current_stock_price')
    
    change = get_dma_change(history_data,current_data)

    return {
            'title':f'Stock History : {STK}',
            'stock_id':STK,
            'cmp': f'{current_stock_price}',
            'timeline':f'{get_data_from_dict(history_data,'start_date')} to {get_data_from_dict(history_data,'end_date')}',
            'dma_30':get_round(get_data_from_dict(history_data,'dma_30')),
            'dma_90':get_round(get_data_from_dict(history_data,'dma_90')),
            'dma_365':get_round(get_data_from_dict(history_data,'dma_365')),
            'change':f'{change}',
            'volume_30':get_format(get_round(get_data_from_dict(history_data,'volume_30'))),
            'volume_90':get_format(get_round(get_data_from_dict(history_data,'volume_90'))),
            'volume_365':get_format(get_round(get_data_from_dict(history_data,'volume_365'))),
            'history': history_data_html,
            'chart':get_chart(history_data_df)
            }