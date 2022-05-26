from utils import parse, load_env
from loguru import logger
import sys

def on_start():
    (path, err) = parse()
    if err != None:
        logger.error(err)
        sys.exit()

    env = load_env(path)

if __name__ == "__main__":
    on_start()
    logger.info("Bot is started")