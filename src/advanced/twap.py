import time
from ..utils import get_client, logger

def twap_execute(symbol, side, total_qty, slices=5, interval_seconds=10, dry_run=False, testnet=False):
    client = get_client(dry_run=dry_run, testnet=testnet)
    qty_each = float(total_qty)/slices
    logger.info(f'Starting TWAP {symbol} {side} total={total_qty} slices={slices} qty_each={qty_each} dry_run={dry_run}')
    order_ids = []
    for i in range(slices):
        order = client.futures_create_order(symbol=symbol, side=side, type='MARKET', quantity=qty_each)
        logger.info(f'Placed slice {i+1}/{slices} orderId={order.get("orderId")}')
        order_ids.append(order.get('orderId'))
        if i < slices-1:
            time.sleep(interval_seconds)
    return order_ids
