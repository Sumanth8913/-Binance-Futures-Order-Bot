import argparse
from .utils import get_client, validate_symbol, validate_side, validate_qty, logger

def place_market_order(symbol, side, qty, dry_run=False, testnet=False):
    client = get_client(dry_run=dry_run, testnet=testnet)
    logger.info(f'Attempting MARKET order {symbol} {side} qty={qty} dry_run={dry_run}')
    try:
        order = client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=qty)
        logger.info(f'Order response: {order}')
        return order
    except Exception as e:
        logger.exception('Error placing market order')
        raise

def main():
    p = argparse.ArgumentParser(description='Place MARKET order')
    p.add_argument('symbol')
    p.add_argument('side')
    p.add_argument('quantity')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--testnet', action='store_true')
    args = p.parse_args()

    symbol = validate_symbol(args.symbol)
    side = validate_side(args.side)
    qty = validate_qty(args.quantity)
    res = place_market_order(symbol, side, qty, dry_run=args.dry_run, testnet=args.testnet)
    print(res)

if __name__=='__main__':
    main()
