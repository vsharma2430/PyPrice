import requests
from base.paytm.paytm_urls import *
from base.paytm.paytm_headers import *
from base.paytm.paytm_payload import *
from base.paytm.paytm_params import *
from your_token_here import *

r = requests.get(live_price_url, 
                  headers=jwt_headers(JWT_TOKEN=response['read_access_token']), 
                  params=live_price_params(MODE_TYPE='FULL',
                                           PREFERENCES=live_price_pref(Exchange='NSE',
                                                                       ScripId=19084,
                                                                       ScripType='ETF')))

print(r.status_code)
print(r.text) 