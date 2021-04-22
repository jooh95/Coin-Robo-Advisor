from .invest_strategy import AbstractInvestStrategy
import pyupbit
from logger import logger
from constants import strategy_name


class VolatilityBreakout(AbstractInvestStrategy):

    def __init__(self):
        self.variation_rate = 0.5

    def get_target_buy_price(self, ticker):
        df = pyupbit.get_ohlcv(ticker, interval="minute10", count=1).iloc[0]  # 최근 영업일부터 10분 동안의 데이터를 조회

        open_price = df['open']  # 시가
        high_price = df['high']  # 고가
        low_price = df['low']  # 저가
        target_price = open_price + (high_price - low_price) * self.variation_rate  # 매수 목표가

        logger.info(f'매수 목표가: {target_price}원')
        return target_price

    def get_buy_fund_amount(self, ticker):
        # FIXME: 현재는 최소 금액만큼만 매수하도록 설정
        return 5000

    def get_target_sell_price(self, ticker):
        # FIXME: 현재는 무조건 시장가로 매도하도록 설정
        return 0

    def get_sell_coin_amount(self, ticker):
        # FIXME: 현재는 최소 금액만큼만 매도하도록 설정
        current_price = pyupbit.get_current_price(ticker)  # 현재가
        sell_coin_amount = round(1 / current_price * 5000, 8)
        logger.info(f'매도 코인량: {sell_coin_amount}개')
        return sell_coin_amount

    def get_name(self):
        return strategy_name.VOLATILITY_BREAKOUT
