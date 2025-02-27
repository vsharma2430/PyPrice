login_url:str = lambda api_key,state_key: f'https://login.paytmmoney.com/merchant-login?apiKey={api_key}&state={state_key}'
logout_url:str = 'https://developer.paytmmoney.com/accounts/v1/logout'
generate_access_token:str = 'https://developer.paytmmoney.com/accounts/v2/gettoken'
live_price_url:str = 'https://developer.paytmmoney.com/data/v1/price/live'