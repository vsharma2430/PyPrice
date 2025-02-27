from ..base_class import security

NSE = security (security_name= 'NSE'    ,fetch_address='https://developer.paytmmoney.com/data/v1/scrips/nse_security_master.csv')
BSE = security (security_name= 'BSE'    ,fetch_address='https://developer.paytmmoney.com/data/v1/scrips/bse_security_master.csv')
INX = security (security_name= 'INDEX'  ,fetch_address='https://developer.paytmmoney.com/data/v1/scrips/index_security_master.csv')
EQY = security (security_name= 'EQUITY' ,fetch_address='https://developer.paytmmoney.com/data/v1/scrips/equity_security_master.csv')
ETF = security (security_name= 'ETF'	,fetch_address='https://developer.paytmmoney.com/data/v1/scrips/etf_security_master.csv')