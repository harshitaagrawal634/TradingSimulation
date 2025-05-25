from exchange.order import Order

class OrderManagementSystem:
    def __init__(self, bank_balance, initial_cash_trading, portfolio, exchange):
        self.bank_balance = bank_balance
        self.cash = initial_cash_trading
        self.portfolio = portfolio
        self.exchange = exchange

    def portfolio_value_current(self, security, quantity):
        self.portfolio[security] = self.portfolio.get(security, 0) + quantity

    def can_place_order(self, price, quantity, order_type, security):
        if order_type == "BUY":
            return self.cash >= price * quantity
        elif order_type == "SELL":
            return self.portfolio.get(security, 0) >= quantity
        return False

    def edit_account(self, security, price, quantity, order_type, trader_idd):
        if order_type == "BUY":
            if self.cash < price * quantity:
                print(f"Trade Rejected for: {security} as {trader_idd} does not have enough cash!\n")
                return
            self.cash -= price * quantity
            self.portfolio_value_current(security, quantity)
            print(f"{trader_idd} pays: ${price} per share for {security}")
        else:
            if self.portfolio.get(security, 0) < quantity:
                print(f"Trade Rejected for: {security} as {trader_idd} does not have enough stocks!\n")
                return
            self.cash += price * quantity
            self.portfolio_value_current(security, -quantity)
            print(f"{trader_idd} receives: ${price} per share for {security}")

    def add_cash(self, quantity, price_choice):
        print(f"amount needed {quantity * price_choice}\n")
        amt = int(input(f"Current bank_balance: {self.bank_balance}, current trading_balance={self.cash}, how much do you want to transfer?\n"))
        if self.bank_balance >= amt:
            self.cash += amt
            self.bank_balance -= amt
            print(f"Transferred {amt} from bank to trading account. Bank Balance: {self.bank_balance}, Trading Cash: {self.cash}\n")
        else:
            print(f"Insufficient funds in bank. Available: {self.bank_balance}\n")
            return 0

    def place_buy(self, trader_id, security, quantity, price_choice, t):
        if self.can_place_order(price_choice, quantity, "BUY", security):
            order = Order(trader_id, security, price_choice, quantity, "BUY", t, self)
            self.exchange.place_order(order)
        else:
            print(f"Insufficient funds for transaction of security {security} for {trader_id}. Available: {self.cash}")
            ch = input("Do you want to transfer cash? y/n\n")
            if ch == 'y':
                self.add_cash(quantity, price_choice)

    def place_sell(self, trader_id, security, quantity, price_choice, t):
        if self.can_place_order(price_choice, quantity, "SELL", security):
            order = Order(trader_id, security, price_choice, quantity, "SELL", t, self)
            self.exchange.place_order(order)
        else:
            print(f"{trader_id} does not have enough securities {security} to sell\n")
