from loguru import logger
from utils import tengers

# init handlers
from handlers import echo

def start():
    print("start")
    tengers.run()

if __name__ == "__main__":
    logger.info("Bot is starting")
    start()
    logger.info("Bot is stopped")
