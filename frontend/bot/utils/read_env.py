from dotenv import dotenv_values

def load_env(path):
    return dotenv_values(path)