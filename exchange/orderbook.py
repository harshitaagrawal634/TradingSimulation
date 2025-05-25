import heapq

class OrderBook:
    def __init__(self):
        self.bids = []  # Max heap for bids
        self.asks = []  # Min heap for asks

    def add_order(self, order):
        if order.order_type == "BUY":
            heapq.heappush(self.bids, (-order.price, order))
        else:
            heapq.heappush(self.asks, (order.price, order))

    def get_best_bid(self):
        return -self.bids[0][0] if self.bids else None

    def get_best_ask(self):
        return self.asks[0][0] if self.asks else None

    def pop_best_bid(self):
        return heapq.heappop(self.bids)[1] if self.bids else None

    def pop_best_ask(self):
        return heapq.heappop(self.asks)[1] if self.asks else None
