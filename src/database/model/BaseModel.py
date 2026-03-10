from abc import ABC, abstractmethod
from typing import Type


class BaseModel(ABC):

    @staticmethod
    @abstractmethod
    def create_model(*args, **kwargs) -> Type["BaseModel"]:
        pass
