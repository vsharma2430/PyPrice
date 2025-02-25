import uvicorn
import click
from price_server import app

@click.command
@click.option('--host',default='localhost')
@click.option('--port',default=8006)
@click.option('--dev',default=False)
def uvicorn_app(host,port,dev):
    uvicorn.run('price_server:app', host=host, port=port,reload=dev)

if (__name__ == '__main__'):
    uvicorn_app()