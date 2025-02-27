json_headers = {
    'Content-Type': 'application/json',
}

token_headers = lambda CLIENT_ID,CLIENT_SECRET,API_KEY : {
    "Content-Type": "application/json",
    "x-client-id": CLIENT_ID,
    "x-client-secret": CLIENT_SECRET,
    "x-api-key": API_KEY
}

jwt_headers = lambda JWT_TOKEN : {
    'x-jwt-token': f'{JWT_TOKEN}',
}