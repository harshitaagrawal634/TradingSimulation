import time

class Order:
    """Represents a Buy/Sell Order"""
    def __init__(self, trader_id, security, price, quantity, order_type, timestamp, oms):
        self.trader_id = trader_id
        self.security = security
        self.price = price
        self.quantity = quantity
        self.order_type = order_type
        self.timestamp = timestamp
        self.oms = oms

    def __lt__(self, other):
        if self.price == other.price:
            return self.timestamp < other.timestamp
        return self.price > other.price if self.order_type == "BUY" else self.price < other.price
