from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    @abstractmethod
    def update_(self, value: T) -> None:
        ...


class Observable(Generic[T]):
    def __init__(self, observers: str) -> None:
        self.observers = observers

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name

    def __set__(self, instance: object, value: T) -> None:
        instance.__dict__[self.name] = value
        observers = instance.__dict__[self.observers]
        for observer in observers:
            observer.update_(value)

    def __get__(self, instance: object, owner: type = None) -> T:
        return instance.__dict__[self.name]
