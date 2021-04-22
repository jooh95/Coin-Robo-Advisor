from abc import ABC, abstractmethod


class AbstractInvestStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_target_buy_price(self, ticker):
        pass

    @abstractmethod
    def get_buy_fund_amount(self, ticker):
        pass

    @abstractmethod
    def get_target_sell_price(self, ticker):
        pass

    @abstractmethod
    def get_sell_coin_amount(self, ticker):
        pass
