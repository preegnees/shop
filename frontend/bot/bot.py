from loguru import logger
from handlers import echo
from utils import tengers

def start():
    print("start")
    tengers.run()

if __name__ == "__main__":
    logger.info("Bot is starting")
    start()
    logger.info("Bot is stopped")
