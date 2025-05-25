from exchange.orderbook import OrderBook

class StockExchange:
    def __init__(self):
        self.current_prices = {"AAPL": 1, "TSLA": 2, "MSFT": 3, "GOOG": 4, "AMZN": 5}
        self.order_books = {sec: OrderBook() for sec in self.current_prices}

    def place_order(self, order):
        book = self.order_books[order.security]
        book.add_order(order)
        self.match_orders(order.security)

    def match_orders(self, security):
        book = self.order_books[security]
        fixed_quantity = 1000

        while book.bids and book.asks:
            best_bid = book.pop_best_bid()
            best_ask = book.pop_best_ask()

            if best_bid.trader_id == best_ask.trader_id:
                break

            if best_bid.price >= best_ask.price:
                buyer_pays = best_bid.price
                seller_receives = best_ask.price
                self.current_prices[security] = best_bid.price

                best_bid.oms.edit_account(security, buyer_pays, fixed_quantity, "BUY", best_bid.trader_id)
                best_ask.oms.edit_account(security, seller_receives, fixed_quantity, "SELL", best_ask.trader_id)
            else:
                book.add_order(best_bid)
                book.add_order(best_ask)
                break

    def get_best_bid_ask(self, security):
        book = self.order_books[security]
        return book.get_best_bid(), book.get_best_ask()
