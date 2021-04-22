from .bot import AbstractBot
from constants import position, ticker
from logger import logger
from trade_system import upbit
from invest_strategy import VolatilityBreakout
import pyupbit


class CoinBot(AbstractBot):

    def __init__(self, current_position=position.BUY, target_ticker=ticker.BITCOIN):
        self.current_position = current_position
        self.target_ticker = target_ticker

    def get_current_position(self):
        logger.info(f'현재 포지션: {self.current_position}')
        return self.current_position

    def set_current_position(self, position):
        self.current_position = position

    def get_target_ticker(self):
        # FIXME: 현재 매매 대상 ticker는 비트코인으로 고정
        logger.info(f'매매 대상 ticker: {self.target_ticker}')
        return self.target_ticker

    def select_investment_strategy(self):
        # FIXME: 현재 매수 전략은 변동성 돌파 전략으로 고정
        strategy = VolatilityBreakout()

        logger.info(f'선택된 매매 전략: {strategy.get_name()}')

        return strategy

    def buy_crypto_currency(self, ticker, buy_fund_amount):
        status = upbit.buy_market_order(ticker, buy_fund_amount)  # 시장가로 코인 매수 (수수료를 제외한 만큼의 코인이 구매됨)

        logger.info(f'매수 상태: {status}')

        if status.get('error'):
            return False

        return True

    def sell_crypto_currency(self, ticker, sell_coin_amount):
        status = upbit.sell_market_order(ticker, sell_coin_amount)  # 시장가로 코인 매도 (수수료를 제외한 금액이 입금)

        logger.info(f'매도 상태: {status}')

        if status.get('error'):
            return False

        return True

    def get_current_price(self, ticker):
        current_price = pyupbit.get_current_price(ticker)  # 현재가

        logger.info(f'현재가: {current_price}원')

        return current_price

    def get_current_balance(self):
        current_balance = upbit.get_balance(ticker='KRW')

        logger.info(f'현재잔고: {current_balance}원')

        return current_balance
