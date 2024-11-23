import uvicorn
from price_server import app

if (__name__ == '__main__'):
    uvicorn.run('price_server:app', host='localhost', port=8006)