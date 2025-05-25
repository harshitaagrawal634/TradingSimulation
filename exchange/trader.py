import random

class Trader:
    def __init__(self, trader_id, oms, exchange, active=True):
        self.trader_id = trader_id
        self.oms = oms
        self.exchange = exchange
        self.active = active

    def action(self, security, t):
        best_bid, best_ask = self.exchange.get_best_bid_ask(security)
        last_price = self.exchange.current_prices[security]

        if best_bid and best_ask:
            price_choice = random.choice([best_bid, best_ask, (best_bid + best_ask) / 2])
        else:
            price_choice = last_price * random.uniform(0.95, 1.05)

        quantity = 1000
        order_type = random.choice(["BUY", "SELL"])

        if order_type == "BUY":
            self.oms.place_buy(self.trader_id, security, quantity, price_choice, t)
        else:
            self.oms.place_sell(self.trader_id, security, quantity, price_choice, t)

    def activeness(self):
        if self.oms.bank_balance < 1000:
            self.active = False
        return self.active
