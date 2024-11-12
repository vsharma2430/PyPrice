from enum import Enum

class Stock_Type(Enum):
    EQUITY = 1
    ETF = 2
    COMMODITY = 3
    
class Stock_Exchange(Enum):
    NSE = 1
    BSE = 2
    
class Stock_Symbol(Enum):
    PLAIN = 1
    GFIN = 2
    YFIN = 3
    
class Stock_Trade(Enum):
    BUY = 1
    SELL = 2