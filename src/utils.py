import os
from dotenv import load_dotenv
from .logger_setup import get_logger

load_dotenv()
logger = get_logger(__name__)

def validate_symbol(sym):
    if not isinstance(sym, str) or not sym.endswith('USDT'):
        raise ValueError('Symbol should end with USDT')
    return sym.upper()

def validate_side(side):
    s = side.upper()
    if s not in ('BUY','SELL'):
        raise ValueError('Side must be BUY or SELL')
    return s

def validate_qty(q):
    qq = float(q)
    if qq <= 0:
        raise ValueError('Quantity must be > 0')
    return qq

def validate_price(p):
    pp = float(p)
    if pp <= 0:
        raise ValueError('Price must be > 0')
    return pp

def get_client(dry_run=False, testnet=False):
    if dry_run:
        logger.info('Using MockClient (dry-run mode)')
        return MockClient()
    try:
        from binance.client import Client
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        if not api_key or not api_secret:
            logger.warning('API keys missing, using MockClient')
            return MockClient()
        client = Client(api_key, api_secret)
        if testnet:
            client.FUTURE_API_URL = 'https://testnet.binancefuture.com/fapi'
        return client
    except Exception:
        logger.exception('python-binance not available, using MockClient')
        return MockClient()

class MockClient:
    def futures_create_order(self, **kwargs):
        return {'orderId': 123456, 'status':'NEW', 'clientOrderId':'mocked', **kwargs}
    def futures_get_order(self, **kwargs):
        return {'orderId': kwargs.get('orderId'), 'status':'NEW'}
    def futures_cancel_order(self, **kwargs):
        return {'orderId': kwargs.get('orderId'), 'status':'CANCELED'}
