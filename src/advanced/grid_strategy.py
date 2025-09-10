from ..utils import get_client, logger

def generate_grid(base_price, spacing, levels):
    buys = [round(base_price - spacing*i, 2) for i in range(1, levels+1)]
    sells = [round(base_price + spacing*i, 2) for i in range(1, levels+1)]
    return buys, sells

def place_grid(symbol, base_price, spacing, levels, qty, dry_run=False, testnet=False):
    client = get_client(dry_run=dry_run, testnet=testnet)
    buys, sells = generate_grid(base_price, spacing, levels)
    orders = []
    for p in buys:
        o = client.futures_create_order(symbol=symbol, side='BUY', type='LIMIT', timeInForce='GTC', price=str(p), quantity=qty)
        orders.append(o)
       
