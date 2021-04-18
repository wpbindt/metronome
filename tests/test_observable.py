from etronome.observable import Observable, Observer
from tests.doubles import FakeObserver


def test_observable() -> None:
    class ObservableContainer:
        obs = Observable[int]('_observers')

        def __init__(self) -> None:
            self._observers: list[Observer[int]] = []
            self.obs = 10

        def register(self, observer: Observer[int]) -> None:
            self._observers.append(observer)

    container_instance = ObservableContainer()
    fake_observer = FakeObserver[int]()
    container_instance.register(fake_observer)

    container_instance.obs += 10
    assert container_instance.obs == 20
    container_instance.obs = 30
    assert container_instance.obs == 30
    assert fake_observer.update_values == [20, 30]


def test_observable_transformer() -> None:
    class ObservableContainer:
        obs = Observable[int]('_observers', lambda x: x + 10)

        def __init__(self) -> None:
            self._observers: list[Observer[int]] = []
            self.obs = 10

        def register(self, observer: Observer[int]) -> None:
            self._observers.append(observer)

    container_instance = ObservableContainer()
    fake_observer = FakeObserver[int]()
    container_instance.register(fake_observer)

    container_instance.obs = 20
    assert container_instance.obs == 30
    assert fake_observer.update_values == [30]
