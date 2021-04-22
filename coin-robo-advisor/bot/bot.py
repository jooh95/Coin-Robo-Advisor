from abc import ABC, abstractmethod
from constants import position
from logger import logger

class AbstractBot(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_current_position(self):
        pass

    @abstractmethod
    def get_target_ticker(self):
        pass

    @abstractmethod
    def select_investment_strategy(self):
        pass

    @abstractmethod
    def buy_crypto_currency(self, ticker, target_price):
        pass

    @abstractmethod
    def set_current_position(self):
        pass

    @abstractmethod
    def sell_crypto_currency(self):
        pass

    @abstractmethod
    def set_current_position(self, position):
        pass

    @abstractmethod
    def get_current_price(self, ticker):
        pass

    @abstractmethod
    def get_current_balance(self):
        pass

    def invest(self):
        try:
            # 현재 포지션이 매수 or 매도인지 확인
            current_position = self.get_current_position()

            # 매매 대상 코인 선택
            ticker = self.get_target_ticker()

            # 현재 잔고 조회
            current_balance = self.get_current_balance()

            # 매매 전략 선택
            investment_strategy = self.select_investment_strategy()

            if current_position is position.BUY:  # 현재 포지션이 매수인 경우

                # 1 매수 목표가 계산
                buy_target_price = investment_strategy.get_target_buy_price(ticker)

                # 2. 현재가 조회
                current_price = self.get_current_price(ticker)

                # 3. 현재가가 매수 목표가 보다 크거나 같으면 매수 시도
                if current_price >= buy_target_price:
                    buy_fund_amount = investment_strategy.get_buy_fund_amount(ticker)  # 매수 정도 (원)
                    is_buy_success = self.buy_crypto_currency(ticker, buy_fund_amount)

                    # 매수했으면, 현재 포지션을 매도로 변경
                    if is_buy_success:
                        self.set_current_position(position.SELL)

            elif current_position is position.SELL:  # 현재 포지션이 매도인 경우

                # 1. 매도 목표가 계산
                sell_target_price = investment_strategy.get_target_sell_price(ticker)

                # 2. 현재가 조회
                current_price = self.get_current_price(ticker)

                # 3. 현재가가 매도 목표가 보다 크거나 같으면 매도 시도
                if current_price >= sell_target_price:
                    sell_coin_amount = investment_strategy.get_sell_coin_amount(ticker)  # 매도 정도 (원)
                    is_sell_success = self.sell_crypto_currency(ticker, sell_coin_amount)

                    # 매도했으면, 현재 포지션을 매수로 변경
                    if is_sell_success:
                        self.set_current_position(position.BUY)
        except Exception as e:
            logger.error(f'예외발생: {e}')
