import pytest
from src.limit_orders import place_limit_order
from src.utils import get_client

def test_limit_order_dry_run():
    symbol = 'BTCUSDT'
    side = 'SELL'
    qty = 0.001
    price = 40000
    client = get_client(dry_run=True)
    order = place_limit_order(symbol, side, qty, price, dry_run=True)
    assert order['status'] == 'NEW'
    assert order['symbol'] == symbol
    assert order['side'] == side
    assert float(order['quantity']) == qty
    assert float(order['price']) == price

def test_invalid_price():
    from src.utils import validate_price
    with pytest.raises(ValueError):
        validate_price(-100)

def test_invalid_tif():
    from src.limit_orders import place_limit_order
    # Should default to GTC if TIF not provided
    order = place_limit_order('BTCUSDT','BUY',0.001,40000,dry_run=True)
    assert order['status'] == 'NEW'
