from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy import BinaryExpression
from sqlalchemy.orm import DeclarativeBase


class BaseRepository(ABC):
    def __init__(self):
        pass

    def create(self, data: Type[DeclarativeBase]):
        pass

    def read(self, filter: BinaryExpression) -> Type[DeclarativeBase]:
        pass

    def update(self, filter: BinaryExpression, data: Type[DeclarativeBase]):
        pass

    def delete(self, filter: BinaryExpression):
        pass



