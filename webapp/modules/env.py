from dotenv import load_dotenv
import os

class EnvVars:

    def __init__(self) -> None:
        load_dotenv()
        self.user = os.getenv('USERNAME')
        self.passwd = os.getenv('PASSWORD')
        self.port = os.getenv('PORT')
        self.db = os.getenv('DB')
        