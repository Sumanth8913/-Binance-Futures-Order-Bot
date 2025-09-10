# README.md (Clean Version)

````markdown
# Sumanth Binance USDT-M Futures CLI Bot

## Overview
This CLI-based bot allows you to trade Binance USDT-M Futures with:
- Core Orders: Market and Limit Orders
- Advanced Orders: OCO, TWAP, and Grid Strategy
- Dry-run mode: Mock API calls for testing without real trades
- Logging: All actions are logged in bot.log
- Unit Tests: Tests can run without live API

---

## Setup

1. Clone or unzip project
```bash
git clone <your_repo_url>  # or unzip sumanth_binance_bot.zip
cd sumanth_binance_bot
````

2. Create and activate virtual environment

```bash
python -m venv venv
# Activate
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

3. Setup Binance API keys (optional for live mode)
   Create .env in project root:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

If keys are missing, the bot automatically uses dry-run mode (mock trades).

---

## CLI Usage Examples

### Market Orders

Command:

```bash
python src/market_orders.py BTCUSDT BUY 0.001 --dry-run
```

Input:

* Symbol: BTCUSDT
* Side: BUY
* Quantity: 0.001
* \--dry-run: Optional (simulate order)

Sample Output:

```json
{
  "orderId": 123456,
  "status": "NEW",
  "symbol": "BTCUSDT",
  "side": "BUY",
  "quantity": 0.001
}
```

Logged in bot.log:

```
2025-09-10 12:00:01 | INFO | binance_bot | place_market_order | Attempting MARKET order BTCUSDT BUY qty=0.001 dry_run=True
2025-09-10 12:00:01 | INFO | binance_bot | place_market_order | Order response: {'orderId': 123456, 'status': 'NEW'}
```

---

### Limit Orders

Command:

```bash
python src/limit_orders.py BTCUSDT SELL 0.001 40000 --tif GTC --dry-run
```

Input:

* Symbol: BTCUSDT
* Side: SELL
* Quantity: 0.001
* Price: 40000
* TIF: GTC (Good Till Cancel)
* \--dry-run: Optional

Sample Output:

```json
{
  "orderId": 123457,
  "status": "NEW",
  "symbol": "BTCUSDT",
  "side": "SELL",
  "quantity": 0.001,
  "price": 40000
}
```

Logged in bot.log:

```
2025-09-10 12:01:05 | INFO | binance_bot | place_limit_order | Attempting LIMIT order BTCUSDT SELL qty=0.001 price=40000 TIF=GTC dry_run=True
2025-09-10 12:01:05 | INFO | binance_bot | place_limit_order | Order response: {'orderId': 123457, 'status': 'NEW'}
```

---

### Advanced Orders (Python Scripts)

OCO Order Example:

```python
from src.advanced.oco import OCOManager
oco_mgr = OCOManager(dry_run=True)
oco_mgr.place_oco('BTCUSDT','BUY',0.001,tp_price=35000,stop_price=29000)
```

Input:

* Symbol: BTCUSDT
* Side: BUY
* Quantity: 0.001
* Take Profit Price: 35000
* Stop Loss Price: 29000

Sample Output:

```json
{
  "tp_order": {"orderId": 123458, "status": "NEW"},
  "stop_order": {"orderId": 123459, "status": "NEW"}
}
```

Logged in bot.log:

```
2025-09-10 12:02:00 | INFO | binance_bot | place_oco | Placing OCO for BTCUSDT side=BUY qty=0.001 tp=35000 stop=29000
```

TWAP Example:

```python
from src.advanced.twap import twap_execute
twap_execute('BTCUSDT','BUY',0.01,slices=4,interval_seconds=5,dry_run=True)
```

Sample Output (Orders placed over time):

```json
[123460, 123461, 123462, 123463]
```

Logs:

```
Placed slice 1/4 orderId=123460
Placed slice 2/4 orderId=123461
...
```

Grid Strategy Example:

```python
from src.advanced.grid_strategy import place_grid
place_grid('BTCUSDT', base_price=30000, spacing=100, levels=3, qty=0.001, dry_run=True)
```

Sample Output:

* Multiple buy and sell limit orders around base price
* Logged in bot.log for each order

---

## Running Tests

```bash
pytest -q
```

Expected Output:

```
==== test session starts ====
collected 6 items

tests/test_market.py ..  
tests/test_limit.py ..  

6 passed in 0.45s
```

---

## Logging

* All actions and errors logged in bot.log
* Includes timestamp, module, function, and order details

---

## Submission

* Zip folder: sumanth\_binance\_bot.zip
* Push to private GitHub: sumanth-binance-bot
* Add instructor as collaborator

