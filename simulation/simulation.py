import random
from exchange.oms import OrderManagementSystem
from exchange.trader import Trader
from exchange import StockExchange

class Simulation:
    def __init__(self, num_traders, trading_hours):
        self.exchange = StockExchange()
        self.traders = []
        self.sec = ["AAPL", "TSLA", "MSFT", "GOOG", "AMZN"]
        self.num_traders = num_traders
        self.trading_seconds = int(trading_hours * 3600)

        for i in range(num_traders):
            portfolio = {s: random.randint(1000, 10000) for s in self.sec}
            oms = OrderManagementSystem(
                bank_balance=random.randint(50000, 100000),
                initial_cash_trading=random.randint(5000, 20000),
                portfolio=portfolio,
                exchange=self.exchange
            )
            trader = Trader(f"Trader_{i+1}", oms, self.exchange)
            self.traders.append(trader)

    def run(self):
        for second in range(self.trading_seconds):
            list_active_traders = [t for t in self.traders if t.activeness()]
            if len(list_active_traders) <= 1:
                break
            for trader in list_active_traders:
                if random.random() >= 0.5:
                    security = random.choice(self.sec)
                    trader.action(security, second)

        print("\nFinal Prices:")
        for s in self.sec:
            best_bid, best_ask = self.exchange.get_best_bid_ask(s)
            print(f"{s}: Best Bid = {best_bid}, Best Ask = {best_ask}")

        for trader in self.traders:
            print(f"{trader.trader_id} Final Total Cash Left: {trader.oms.cash + trader.oms.bank_balance}, Portfolio: {trader.oms.portfolio}")
