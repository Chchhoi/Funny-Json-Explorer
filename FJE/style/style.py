from abc import ABC, abstractmethod

class Style(ABC):
    @abstractmethod
    def draw(self, data, icon_family):
        pass