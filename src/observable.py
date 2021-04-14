from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    @abstractmethod
    def update_(self, value: T):
        ...


class Observable(Generic[T]):
    def __init__(self, observers: list[Observer[T]]) -> None:
        self._observers = observers
        self._value: Optional[T] = None

    def __set__(self, obj: object, value: T) -> None:
        self._value = value
        for observer in self._observers:
            observer.update_(value)

    def __get__(self, obj: object, type=None) -> T:
        if self._value is None:
            raise AttributeError('Value not set')
        return self._value
