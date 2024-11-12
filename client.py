import os
import signal
import fastapi
import uvicorn
from price_server import live_price_app

def start():
    return fastapi.Response(status_code=200, content='Server started')

def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)
    return fastapi.Response(status_code=200, content='Server shutting down...')

@live_price_app.on_event('shutdown')
def on_shutdown():
    print('Server shutting down...')

live_price_app.add_api_route('/start', start, methods=['GET'])
live_price_app.add_api_route('/shutdown', shutdown, methods=['GET'])

if __name__ == '__main__':
    uvicorn.run(live_price_app, host='localhost', port=8006)