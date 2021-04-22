from bot import CoinBot
from apscheduler.schedulers.blocking import BlockingScheduler
from logger import logger
from constants import position


def investment_job(*args):
    coin_bot = args[0]

    logger.info("----------COIN_ROBO_ADVISOR----------")
    logger.info("자동투자 시작")

    coin_bot.invest()

    logger.info("자동투자 종료")
    logger.info("-------------------------------------\n")


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    coin_bot = CoinBot()

    # 매 10분마다 투자 job 실행
    scheduler.add_job(investment_job, 'cron', minute="*/10", args=[coin_bot])

    scheduler.start()
