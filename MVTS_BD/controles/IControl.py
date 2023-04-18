from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class IControl(ABC):
    def __init__(self, session: Session):
        self._session = session

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj):
        pass
