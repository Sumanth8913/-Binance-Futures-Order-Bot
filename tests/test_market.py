import pytest
from src.market_orders import place_market_order
from src.utils import get_client

def test_market_order_dry_run():
    symbol = 'BTCUSDT'
    side = 'BUY'
    qty = 0.001
    client = get_client(dry_run=True)
    order = place_market_order(symbol, side, qty, dry_run=True)
    assert order['status'] == 'NEW'
    assert order['symbol'] == symbol
    assert order['side'] == side
    assert float(order['quantity']) == qty

def test_invalid_symbol():
    from src.utils import validate_symbol
    with pytest.raises(ValueError):
        validate_symbol('BTC')

def test_invalid_side():
    from src.utils import validate_side
    with pytest.raises(ValueError):
        validate_side('HOLD')

def test_invalid_quantity():
    from src.utils import validate_qty
    with pytest.raises(ValueError):
        validate_qty(0)
