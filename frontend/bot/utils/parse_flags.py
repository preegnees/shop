import argparse
import os.path

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='Path to the file with environment variables for bot.py. [bot.env]')
    args = parser.parse_args()
    return _is_exists(args.p)

def _is_exists(path):
    if os.path.exists(path):
        return path, None
    else:
        return None, f"Invalid path env file. Path: {path}"