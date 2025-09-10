import argparse
from .utils import get_client, validate_symbol, validate_side, validate_qty, validate_price, logger

def place_limit_order(symbol, side, qty, price, tif='GTC', dry_run=False, testnet=False):
    client = get_client(dry_run=dry_run, testnet=testnet)
    logger.info(f'Attempting LIMIT order {symbol} {side} qty={qty} price={price} TIF={tif} dry_run={dry_run}')
    try:
        order = client.futures_create_order(
            symbol=symbol, side=side, type='LIMIT', timeInForce=tif,
            quantity=qty, price=str(price)
        )
        logger.info(f'Order response: {order}')
        return order
    except Exception:
        logger.exception('Error placing limit order')
        raise

def main():
    p = argparse.ArgumentParser(description='Place LIMIT order')
    p.add_argument('symbol')
    p.add_argument('side')
    p.add_argument('quantity')
    p.add_argument('price')
    p.add_argument('--tif', default='GTC')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--testnet', action='store_true')
    args = p.parse_args()

    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    qty = validate_qty(args.quantity)
    price = validate_price(args.price)
    res = place_limit_order(symbol, side, qty, price, tif=args.tif, dry_run=args.dry_run, testnet=args.testnet)
    print(res)

if __name__=='__main__':
    main()
