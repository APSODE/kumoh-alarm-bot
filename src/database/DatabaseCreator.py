from typing import Literal, Dict

from sqlalchemy import create_engine

from utils.metaclass.SingletonMeta import SingletonMeta


class DatabaseCreator(metaclass = SingletonMeta):
    def __init__(self, database_account: Dict[Literal["id", "pw"], str]):
        self._engine = create_engine(
            f"mysql+pymysql://{database_account.get("id")}:{database_account.get("pw")}@127.0.0.1:3306/kab_db",
            echo = True
        )

    @staticmethod
    def create_object(database_account: Dict[Literal["id", "pw"], str]):
        return DatabaseCreator(database_account = database_account)
