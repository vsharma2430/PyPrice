live_price_params = lambda MODE_TYPE,PREFERENCES :{
    'mode': f'{MODE_TYPE}',
    'pref': f'{PREFERENCES}',
}

live_price_pref = lambda Exchange,ScripId,ScripType : f'{Exchange}:{ScripId}:{ScripType}'