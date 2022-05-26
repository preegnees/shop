from loguru import logger
from utils import tengers

def start():
    tengers.run()


if __name__ == "__main__":
    logger.info("Bot is starting")
    start()
    logger.info("Bot is stopped")
