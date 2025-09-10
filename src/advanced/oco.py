import threading, time
from ..utils import get_client, logger

class OCOManager:
    def __init__(self, dry_run=False, testnet=False):
        self.client = get_client(dry_run=dry_run, testnet=testnet)

    def place_oco(self, symbol, side, quantity, tp_price, stop_price):
        logger.info(f'Placing OCO for {symbol} side={side} qty={quantity} tp={tp_price} stop={stop_price}')
        tp_order = self.client.futures_create_order(
            symbol=symbol, side=side, type='LIMIT', timeInForce='GTC',
            price=str(tp_price), quantity=quantity
        )
        stop_side = 'SELL' if side=='BUY' else 'BUY'
        stop_order = self.client.futures_create_order(
            symbol=symbol, side=stop_side, type='STOP_MARKET',
            stopPrice=str(stop_price), quantity=quantity
        )
        threading.Thread(target=self._monitor_pair, args=(symbol, tp_order['orderId'], stop_order['orderId']), daemon=True).start()
        return tp_order, stop_order

    def _monitor_pair(self, symbol, tp_id, stop_id):
        while True:
            try:
                tp = self.client.futures_get_order(symbol=symbol, orderId=tp_id)
                stop = self.client.futures_get_order(symbol=symbol, orderId=stop_id)
                if tp.get('status')=='FILLED':
                    logger.info(f'TP filled; cancelling stop {stop_id}')
                    self.client.futures_cancel_order(symbol=symbol, orderId=stop_id)
                    break
                if stop.get('status')=='FILLED':
                    logger.info(f'Stop filled; cancelling tp {tp_id}')
                    self.client.futures_cancel_order(symbol=symbol, orderId=tp_id)
                    break
            except Exception:
                logger.exception('Error monitoring OCO pair')
            time.sleep(1)
