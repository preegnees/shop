from loguru import logger
from utils import tengers

# init handlers
from handlers import echo

def start():
    tengers.run()

def _remove_pycache(path):
    import os
    import shutil
    dir_list = os.listdir(path)
    for i in dir_list:
        if i == "__pycache__":
            shutil.rmtree(path + "\\" + i)
        else:
            if os.path.isdir(path + "\\" + i):
                _remove_pycache(path + "\\" + i)


if __name__ == "__main__":
    _remove_pycache("C:\\Users\\79174\\Desktop\\shop\\course_rest_api\\frontend\\bot")
    logger.info("Bot is starting")
    start()
    logger.info("Bot is stopped")
