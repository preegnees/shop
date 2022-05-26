from utils import config
from loguru import logger


def start():
    print(config.get_env())


if __name__ == "__main__":
    start()
    logger.info("Bot is started")
