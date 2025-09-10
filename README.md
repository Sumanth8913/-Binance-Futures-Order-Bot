Sure! Here are the two files separately and ready to copy.

---

# **File: README.md**

````markdown
# Sumanth Binance USDT-M Futures CLI Bot

## Overview
This CLI-based bot allows you to trade Binance USDT-M Futures with:
- **Core Orders**: Market and Limit Orders
- **Advanced Orders**: OCO, TWAP, and Grid Strategy
- **Dry-run mode**: Mock API calls for testing without real trades
- **Logging**: All actions are logged in `bot.log`
- **Unit Tests**: Tests can run without live API

---

## Setup

1. **Clone or unzip project**
```bash
git clone <your_repo_url>  # or unzip sumanth_binance_bot.zip
cd sumanth_binance_bot
````

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. **Setup Binance API keys (optional for live mode)**
   Create `.env` in project root:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

If keys are missing, the bot will use **dry-run mode** (mock client).

---

## CLI Usage Examples

### Market Orders

```bash
python src/market_orders.py BTCUSDT BUY 0.001 --dry-run
```

### Limit Orders

```bash
python src/limit_orders.py BTCUSDT SELL 0.001 40000 --tif GTC --dry-run
```

### Advanced Orders (Python import)

```python
from src.advanced.twap import twap_execute
twap_execute('BTCUSDT','BUY',0.01,slices=4,interval_seconds=5,dry_run=True)

from src.advanced.grid_strategy import place_grid
place_grid('BTCUSDT', base_price=30000, spacing=100, levels=3, qty=0.001, dry_run=True)
```

### OCO Orders

```python
from src.advanced.oco import OCOManager
oco_mgr = OCOManager(dry_run=True)
oco_mgr.place_oco('BTCUSDT','BUY',0.001,tp_price=35000,stop_price=29000)
```

---

## Testing

Run unit tests (no live API required):

```bash
pytest -q
```

---

## Logging

All actions and errors are logged in `bot.log` with timestamp, log level, module, and function.

---

## Submission

* Zip folder: `sumanth_binance_bot.zip`
* Push to private GitHub: `sumanth-binance-bot`
* Add instructor as collaborator

````

