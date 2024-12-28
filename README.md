# Automated Market Maker (AMM) Simulator

A Python implementation of an **Automated Market Maker (AMM)** using the **constant product formula** (\( x \cdot y = k \)) to simulate decentralized trading.

## Features
- Trade two assets: **apples** and **potatoes**.
- Dynamic pricing based on the constant product formula.
- Tracks liquidity pool state and price changes.

## Usage
1. Clone the repository and run the script:
   ```bash
   git clone https://github.com/easyhat/AMM-algo.git
   cd AMM-algo
   python amm.py
   ```

2. Example output:
   ```plaintext
   Initial Pool: Apples: 100.00, Potatoes: 100.00
   Traded 10 apples for 9.09 potatoes.
   Updated Pool: Apples: 110.00, Potatoes: 90.91
   ```

## API
- **`trade_apples_for_potatoes(amount)`**: Trade apples to get potatoes.
- **`trade_potatoes_for_apples(amount)`**: Trade potatoes to get apples.
- **`get_price()`**: Get the current price of apples in potatoes.

## Future Enhancements
- Add fees for trades.
- Support liquidity management.
- Extend to multi-token pools.
